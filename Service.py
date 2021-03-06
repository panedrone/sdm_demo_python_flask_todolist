from datetime import datetime

from dal.data_store import DataStore
from dal.group import Group
from dal.groups_dao import GroupsDao
from dal.task import Task
from dal.tasks_dao import TasksDao


class Service:
    def __init__(self):
        self.ds = DataStore()
        self.ds.open()

    def create_group(self, g_name):
        group = Group()
        group.g_name = g_name
        group.tasks_count = 0
        GroupsDao(self.ds).create_group(group)
        self.ds.commit()

    def delete_group(self, g_id):
        TasksDao(self.ds).delete_group_tasks(g_id)
        GroupsDao(self.ds).delete_group(g_id)
        self.ds.commit()

    def update_group(self, g_id, g_name):
        dao = GroupsDao(self.ds)
        group = Group()
        dao.read_group(g_id, group)
        group.g_name = g_name
        dao.update_group(group)
        self.ds.commit()

    def get_groups(self):
        return GroupsDao(self.ds).get_groups()

    def get_group(self, g_id):
        group = Group()
        GroupsDao(self.ds).read_group(g_id, group)
        return group

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

