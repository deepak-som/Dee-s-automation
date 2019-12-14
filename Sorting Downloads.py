from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
  i =1
  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      src = folder_to_track + "/" + filename
      new_desination = folder_destination + "/" + filename
      os.rename(src, new_desination)

        
folder_to_track = r"C:\Users\Dee!\Downloads\to_track"
folder_destination = r"C:\Users\Dee!\Sorted_downloads"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
 while True:
  time.sleep(10)

except KeyboardInterrupt:
 observer.stop()

observer.join()



