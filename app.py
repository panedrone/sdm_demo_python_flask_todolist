from flask import Flask, request, render_template
from flask_restful import Api, Resource

from rest_utils import to_json_str
from service import Service

app = Flask(__name__)
api = Api(app)


class GroupListResource(Resource):
    @staticmethod
    def get():
        res = Service().get_groups()
        return to_json_str(res)

    @staticmethod
    def post():
        service = Service()
        g_name = request.json["g_name"]
        service.create_group(g_name)


class GroupsResource(Resource):
    @staticmethod
    def get(g_id):
        res = Service().get_group(g_id)
        return to_json_str(res)

    @staticmethod
    def put(g_id):
        g_name = request.json["g_name"]
        Service().update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        Service().delete_group(g_id)


class TaskListResource(Resource):
    @staticmethod
    def get():
        g_id = request.args['g_id']
        res = Service().get_group_tasks(g_id)
        return to_json_str(res)

    @staticmethod
    def post():
        g_id = request.args['g_id']
        t_subject = request.json["t_subject"]
        Service().create_task(g_id, t_subject)


class TasksResource(Resource):
    @staticmethod
    def get(t_id):
        task = Service().get_task(t_id)
        return to_json_str(task)

    @staticmethod
    def put(t_id):
        service = Service()
        task = service.get_task(t_id)
        inp = request.json
        task.t_date = inp["t_date"]
        task.t_subject = inp["t_subject"]
        task.t_priority = inp["t_priority"]
        task.t_comments = inp["t_comments"]
        service.update_task(task)

    @staticmethod
    def delete(t_id):
        Service().delete_task(t_id)


api.add_resource(GroupListResource, "/groups")
api.add_resource(GroupsResource, "/groups/<g_id>")
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TasksResource, '/tasks/<t_id>')


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)
