from datetime import datetime

from dal.data_store import DataStore
from dal.task import Task


class TasksService:
    def __init__(self):
        # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread
        self.ds = DataStore()
        self.ds.open()

    def get_group_tasks(self, g_id):
        tasks = self.ds.session.query(Task).filter(Task.g_id == g_id).order_by(Task.t_date, Task.t_id).all()
        return tasks

    def get_task(self, t_id):
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
        task = self.ds.session.query(Task).get(t_id)
        return task

    def create_task(self, g_id, t_subject):
        task = Task()
        task.g_id = g_id
        task.t_subject = t_subject
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        task.t_date = dt_string
        task.t_priority = 1
        task.t_comments = ''
        self.ds.session.add(task)
        self.ds.commit()
        return task

    def delete_task(self, t_id):
        # https://stackoverflow.com/questions/26643727/python-sqlalchemy-deleting-with-the-session-object
        self.ds.session.query(Task).filter(Task.t_id == t_id).delete()
        self.ds.commit()

    def update_task(self, task):
        self.ds.commit()
