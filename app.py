import flask
import flask_restful

from rest_utils import to_json_str
from services.groups_service import GroupsService
from services.tasks_service import TasksService

app = flask.Flask(__name__)
api = flask_restful.Api(app)


class GroupListResource(flask_restful.Resource):
    @staticmethod
    def get():
        res = GroupsService().get_groups()
        return to_json_str(res)

    @staticmethod
    def post():
        service = GroupsService()
        g_name = flask.request.json["g_name"]
        service.create_group(g_name)


class GroupResource(flask_restful.Resource):
    @staticmethod
    def get(g_id):
        res = GroupsService().get_group(g_id)
        return to_json_str(res)

    @staticmethod
    def put(g_id):
        g_name = flask.request.json["g_name"]
        GroupsService().update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        GroupsService().delete_group(g_id)


class GroupTasksResource(flask_restful.Resource):
    @staticmethod
    def get(g_id):
        res = TasksService().get_group_tasks(g_id)
        return to_json_str(res)

    @staticmethod
    def post(g_id):
        t_subject = flask.request.json["t_subject"]
        TasksService().create_task(g_id, t_subject)


class TasksResource(flask_restful.Resource):
    @staticmethod
    def get(t_id):
        task = TasksService().get_task(t_id)
        return to_json_str(task)

    @staticmethod
    def put(t_id):
        service = TasksService()
        task = service.get_task(t_id)
        inp = flask.request.json
        task.t_date = inp["t_date"]
        task.t_subject = inp["t_subject"]
        task.t_priority = inp["t_priority"]
        task.t_comments = inp["t_comments"]
        service.update_task(task)

    @staticmethod
    def delete(t_id):
        TasksService().delete_task(t_id)


api.add_resource(GroupListResource, "/groups")
api.add_resource(GroupResource, "/group/<g_id>")
api.add_resource(GroupTasksResource, '/group/<g_id>/tasks')
api.add_resource(TasksResource, '/tasks/<t_id>')


@app.route("/")
def home():
    return flask.render_template("index.html")


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)
