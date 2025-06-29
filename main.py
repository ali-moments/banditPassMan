import sqlite3
import argparse

class DB:
    def __init__(self, db_name='data.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS levels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                secret TEXT,
                solve TEXT
            )
        ''')
        self.conn.commit()

    def save_level(self, username, password, secret, solve=''):
        self.cursor.execute('''
            INSERT INTO levels (username, password, secret, solve) VALUES (?, ?, ?, ?)
        ''', (username, password, secret, solve))
        self.conn.commit()

    def load_levels(self):
        self.cursor.execute('SELECT * FROM levels')
        return self.cursor.fetchall()

    def load_level_by_username(self, username):
        self.cursor.execute('SELECT * FROM levels WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def update_level(self, username, password, secret, solve):
        self.cursor.execute('''
            UPDATE levels SET password = ?, secret = ?, solve = ? WHERE username = ?
        ''', (password, secret, solve, username))
        self.conn.commit()

    def close(self):
        self.conn.close()

def list_levels(db):
    levels = db.load_levels()
    for level in levels:
        print(level)

def show_level(db, username):
    level = db.load_level_by_username(username)
    if level:
        print(level)
    else:
        print(f"No level found for username: {username}")

def add_level(db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    secret = input("Enter secret: ")
    solve = input("Enter solve: ")
    db.save_level(username, password, secret, solve)
    print("Level added successfully.")

def edit_level(db, username):
    level = db.load_level_by_username(username)
    if level:
        print(f"Editing level for username: {username}")
        password = input("Enter new password: ")
        secret = input("Enter new secret: ")
        solve = input("Enter new solve: ")
        db.update_level(username, password, secret, solve)
        print("Level updated successfully.")
    else:
        print(f"No level found for username: {username}")

def main():
    parser = argparse.ArgumentParser(description="CLI-based BanditPassMan")
    parser.add_argument("command", choices=["list", "show", "add", "edit"], help="Command to execute")
    parser.add_argument("username", nargs="?", help="Username for show/edit commands")
    args = parser.parse_args()

    db = DB()

    try:
        if args.command == "list":
            list_levels(db)
        elif args.command == "show":
            if args.username:
                show_level(db, args.username)
            else:
                print("Please provide a username for the 'show' command.")
        elif args.command == "add":
            add_level(db)
        elif args.command == "edit":
            if args.username:
                edit_level(db, args.username)
            else:
                print("Please provide a username for the 'edit' command.")
    finally:
        db.close()

if __name__ == "__main__":
    main()