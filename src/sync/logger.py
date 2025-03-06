import json
from datetime import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, action, details =''):
        log_entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'action': action,
            'details': details
        }
        print(json.dumps(log_entry, undent = 2))
        with open(self.log_path, "a") as file:
            file.write(json.dumps((log_entry)) + "\n")
