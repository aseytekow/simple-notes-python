import sqlite3
from os import system, name

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

db = sqlite3.connect('notes.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS NOTES(ID INTEGER PRIMARY KEY, TITLE TEXT, NOTE TEXT)')

def add():
    clear()
    
    title = input('Title: ')
    note = input('Note: ')
    cursor.execute(f"INSERT INTO NOTES VALUES(NULL, '{title}', '{note}')")
    db.commit()
    main()
    
def show_all():
    clear()
    
    notes = cursor.execute('SELECT * FROM NOTES')
    if notes:
        for note in notes:
            print(f"ID: {note[0]}\nTitle: {note[1]}\nNote: {note[2]}\n\n---------------------------------------------------------------------\n")
    else:
        print('No note!')
        
    input('\nPress ENTER key.')
    main()

def view():
    clear()
    
    idx = int(input('Enter note ID: '))
    cursor.execute(f"SELECT * FROM NOTES WHERE ID = {idx}")
    data = cursor.fetchall()
    if data:
        print(f"ID: {data[0][0]}\nTitle: {data[0][1]}\nNote: {data[0][2]}")
    else:
        print('No note in this ID.')
    
    input('\nPress ENTER key.')
    main()

def delete():
    clear()
    
    idx = int(input('Enter note ID: '))
    cursor.execute(f"DELETE FROM NOTES WHERE ID = {idx}")
    print('Note deleted!')
    
    input('\nPress ENTER key.')
    main()
    
def main():
    clear()
    
    print('1. Add note.\n2. Show all notes.\n3. View note.\n4. Delete note.\n5. Exit.\n')

    num = int(input('Enter your choice: '))

    if num == 1:
        add()
    elif num == 2:
        show_all()
    elif num == 3:
        view()
    elif num == 4:
        delete()
    elif num == 5:
        db.close()
        exit()
    else:
        main()
        
if __name__ == '__main__':
    main()