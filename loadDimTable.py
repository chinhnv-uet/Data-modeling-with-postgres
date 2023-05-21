import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
import pandas as pd
import datetime as dt

def getConnectMongo():
    ''' Connect to source MongoDB to read data'''
    CONNECTION_STRING = "mongodb://chinhnv:123456%40!@localhost:27017/products"
    client = MongoClient(CONNECTION_STRING)
    return client['products']

def getConnectPostgres():
    destDb = 'postgresql://chinhnv:123456@localhost:5432/chinhnv'
    db = create_engine(destDb)
    return db.connect()
    
def loadDimLocation(srcDb, connDest):
    df = pd.DataFrame(list(srcDb['musicWebLog'].find()))
    locationData = df.location.unique()
    data = pd.DataFrame()
    data['location'] = locationData
    data['location_id'] = [int(i) for i in range(len(data))]
    data.to_sql('dim_location', con=connDest, if_exists='append', index=False)
    print("Done load dim location")

def loadDimUser(srcDb, connDest):
    df = pd.DataFrame(list(srcDb['musicWebLog'].find({}, {'_id': 0, 'userId': 1, 'firstName' : 1, 'lastName' : 1, 'gender' : 1})))
    df = df.drop_duplicates('userId')
    df = df.replace({'gender': 'F'}, "Female").replace({'gender': 'M'}, "Male").replace({"userId": ''}, "-1")
    df = df.rename(columns={"firstName": "first_name", "lastName": "last_name", "userId": "user_id"})
    df.to_sql('dim_user', con=connDest, if_exists='append', index=False)
    print("Done load dim user")

def loadDimArtist(srcDb, connDest):
    df = pd.DataFrame(list(srcDb['songs'].find({}, {'_id': 0, 'artist_id': 1, 'artist_name' : 1, 'artist_location' : 1, 'artist_latitude' : 1, 'artist_longitude' : 1})))
    df = df.drop_duplicates('artist_id')
    df = df.rename(columns={"artist_location": "location", "artist_latitude": "latitude", "artist_longitude": "longitude"})
    df.to_sql('dim_artist', con=connDest, if_exists='append', index=False)
    print("Done load dim artist")

def loadDimSong(srcDb, connDest):
    df = pd.DataFrame(list(srcDb['songs'].find({}, {'_id': 0, 'song_id': 1, 'artist_id' : 1, 'title' : 1, 'year' : 1, 'duration' : 1})))
    df = df.drop_duplicates('song_id')
    df.to_sql('dim_song', con=connDest, if_exists='append', index=False)
    print("Done load dim song")

def loadDimDate(srcDb, connDest):
    data = []

    start_date = dt.date(2010, 1, 1)
    end_date = dt.date(2030, 12, 31)

    current_date = start_date
    while current_date <= end_date:
        day = current_date.day
        month = current_date.month
        year = current_date.year
        week = current_date.isocalendar()[1]
        weekday = current_date.strftime('%a')
        datefull = current_date.strftime('%Y-%m-%d')
        
        data.append([day, month, year, week, weekday, datefull])
        
        current_date += dt.timedelta(days=1)

    df = pd.DataFrame(data, columns=['day', 'month', 'year', 'week', 'weekday', 'date_full'])
    df['date_id'] = [int(i) for i in range(len(df))]
    df.to_sql('dim_date', con=connDest, if_exists='append', index=False)
    print("Done load dim date")
    
def loadDimTime(srcDb, connDest):
    data = []
    date = dt.date.today()
    for second in range(0, 86400):
        hour = second // 3600
        minute_of_hour = (second % 3600) // 60
        second_of_minute = second % 60
        
        current_time = dt.datetime.combine(date, dt.time(hour=hour, minute=minute_of_hour, second=second_of_minute))
        
        time_full = current_time.strftime('%H:%M:%S')
        timebysecond = second
        
        data.append([hour, minute_of_hour, second_of_minute, time_full, timebysecond])

    df = pd.DataFrame(data, columns=['hour', 'minute', 'second', 'time_full', 'timebysecond'])
    df['time_id'] = [int(i) for i in range(len(df))]
    df.to_sql('dim_time', con=connDest, if_exists='append', index=False)
    print("Done load dim time")

def execute():
    # Get connect to source DB and destination DB
    srcDb = getConnectMongo()
    connDest = getConnectPostgres()

    #Load location
    loadDimLocation(srcDb, connDest)
    
    #load artist
    loadDimArtist(srcDb, connDest)
    
    #load user
    loadDimUser(srcDb, connDest)
    
    # load date
    loadDimDate(srcDb, connDest)

    # load time
    loadDimTime(srcDb, connDest)
    
    #load song
    loadDimSong(srcDb, connDest)