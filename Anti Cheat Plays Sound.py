import os
import time
import glob
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from playsound import playsound

# Paste the path to your logs folder.
LOGS_FOLDER = " "
SOUND_FILE = "MGS.mp3"
# Paste the path to your sound file. I'm using Metal Gear Solid's alert sound as a default.

def get_latest_log():
    log_files = glob.glob(os.path.join(LOGS_FOLDER, "*.log"))
    if not log_files:
        return None
    return max(log_files, key=os.path.getmtime)

class LogFileHandler(FileSystemEventHandler):

    def __init__(self, log_file):
        self.log_file = log_file
        self.last_position = os.path.getsize(log_file)

    def on_modified(self, event):
        if event.src_path == self.log_file:
            with open(self.log_file, "r", encoding="utf-8") as file:
                file.seek(self.last_position)
                new_lines = file.readlines()
                self.last_position = file.tell()

            for line in new_lines:
                #Type, in between quotations, words that are used in alerts from your Anti-Cheat, this example is from the Vulcan AC.
                if "VULCAN »" in line and "failed" in line:
                    print(f"FUCKING CHEATER KILL HIM {line.strip()}")
                    playsound(SOUND_FILE)

def monitor_log():
    latest_log = get_latest_log()
    if not latest_log:
        print("No log files found.")
        return

    print(f"Monitoring: {latest_log}")
    event_handler = LogFileHandler(latest_log)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(latest_log), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_log()
