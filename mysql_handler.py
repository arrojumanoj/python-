import mysql.connector
import logging

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute(open("sql/create_tables.sql", "r").read())
        self.conn.commit()

    def insert_batch_log_entries(self, log_data_list):
        for log_data in log_data_list:
            self.cursor.execute(
                "INSERT INTO log_entries (ip_address, timestamp, method, path, status_code, bytes_sent, referrer, user_agent_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, NULL)",  # Simplified for demo
                (log_data['ip_address'], log_data['timestamp'], log_data['method'],
                 log_data['path'], log_data['status_code'], log_data['bytes_sent'], log_data['referrer'])
            )
        self.conn.commit()

    def get_top_n_ips(self, n):
        self.cursor.execute(
            "SELECT ip_address, COUNT(*) AS request_count FROM log_entries GROUP BY ip_address ORDER BY request_count DESC LIMIT %s",
            (n,)
        )
        return self.cursor.fetchall()

    def get_status_code_distribution(self):
        self.cursor.execute(
            "SELECT status_code, COUNT(*) AS count, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM log_entries)) AS percentage "
            "FROM log_entries GROUP BY status_code ORDER BY count DESC"
        )
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
