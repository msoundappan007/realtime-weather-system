import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "weather_data.db"


@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_summaries (
                
                date TEXT,
                city TEXT,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                avg_humidity REAL,      -- New field
                avg_wind_speed REAL,    -- New field
                dominant_condition TEXT,
                PRIMARY KEY (date, city)
            )
        ''')
        
       

init_db()
