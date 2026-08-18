import sqlite3

class Student:
    def __init__(self, student_id, name, course):
        self.id = student_id
        self.name = name
        self.course = course

class StudentModel:
    def __init__(self, db_name='students.db'):
        self.db_name = db_name
        self._create_table()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    course TEXT NOT NULL
                )
            ''')
            conn.commit()

    def get_all_students(self):
        students = []
        with self._get_connection() as conn:
            cursor = conn.execute('SELECT id, name, course FROM students')
            for row in cursor.fetchall():
                students.append(Student(row['id'], row['name'], row['course']))
        return students

    def add_student(self, name, course):
        with self._get_connection() as conn:
            cursor = conn.execute(
                'INSERT INTO students (name, course) VALUES (?, ?)',
                (name, course)
            )
            conn.commit()
            return Student(cursor.lastrowid, name, course)

db = StudentModel()
