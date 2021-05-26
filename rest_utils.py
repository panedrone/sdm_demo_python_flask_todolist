from flask import jsonify


def to_json_str(obj):
    if isinstance(obj, list):
        res = [o.__dict__ for o in obj]
    else:
        res = obj.__dict__
    return jsonify(res)