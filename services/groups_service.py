from dal.data_store import DataStore
from dal.group import Group
from dal.group_ex import GroupEx
from dal.groups_dao import GroupsDao
from dal.task import Task


class GroupsService:
    def __init__(self):
        # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread
        self.ds = DataStore()
        self.ds.open()

    def create_group(self, g_name):
        group = Group(g_name=g_name)
        self.ds.session.add(group)
        self.ds.commit()

    def delete_group(self, g_id):
        # https://stackoverflow.com/questions/26643727/python-sqlalchemy-deleting-with-the-session-object
        self.ds.session.query(Task).filter(Task.g_id == g_id).delete()
        self.ds.session.query(Group).filter(Group.g_id == g_id).delete()
        self.ds.commit()

    def update_group(self, g_id, g_name):
        # https://code-maven.com/slides/python/orm-update
        group = self.ds.session.query(Group).get(g_id)
        group.g_name = g_name
        self.ds.commit()

    def get_groups(self):
        # https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app
        # user = session.query(User).from_statement(
        #     text("""SELECT * FROM users where name=:name""")
        # ).params(name="ed").all()

        # query = self.ds.engine.execute(GroupExModel.SQL) # it returns an array of tuples
        # return query.all()

        # m: GroupEx = None

        return GroupsDao(self.ds).get_groups(GroupEx.SQL)

    def get_group(self, g_id):
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
        group = self.ds.session.query(Group).get(g_id)
        return group
