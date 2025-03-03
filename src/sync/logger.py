import os
from datetime import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, message):
        timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(self.log_path, "a") as file:
            file.write(log_message + "\n")
