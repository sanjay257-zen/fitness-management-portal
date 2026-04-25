import sqlite3

# Database configuration
DATABASE_NAME = 'fitness_management.db'

# Table creation queries
CREATE_USERS_TABLE = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

CREATE_TRAINERS_TABLE = '''
CREATE TABLE IF NOT EXISTS trainers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

CREATE_CLASSES_TABLE = '''
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration INTEGER NOT NULL,
    trainer_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id)
);
'''

CREATE_PACKAGES_TABLE = '''
CREATE TABLE IF NOT EXISTS packages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    duration INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

CREATE_REGISTRATIONS_TABLE = '''
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    class_id INTEGER,
    package_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (class_id) REFERENCES classes (id),
    FOREIGN KEY (package_id) REFERENCES packages (id)
);
'''

CREATE_TRAINER_SCHEDULES_TABLE = '''
CREATE TABLE IF NOT EXISTS trainer_schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trainer_id INTEGER,
    class_id INTEGER,
    schedule_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id),
    FOREIGN KEY (class_id) REFERENCES classes (id)
);
'''

# Function to initialize the database
def initialize_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Creating tables
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_TRAINERS_TABLE)
    cursor.execute(CREATE_CLASSES_TABLE)
    cursor.execute(CREATE_PACKAGES_TABLE)
    cursor.execute(CREATE_REGISTRATIONS_TABLE)
    cursor.execute(CREATE_TRAINER_SCHEDULES_TABLE)
    conn.commit()
    conn.close()

# Initialize the database
if __name__ == '__main__':
    initialize_db()