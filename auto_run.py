import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    def __init__(self, file_to_watch):
        self.file_to_watch = file_to_watch
        self.event_handler = Handler(file_to_watch)
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.event_handler, ".", recursive=False)
        self.observer.start()
        print(f"[INFO] Watching {self.file_to_watch} for changes...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
s setattr
class Handler(FileSystemEventHandler):
    def __init__(self, file_to_watch):
        self.file_to_watch = file_to_watch

    def on_modified(self, event):
        if event.src_path.endswith(self.file_to_watch):
            print(f"\n[INFO] Detected change in {self.file_to_watch}. Running...\n")
            subprocess.run(["python", self.file_to_watch])

if __name__ == "__main__":
    file_name = "empleyee_practice.py"  # apni main file ka naam
    w = Watcher(file_name)
    w.run()
