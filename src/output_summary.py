import json
import psycopg2
import os

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST')
}

def fetch_summary(cursor):
    cursor.execute("""
        SELECT p.given_name, p.family_name, p.date_of_birth, pl.city, pl.county, pl.country
        FROM people p
        JOIN places pl ON p.place_of_birth = pl.city
    """)
    rows = cursor.fetchall()
    summary = []
    for row in rows:
        summary.append({
            'given_name': row[0],
            'family_name': row[1],
            'date_of_birth': row[2].strftime('%Y-%m-%d'),
            'city': row[3],
            'county': row[4],
            'country': row[5]
        })
    return summary

def main():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    summary = fetch_summary(cursor)
    
    with open('../data/summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
