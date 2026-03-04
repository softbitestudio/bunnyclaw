import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if "Ask-Bunny.txt" in event.src_path:
            try:
                with open(event.src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if "BunnyClaw will read it" not in content:
                    print("🐰 BunnyClaw processing...")
                    result = subprocess.check_output(
                        ["picoclaw", "agent", "-m", content.split("BunnyClaw will read it")[0].strip()],
                        env={**os.environ, "PICOCLAW_HOME": os.getcwd(), "PICOCLAW_CONFIG": "portable-config.json"},
                        timeout=180
                    ).decode()
                    with open(event.src_path, 'a', encoding='utf-8') as f:
                        f.write(f"\n\n=== BUNNYCLAW ANSWER ===\n{result}")
            except:
                pass

observer = Observer()
observer.schedule(Handler(), path=".", recursive=False)
observer.start()
print("🐰 BunnyClaw waiting patiently — edit Ask-Bunny.txt and save!")
try:
    while True:
        time.sleep(1)
except:
    observer.stop()
observer.join()
