import json


def load_json(path_to_json: str):
    with open(path_to_json, "r", encoding="utf-8") as f:
        resp = json.load(f)
    return resp
