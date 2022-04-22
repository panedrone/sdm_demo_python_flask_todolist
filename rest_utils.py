from flask import jsonify

from dal.data_store import Base


def to_json_str(obj):
    if isinstance(obj, list):
        if len(obj) > 0:
            if isinstance(obj[0], Base):
                res = [o.__dict__ for o in obj]
                [r.pop('_sa_instance_state', None) for r in res]
            else:
                res = obj
        else:
            res = obj
    elif isinstance(obj, Base):
        # https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict
        res = dict(obj.__dict__)
        res.pop('_sa_instance_state', None)
    else:
        if isinstance(obj, dict):
            res = obj
        else:
            res = obj.__dict__
    return jsonify(res)
