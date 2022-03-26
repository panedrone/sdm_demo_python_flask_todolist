from dal.data_store import DataStore
from dal.group import Group
from dal.groups_dao import GroupsDao
from dal.tasks_dao import TasksDao


class GroupsService:
    def __init__(self):
        # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread
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
