#//+------------------------------------------------------------------+
#//|                               VerysVeryInc.POSforFreee.XLS_S3.py |
#//|                  Copyright(c) 2018, VerysVery Inc. & Yoshio.Mr24 |
#//|                      https://github.com/MatsuoStation/Freee.POS/ |
#//|                                                 Since:2018.02.24 |
#//|                                Released under the Apache license |
#//|                       https://opensource.org/licenses/Apache-2.0 |
#//|        "VsV.POSforFreee.XLS_S3.py - Ver.0.0.2 Update:2018.02.25" |
#//+------------------------------------------------------------------+
#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Python3 : Setup ###
import time
import os

### Path : Setup ###
# from pathlib import Path

### Watchdog : Setup ###
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


### BaseDir : Setup ###
BASEDIR = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, os.pardir, 'ScanData/ScanXLS')
# BASEDIR = Path(__file__).parent
# BASEDIR /= '../ScanXLS'
# BASEDIR00 = os.path.abspath(os.path.dirname(__file__))
# BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


### GetText ###
def getext(filename):
    return os.path.splitext(filename)[-1].lower()

### ChangeHandler ###
class ChangeHandler(FileSystemEventHandler):

    ### * Created
    def on_created(self, event):
        if event.is_directory:
            return

        # if getext(event.src_path) in ('.jpg','.png','.txt'):
        if getext(event.src_path) in ('.xlsx'):
            print('%s has been created.' % event.src_path)

    ### * Deleted
    def on_deleted(self, event):
        if event.is_directory:
            return

        # if getext(event.src_path) in ('.jpg','.png','.txt'):
        if getext(event.src_path) in ('.xlsx'):
            print('%s has been deleted.' % event.src_path)

    ### * Modify
    """
    def on_modified(self, event):
        if event.is_directory:
            return

        # if getext(event.src_path) in ('.jpg','.png','.txt'):
        if getext(event.src_path) in ('.xlsx'):

            print('%s has been modified.' % event.src_path)
    """


### Main ###
if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler,BASEDIR,recursive=True)

        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()     # (Mac) Ctrl+z / (Win) Ctrl+Break
        observer.join()

#+------------------------------------------------------------------+