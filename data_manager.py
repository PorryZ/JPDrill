import json
import random
from pathlib import Path

class DataManager:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)

    def load(self, filename):
        path = self.data_dir / filename
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def random_item(self, data):
        return random.choice(data)
