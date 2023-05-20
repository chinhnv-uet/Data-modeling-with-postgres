# DROP TABLES
FactSongPlay_table_drop = "DROP TABLE  IF EXISTS songplays"
DimLocation_table_create = "DROP TABLE IF EXISTS  users"
DimUser_table_create = "DROP TABLE IF EXISTS  songs"
DimSong_table_create = "DROP TABLE  IF EXISTS artists"
DimArtist_table_create = "DROP TABLE  IF EXISTS time"
DimDate_table_create = "DROP TABLE  IF EXISTS time"
DimTime_table_create = "DROP TABLE  IF EXISTS time"


# create table
FactSongPlay_table_create = ("""CREATE TABLE IF NOT EXISTS FACT_SONGPLAY(
	songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
	start_date_id DATE REFERENCES DIM_DATE (date_id),
    start_time_id TIME REFERENCES DIM_TIME (time_id),
	user_id INT REFERENCES DIM_USER (user_id),
	level VARCHAR NOT NULL,
	song_id VARCHAR REFERENCES DIM_SONG (song_id),
	artist_id VARCHAR REFERENCES DIM_ARTIST (artist_id),
	session_id INT NOT NULL, 
	location_id INT REFERENCES DIM_LOCATION (location_id),
	user_agent TEXT
)""")

DimLocation_table_create = ("""CREATE TABLE IF NOT EXISTS  DIM_LOCATION(
	location_id SERIAL CONSTRAINT location_pk PRIMARY KEY,
	location  VARCHAR,
)""")

DimUser_table_create = ("""CREATE TABLE IF NOT EXISTS  DIM_USER(
	user_id INT CONSTRAINT user_pk PRIMARY KEY,
	first_name VARCHAR,
	last_name VARCHAR,
	gender VARCHAR,
)""")

DimSong_table_create = ("""CREATE TABLE  IF NOT EXISTS DIM_SONG(
	song_id VARCHAR CONSTRAINT song_pk PRIMARY KEY,
	title  VARCHAR,
	artist_id  VARCHAR REFERENCES DIM_ARTIST (artist_id),
	year INT,
	duration FLOAT
)""")

DimArtist_table_create = ("""CREATE TABLE  IF NOT EXISTS DIM_ARTIST(
	artist_id VARCHAR CONSTRAINT artist_pk PRIMARY KEY,
	name VARCHAR,
	location_id INT REFERENCES DIM_LOCATION (location_id),
	latitude DECIMAL,
	longitude DECIMAL
)""")

DimDate_table_create = ("""CREATE TABLE IF NOT EXISTS DIM_DATE (
    date_id SERIAL CONSTRAINT date_pk PRIMARY KEY,
    day INT NOT NULL CHECK (day >= 0),
    week INT NOT NULL CHECK (week >= 0),
	month INT NOT NULL CHECK (month >= 0),
	year INT NOT NULL CHECK (year >= 0),
	weekday VARCHAR NOT NULL,
    date_full DATE NOT NULL
)""")

DimTime_table_create = ("""CREATE TABLE IF NOT EXISTS DIM_TIME (
    time_id SERIAL CONSTRAINT time_pk PRIMARY KEY,
	hour INT NOT NULL CHECK (hour >= 0),
	minute INT NOT NULL CHECK (minute >= 0),
    time_full TIME NOT NULL,
    timeBySecond INT NOT NULL
)""")


# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s )
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (user_id) DO UPDATE SET 
                        level = EXCLUDED.level 
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (song_id) DO NOTHING                        
""")


# Artist location, latitude and longitude might change and need to be updated.
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) 
                          ON CONFLICT (artist_id) DO UPDATE SET
                          location = EXCLUDED.location,
                          latitude = EXCLUDED.latitude,
                          longitude = EXCLUDED.longitude
""")

time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")


# QUERY LISTS
create_table_queries = [FactSongPlay_table_create, DimLocation_table_create, DimUser_table_create, DimSong_table_create, DimArtist_table_create, DimDate_table_create, DimTime_table_create]
drop_table_queries = [FactSongPlay_table_drop, DimLocation_table_create, DimUser_table_create, DimSong_table_create, DimArtist_table_create, DimDate_table_create, DimTime_table_create]

