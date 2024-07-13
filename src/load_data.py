import csv
import psycopg2
import os

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST')
}

def load_places(cursor, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO places (city, county, country) VALUES (%s, %s, %s)
            """, (row['city'], row['county'], row['country']))

def load_people(cursor, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO people (given_name, family_name, date_of_birth, place_of_birth) VALUES (%s, %s, %s, %s)
            """, (row['given_name'], row['family_name'], row['date_of_birth'], row['place_of_birth']))

def main():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    load_places(cursor, '../data/places.csv')
    load_people(cursor, '../data/people.csv')
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
