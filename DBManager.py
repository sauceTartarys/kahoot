import sqlite3


class DBManager:
        def __init__(self, db_name):
            self.connection = sqlite3.connect(db_name)


        def create_tables(self):
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Options (
                Oprion_id INT PRIMARY KEY,
                Question_id int,
                Content TEXT
                IS_CORRECT BOOLEAN
                );
                
                CREATE TABLE "Options" (
                    "Oprion_id"	INT,
                    "Question_id"	int,
                    "Content"	TEXT IS_CORRECT BOOLEAN,
                    PRIMARY KEY("Oprion_id")
                    );
                CREATE TABLE "Question" (
                    "Question_id"	INT,
                    "Quiz_title"	int,
                    "Content"	TEXT,
                    PRIMARY KEY("Question_id")
                    );
                CREATE TABLE "Quiz" (
                    "id"	INT,
                    "title"	VARCHAR(255),
                    "description"	TEXT,
                    PRIMARY KEY("id")
                
                
                );
                """)
            self.connection.commit()