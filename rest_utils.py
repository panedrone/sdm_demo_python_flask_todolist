from flask import jsonify

from dal.data_store import Base


def to_json_str(obj):
    if isinstance(obj, list):
        res = [o.__dict__ for o in obj]
        if len(res) > 0:
            if res[0].get('_sa_instance_state'):
                [r.pop('_sa_instance_state', None) for r in res]
    elif isinstance(obj, Base):
        # https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict
        res = dict(obj.__dict__)
        res.pop('_sa_instance_state', None)
    else:
        res = obj.__dict__
    return jsonify(res)