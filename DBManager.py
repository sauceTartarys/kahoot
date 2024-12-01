import sqlite3


class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
           CREATE TABLE IF NOT EXISTS Quiz (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT
        )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Questions (
            id INT PRIMARY KEY,
            quiz_id INT,
            content TEXT
        );

         """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Options (
            id INT PRIMARY KEY,
            question_id INT,
            content TEXT,
            is_correct BOOLEAN
        );
            """)
        self.connection.commit()


    def add_quiz(self, id, title, description):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Quiz(id, title, description) VALUES (?, ?, ?)",
                       [id, title, description])
        self.connection.commit()
        cursor.close()
    def add_question(self,id, quiz_id,content):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Quiz(id, quiz_id, content) VALUES (?, ?, ?)",
                       [id,quiz_id,content ])
        self.connection.commit()
        cursor.close()
    def get_quizzes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Quiz")
        res = cursor.fetchall()
        cursor.close()
        return res
    def get_questions(self, quiz_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from Questions WHERE quiz_id = ?",[quiz_id])
        res = cursor.fetchall()
        self.connection.commit()
        return res
    def get_options(self, Question_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from Options WHERE Question_id = ?",[Question_id])
        res = cursor.fetchall()
        cursor.close()
        return res