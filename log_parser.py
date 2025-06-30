import re
from datetime import datetime
import logging

class LogParser:
    LOG_PATTERN = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"'
    )

    def parse_line(self, log_line):
        match = self.LOG_PATTERN.match(log_line)
        if match:
            ip_address = match.group(1)
            timestamp_str = match.group(2)
            request = match.group(3)
            status_code = int(match.group(4))
            bytes_sent = int(match.group(5)) if match.group(5) != '-' else 0
            referrer = match.group(6) if match.group(6) != '-' else None
            user_agent = match.group(7) if match.group(7) != '-' else None

            request_parts = request.split(' ')
            method = request_parts[0] if len(request_parts) > 0 else None
            path = request_parts[1] if len(request_parts) > 1 else None

            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')

            return {
                'ip_address': ip_address,
                'timestamp': timestamp,
                'method': method,
                'path': path,
                'status_code': status_code,
                'bytes_sent': bytes_sent,
                'referrer': referrer,
                'user_agent': user_agent
            }

        logging.warning(f"Malformed log line: {log_line.strip()}")
        return None
