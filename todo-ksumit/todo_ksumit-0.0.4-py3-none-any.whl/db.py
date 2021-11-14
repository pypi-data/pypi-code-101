import sqlite3
import os

from .helper import cursor_to_dict_list, nextRecurDate

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.expanduser('~') + '/todo.db')
        self.cursor = self.connection.cursor()

    def createTable(self):
        try:
            self.cursor.execute("DROP TABLE tasks")
        except:
            pass
        self.cursor.execute("""CREATE TABLE tasks (
                title TEXT NOT NULL,
                date TEXT,
                time TEXT,
                recur TEXT,
                project TEXT,
                is_completed BOOL
            )""")

    def createTask(self, task):
        self.cursor.execute("INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?)", task.to_db_tuple())

    def deleteTask(self, id):
        res = self.cursor.execute(f"""
            DELETE FROM tasks where rowid = {id}
        """).rowcount
        return res

    def getTasks(self, date, project=None, completed=False, sort='time'):
        if project:
            query = f"""SELECT rowid, * from tasks WHERE project = '{project}' AND date <= '{date}' AND is_completed = '{int(completed)}' ORDER BY {sort} """
        else:
            query = f"""SELECT rowid, * from tasks WHERE date <= '{date}' AND is_completed = '{int(completed)}' ORDER BY {sort} """

        self.cursor.execute(query)
        return cursor_to_dict_list(self.cursor)
    
    def getAllTasks(self, find="", completed=False, sort='date'):
        query = f"""SELECT rowid, * 
                        from tasks 
                    where is_completed = '{int(completed)}'
                    AND (
                        title LIKE '%{find}%'
                        OR date LIKE '%{find}%'
                        OR time LIKE '%{find}%'
                        OR recur LIKE '%{find}%'
                        OR project LIKE '%{find}%'
                    )
                    order by {sort}
                """
        self.cursor.execute(query)
        return cursor_to_dict_list(self.cursor)
    
    def updateTask(self, id, title=None, project=None, date=None, time=None, recur=None):
        items = []
        if title: items.append(f"title = '{title}'")
        if project: items.append(f"project = '{project}'")
        if date: items.append(f"date = '{date}'")
        if time: items.append(f"time = '{time}'")
        if recur is not None: items.append(f"recur = '{recur}'")
        if len(items) == 0: return
        self.cursor.execute(f"UPDATE tasks SET {', '.join(items)} where rowid = '{id}'")

    def getTask(self, id):
        res = self.cursor.execute(f"""
            SELECT rowid, * from tasks where rowid = {id}
        """).fetchone()
        if not res: return res
        cols = [col[0] for col in self.cursor.description]
        return dict(zip(cols, res))
        

    def completeTask(self, id):
        task = self.getTask(id)
        if task:
            if task['recur']:
                new_date = nextRecurDate(task['date'], task['recur'])
                query = f"update tasks set date = '{new_date}' where rowid = '{id}'"
            else:
                query = f"update tasks set is_completed = {not task['is_completed']} where rowid = '{id}'"
            self.cursor.execute(query)

    def __del__ (self):
        self.connection.commit()
        self.connection.close()
