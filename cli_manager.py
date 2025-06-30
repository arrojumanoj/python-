import argparse
from log_parser import LogParser
from tabulate import tabulate
import logging

class CLIManager:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.parser = argparse.ArgumentParser(description="Log Analyzer CLI")
        self._setup_parser()

    def _setup_parser(self):
        subparsers = self.parser.add_subparsers(dest='command')
        process_parser = subparsers.add_parser('process_logs')
        process_parser.add_argument('file_path', type=str)
        process_parser.add_argument('--batch_size', type=int, default=1000)

        report_parser = subparsers.add_parser('generate_report')
        report_subparsers = report_parser.add_subparsers(dest='report_type')
        top_ips_parser = report_subparsers.add_parser('top_n_ips')
        top_ips_parser.add_argument('n', type=int)
        report_subparsers.add_parser('status_code_distribution')

    def run(self):
        args = self.parser.parse_args()
        if args.command == 'process_logs':
            parser = LogParser()
            batch, count = [], 0
            with open(args.file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    parsed = parser.parse_line(line)
                    if parsed:
                        batch.append(parsed)
                    if len(batch) >= args.batch_size:
                        self.db_handler.insert_batch_log_entries(batch)
                        count += len(batch)
                        batch = []
            if batch:
                self.db_handler.insert_batch_log_entries(batch)
                count += len(batch)
            logging.info(f"Processed {count} lines.")
        elif args.command == 'generate_report':
            if args.report_type == 'top_n_ips':
                results = self.db_handler.get_top_n_ips(args.n)
                print(tabulate(results, headers=["IP", "Count"], tablefmt="grid"))
            elif args.report_type == 'status_code_distribution':
                results = self.db_handler.get_status_code_distribution()
                print(tabulate(results, headers=["Code", "Count", "Percent"], tablefmt="grid"))
