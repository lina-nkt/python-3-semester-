from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=False)
    birthDate = Column(Integer, nullable=False)
    occupation = Column(String, nullable=False)


Base.metadata.create_all(engine)


def insert_user():
    fullname = input("Введите ФИО пользователя: ")
    birthDate = int(input("Введите год рождения пользователя: "))
    occupation = input("Введите род деятельности пользователя: ")

    user = User(fullname=fullname, birthDate=birthDate, occupation=occupation)
    session.add(user)
    session.commit()


def display_users():
    users = session.query(User).all()
    if users:
        for user in users:
            print("ID:", user.id)
            print("ФИО:", user.fullname)
            print("Год рождения:", user.birthDate)
            print("Род деятельности:", user.occupation)
            print("-----------------------------------------")
    else:
        print("База данных пуста.")


def main():
    while True:
        choice = input("Выберите действие:\n1 - Добавить пользователя\n2 - Вывести содержимое базы данных\n3 - Выйти\n")

        match choice:
            case "1":
                insert_user()
            case "2":
                display_users()
            case "3":
                break
            case _:
                print("Некорректный выбор, попробуйте снова.")

main()