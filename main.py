from log_parser import LogParser
from sqlite_handler import SQLiteHandler
from cli_manager import CLIManager

def main():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'your_password',
        'database': 'weblogs_db'
    }
    db_handler = SQLiteHandler()
    db_handler.create_tables()

    cli_manager = CLIManager(db_handler)
    cli_manager.run()

    db_handler.close()

if __name__ == "__main__":
    main()
