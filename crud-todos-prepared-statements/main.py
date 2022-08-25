# pip install mysql-connector-python
from mysql import connector
from config import config
from commands import *
from helperfns.tables import tabulate_data

conn = connector.connect(**config)
cursor = conn.cursor()
cursor.execute(CREATE_TABLE_COMMAND)

columns = ["id", "title", "completed"]


def insert():
    title = input("Enter the todo title: ").strip()
    cursor.execute(INSERT_COMMAND, (title,))
    conn.commit()


def delete():
    try:
        id = int(input("Enter the todo id: ").strip())
        cursor.execute(DELETE_COMMAND, {id})
        conn.commit()
    except:
        print(f"There's no todo of id: {id}")


def update():
    try:
        id = int(input("Enter the todo id: ").strip())
        cursor.execute(UPDATE_COMMAND, (True, id))
        conn.commit()
    except:
        print(f"There's no todo of id: {id}")


def get(all=False):
    if all:
        cursor.execute(ALL_TODOS_COMMAND)
        rows = [(i, t, bool(c)) for (i, t, c) in cursor]
        if len(rows) > 0:
            tabulate_data(columns, rows, title="ALL TODOS")
        else:
            print("There are no todos in the table.")
    else:
        id = int(input("Enter the todo id: ").strip())
        cursor.execute(SINGLE_TODO_COMMAND, [id])
        try:
            rows = [(i, t, bool(c)) for (i, t, c) in cursor]
            tabulate_data(columns, rows, title="TODO OF ID: {}".format(id))
        except:
            print(f"There's no todo of id: {id}")


if __name__ == "__main__":
    while True:
        choice = int(input("Choice 1. add 2. delete 3. update 4. get one 5. get all 0. exit:\n"))
        if choice == 0:
            break
        elif choice == 1:
            insert()
        elif choice == 2:
            delete()
        elif choice == 3:
            update()
        elif choice == 4:
            get()
        elif choice == 5:
            get(all=True)
        else:
            continue
    # close connection
    conn.close()
