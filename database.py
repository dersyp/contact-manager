import sqlite3
from sqlite3 import Error
from repository import ContactGroupRepository
from models import session
from models.group_priority import GroupPriority

group_list = ["Family", "Professional", "Friends ", "Emergency contact"]
class DatabaseManager:

    def __init__(self, db_file):
        """ create a database connection to a SQLite database """
        self.connexion = None
        try:
            self.connexion = sqlite3.connect(db_file, check_same_thread=False)
        except Error as e:
            print(e)

    def create_database(self):
        try:
            cur = self.connexion.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS contact (
                                            contact_id integer primary key,
                                            name text NOT NULL,
                                            surname text NOT NULL,
                                            mail text NOT NULL,
                                            phone_number text NOT NULL,
                                            group_id integer NOT NULL,
                                            address text NOT NULL,
                                            priority real
                                        ); """)
            cur.execute(""" CREATE TABLE IF NOT EXISTS contact_group (
                                                                    group_id integer primary key,
                                                                    group_name text NOT NULL,
                                                                    group_priority real,
                                                                    UNIQUE(group_name)
                                                                ); """)
        except Error as e:
            print(e)

    def initialize_database(self):
        for group_name in group_list:
            contact_group_repo = ContactGroupRepository(session=session)
            contact_group_repo.add_contact_group(GroupPriority(group_name=group_name, group_priority=0.05))

