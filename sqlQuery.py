# DROP TABLES
FactSongPlay_table_drop = "DROP TABLE IF EXISTS FACT_SONGPLAY"
DimLocation_table_drop = "DROP TABLE IF EXISTS DIM_LOCATION"
DimUser_table_drop = "DROP TABLE IF EXISTS DIM_USER"
DimSong_table_drop = "DROP TABLE IF EXISTS DIM_SONG"
DimArtist_table_drop = "DROP TABLE IF EXISTS DIM_ARTIST"
DimDate_table_drop = "DROP TABLE IF EXISTS DIM_DATE"
DimTime_table_drop = "DROP TABLE IF EXISTS DIM_TIME"


# create table
FactSongPlay_table_create = ("""CREATE TABLE IF NOT EXISTS FACT_SONGPLAY(
	songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
	start_date_id INT REFERENCES DIM_DATE (date_id),
    start_time_id INT REFERENCES DIM_TIME (time_id),
	user_id INT REFERENCES DIM_USER (user_id),
	level VARCHAR NOT NULL,
	song_id VARCHAR REFERENCES DIM_SONG (song_id),
	artist_id VARCHAR REFERENCES DIM_ARTIST (artist_id),
	session_id INT NOT NULL, 
	location_id INT REFERENCES DIM_LOCATION (location_id),
	user_agent VARCHAR
)""")

DimLocation_table_create = ("""CREATE TABLE IF NOT EXISTS  DIM_LOCATION(
	location_id SERIAL CONSTRAINT location_pk PRIMARY KEY,
	location  VARCHAR
)""")

DimUser_table_create = ("""CREATE TABLE IF NOT EXISTS  DIM_USER(
	user_id INT CONSTRAINT user_pk PRIMARY KEY,
	first_name VARCHAR,
	last_name VARCHAR,
	gender VARCHAR
)""")

DimArtist_table_create = ("""CREATE TABLE  IF NOT EXISTS DIM_ARTIST(
	artist_id VARCHAR CONSTRAINT artist_pk PRIMARY KEY,
	artist_name VARCHAR,
	location VARCHAR,
	latitude DECIMAL,
	longitude DECIMAL
)""")

DimSong_table_create = ("""CREATE TABLE  IF NOT EXISTS DIM_SONG(
	song_id VARCHAR CONSTRAINT song_pk PRIMARY KEY,
	title  VARCHAR,
	artist_id VARCHAR,
	year INT,
	duration FLOAT
)""")

DimDate_table_create = ("""CREATE TABLE IF NOT EXISTS DIM_DATE (
    date_id SERIAL CONSTRAINT date_pk PRIMARY KEY,
    day INT NOT NULL,
    week INT NOT NULL,
	month INT NOT NULL,
	year INT NOT NULL,
	weekday VARCHAR NOT NULL,
    date_full DATE NOT NULL
)""")

DimTime_table_create = ("""CREATE TABLE IF NOT EXISTS DIM_TIME (
    time_id SERIAL CONSTRAINT time_pk PRIMARY KEY,
	hour INT NOT NULL,
	minute INT NOT NULL,
 	second INT NOT NULL,
    time_full TIME NOT NULL,
    timeBySecond INT NOT NULL
)""")


# QUERY LISTS
create_table_queries = [DimLocation_table_create, DimArtist_table_create, DimUser_table_create, DimSong_table_create, DimDate_table_create, DimTime_table_create, FactSongPlay_table_create]
drop_table_queries = [FactSongPlay_table_drop, DimTime_table_drop, DimDate_table_drop, DimSong_table_drop, DimUser_table_drop, DimArtist_table_drop, DimLocation_table_drop]

