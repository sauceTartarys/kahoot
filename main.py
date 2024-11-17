from DBManager import DBManager

db_manager = DBManager("kahoot.db")
db_manager.create_tables()

"""db_manager.add_quiz(2,
                    "Квіз про Логіка",
                    "деякя інфа")"""
print(db_manager.get_quizzes())

db_manager.add_question(1,1,"Коли в Україні незалежність")
print(db_manager.get_questions())
db_manager.add_question(1,1,"few")