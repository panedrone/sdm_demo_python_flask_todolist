from datetime import datetime

from dal.data_store import DataStore
from dal.task import Task
from dal.tasks_dao import TasksDao


class TasksService:
    def __init__(self):
        # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread
        self.ds = DataStore()
        self.ds.open()

    def get_group_tasks(self, g_id):
        return TasksDao(self.ds).get_group_tasks(g_id)

    def get_task(self, t_id):
        task = Task()
        TasksDao(self.ds).read_task(t_id, task)
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
        TasksDao(self.ds).create_task(task)
        self.ds.commit()
        return task

    def delete_task(self, t_id):
        TasksDao(self.ds).delete_task(t_id)
        self.ds.commit()

    def update_task(self, task):
        TasksDao(self.ds).update_task(task)
        self.ds.commit()
