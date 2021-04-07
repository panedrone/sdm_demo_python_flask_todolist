from flask import Flask, request, render_template, redirect

from Service import Service

app = Flask(__name__)


@app.route("/")
def home():
    groups = Service().get_groups()
    return render_template("home.html", groups=groups, current_group=None, tasks=None, current_task=None)


@app.route("/group/create", methods=["POST"])
def group_create():
    service = Service()
    service.create_group(request.form["g_name"])
    return redirect("/")


@app.route("/group/update", methods=["POST"])
def group_update():
    service = Service()
    g_id = request.args["g_id"]
    g_name = request.form["g_name"]
    service.update_group(g_id, g_name)
    return redirect(f"/group/tasks?g_id={g_id}")


@app.route("/group/delete", methods=["GET"])
def group_delete():
    service = Service()
    g_id = request.args['g_id']
    service.delete_group(g_id)
    return redirect("/")


@app.route("/group/tasks", methods=["GET"])
def group_tasks():
    service = Service()
    groups = service.get_groups()
    g_id = request.args['g_id']
    tasks = service.get_group_tasks(g_id)
    current_group = service.get_group(g_id)
    return render_template("home.html", groups=groups, current_group=current_group, tasks=tasks, current_task=None)


@app.route("/task/create", methods=["POST"])
def task_create():
    service = Service()
    g_id = request.args['g_id']
    t_subject = request.form["t_subject"]
    task = service.create_task(g_id, t_subject)
    return redirect(f"/task/details?t_id={task.t_id}")


@app.route("/task/update", methods=["POST"])
def task_update():
    service = Service()
    t_id = request.args['t_id']
    task = service.get_task(t_id)
    task.t_date = request.form["t_date"]
    task.t_subject = request.form["t_subject"]
    task.t_priority = request.form["t_priority"]
    task.t_comments = request.form["t_comments"]
    service.update_task(task)
    return redirect(f"/task/details?t_id={t_id}")


@app.route("/task/details", methods=["GET"])
def task_details():
    service = Service()
    t_id = request.args['t_id']
    task = service.get_task(t_id)
    groups = service.get_groups()
    g_id = task.g_id
    tasks = service.get_group_tasks(g_id)
    current_group = service.get_group(g_id)
    return render_template("home.html", groups=groups, current_group=current_group, tasks=tasks, current_task=task)


@app.route("/task/delete", methods=["GET"])
def task_delete():
    service = Service()
    t_id = request.args['t_id']
    task = service.get_task(t_id)
    g_id = task.g_id
    service.delete_task(t_id)
    return redirect(f"/group/tasks?g_id={g_id}")


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)
