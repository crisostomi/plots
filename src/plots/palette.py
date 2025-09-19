import json


class Palette:

    def __init__(self, path):

        with open(path, "r") as f:
            self.colors = json.load(f)
