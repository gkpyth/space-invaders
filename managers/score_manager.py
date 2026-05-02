import json
import os
from settings import SCORE_FILE

class ScoreManager:
    def __init__(self):
        self.high_score = self._load()


    def _load(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                return json.load(f)["high_score"]
        return 0


    def save(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(SCORE_FILE, "w") as f:
                json.dump({"high_score": self.high_score}, f)
