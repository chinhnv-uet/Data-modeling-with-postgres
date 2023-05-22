import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
import datetime

def getConnectMongo():
    ''' Connect to source MongoDB to read data'''
    CONNECTION_STRING = "mongodb://chinhnv:123456%40!@localhost:27017/products"
    client = MongoClient(CONNECTION_STRING)
    return client['products']

def getConnectPostgres():
    destDb = 'postgresql://chinhnv:123456@localhost:5432/chinhnv'
    db = create_engine(destDb)
    return db, db.connect()

def getDate(s):
    return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d')

def getTime(s):
    return datetime.datetime.fromtimestamp(s).strftime('%H:%M:%S')

def loadFactSongPlay(srcDb, engine, connDest):
    df = pd.DataFrame(list(srcDb['musicWebLog'].find({}, {'_id': 0, 'ts': 1, 'userId' : 1, 'level' : 1, 'song' : 1, 'artist' : 1, 'sessionId' : 1, 'location' : 1, 'userAgent' : 1})))
    df['ts'] = df['ts']//1000
    df['start_date'] = df['ts'].apply(getDate)
    df['start_time'] = df['ts'].apply(getTime)
    df = df.rename(columns={'userId': 'user_id', 'sessionId': 'session_id', 'userAgent': 'user_agent'})
    
    # song -> song_id
    songTab = pd.read_sql_query('select * from "dim_song"',con=engine)
    songTab = songTab[['title', 'song_id']].copy().rename(columns={'title': 'song'})
    df = pd.merge(df, songTab, on='song', how='left')
    
    # artist -> artist_id
    artists = pd.read_sql_query('select * from "dim_artist"',con=engine)
    artists = artists[['artist_name', 'artist_id']].copy().rename(columns={'artist_name': 'artist'})
    df = pd.merge(df, artists, on='artist', how='left')
    
    # location -> location_id
    locations = pd.read_sql_query('select * from "dim_location"',con=engine)
    df = pd.merge(df, locations, on='location', how='inner')
    
    # start_date -> start_date_id
    dates = pd.read_sql_query('select * from "dim_date";', con=engine)
    dates = dates[['date_full', 'date_id']]
    dates['date_full'] = dates['date_full'].astype(str)
    dates = dates.rename(columns={'date_full': 'start_date', 'date_id': 'start_date_id'})
    df = pd.merge(df, dates, on='start_date', how='inner')
    
    # start_time -> start_time_id
    times = pd.read_sql_query('select * from "dim_time"',con=engine)
    times = times[['time_full', 'time_id']].copy().rename(columns={'time_full': 'start_time', 'time_id': 'start_time_id'})
    times['start_time'] = times['start_time'].astype(str)
    df = pd.merge(df, times, on='start_time', how='inner')
    
    # select specific columns for load
    df = df[['start_date_id', 'start_time_id', 'user_id', 'level', 'song_id', 'artist_id', 'session_id', 'location_id', 'user_agent']].copy()
    df['user_id'] = df['user_id'].replace('', None)
    # df['songplay_id'] = range(len(df))
    df.to_sql('fact_songplay', con=connDest, if_exists='append', index=True, index_label='songplay_id')

    print("Done load fact songPlay")

def execute():
    # Get connect to source DB and destination DB
    srcDb = getConnectMongo()
    engine, connDest = getConnectPostgres()
    
    #Load fact
    loadFactSongPlay(srcDb, engine, connDest)