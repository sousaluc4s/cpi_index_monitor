# core/tracker.py
import json
import os

class Tracker:
    def __init__(self, file):
        self.file = file

    def load(self):
        if not os.path.exists(self.file):
            return set()
        with open(self.file) as f:
            return set(json.load(f))

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(list(data), f, indent=2)