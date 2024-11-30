import sqlite3
from os import system, name
from datetime import datetime

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

db = sqlite3.connect('notes.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS NOTES(ID INTEGER PRIMARY KEY, TITLE TEXT, NOTE TEXT, DATE TEXT)')

def add():
    clear()
    
    title = input('Title: ')
    note = input('Note: ')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f"INSERT INTO NOTES VALUES(NULL, '{title}', '{note}', '{date}')")
    db.commit()
    main()
    
def update():
    clear()
    
    idx = int(input('Enter note ID to update: '))
    cursor.execute(f"SELECT * FROM NOTES WHERE ID = {idx}")
    data = cursor.fetchall()
    if data:
        print(f"Current Title: {data[0][1]}\nCurrent Note: {data[0][2]}")
        title = input('New Title: ')
        note = input('New Note: ')
        cursor.execute(f"UPDATE NOTES SET TITLE = '{title}', NOTE = '{note}' WHERE ID = {idx}")
        db.commit()
        print('Note updated!')
    else:
        print('No note found with this ID.')
    
    input('\nPress ENTER key.')
    main()
    
def show_all():
    clear()
    
    notes = cursor.execute('SELECT * FROM NOTES')
    if notes:
        for note in notes:
            print(f"ID: {note[0]}\nTitle: {note[1]}\nNote: {note[2]}\nAdded date: {note[3]}\n\n---------------------------------------------------------------------\n")
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
        print(f"ID: {data[0][0]}\nTitle: {data[0][1]}\nNote: {data[0][2]}\nAdded date: {data[0][3]}")
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
    
def search():
    clear()
    
    keyword = input("Enter keyword to search: ")
    cursor.execute(f"SELECT * FROM NOTES WHERE TITLE LIKE '%{keyword}%' OR NOTE LIKE '{keyword}'")
    results = cursor.fetchall()
    if results:
        for note in results:
            print(f"ID: {note[0]}\nTitle: {note[1]}\nNote: {note[2]}\nAdded date: {note[3]}")
    else:
        print("No notes foind!")
    
    input('\nPress ENTER key.')
    main()
    
def main():
    clear()
    
    print('1. Add note.\n2. Update note.\n3. Show all notes.\n4. View note.\n5. Delete note.\n6. Search note\n7. Exit.\n')

    while True:
        num = input('Enter your choice: ')
        
        if not num:
            print('Invalid input! Please enter a number between 1 and 7.')
            continue
        
        num = int(num)

        if num == 1:
            add()
        elif num == 2:
            update()
        elif num == 3:
            show_all()
        elif num == 4:
            view()  
        elif num == 5:
            delete()
        elif num == 6:
            search()
        elif num == 7:
            db.close()
            exit()
        else:
            main()
        
if __name__ == '__main__':
    main()
