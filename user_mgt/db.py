import os
import dotenv
import pymysql as mysql
from datetime import datetime

dotenv.load_dotenv()

user = os.getenv('DB_USER')
database = os.getenv('DB_NAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))

with mysql.connect(user=user, password=password, database=database, host=host, port=port) as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("""
    
        CREATE TABLE users (
        id INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        dob DATE,
        password VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
        );
    """)

    cursor.execute("INSERT INTO users (first_name, last_name, password, dob) VALUES (%s, %s, %s, %s)", ("Banke", "Owolabi", "password", datetime(1990, 10, 10)))

    cursor.execute("select * from users")
    user = cursor.fetchone()

    print(user)
    connection.commit()
