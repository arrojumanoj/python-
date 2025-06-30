# Log File Analysis & Reporting System

Instructions:
1. Create MySQL DB: `CREATE DATABASE weblogs_db;`
2. Edit `config.ini` with your DB credentials.
3. Run `pip install -r requirements.txt`
4. Run `python main.py process_logs sample_logs/access.log`
5. Run reports with `python main.py generate_report top_n_ips 5`