import sqlite3

db = sqlite3.connect('ebookstore_db')

cursor = db.cursor() # Get a cursor object

cursor.execute('''DROP TABLE IF EXISTS books''')

cursor.execute( '''
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT,
author Text, Qty integer)
''' )
db.commit()

cursor.execute( '''INSERT INTO books(id, title, author, Qty)
VALUES(3001,'A Tale of Two Cities', 'Charles Dickens', 30)''')

cursor.execute( '''INSERT INTO books(id, title, author, Qty)
VALUES(3002,'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40)''')

cursor.execute( '''INSERT INTO books(id, title, author, Qty)
VALUES(3003,'The Lion, the Witch and theWardrobe', 'C. S. Lewis', 25)''')

cursor.execute( '''INSERT INTO books(id, title, author, Qty)
VALUES(3004,'The Lord of the Rings', 'J.R.R Tolkien', 37)''')

cursor.execute( '''INSERT INTO books(id, title, author, Qty)
VALUES(3005,'Alice in Wonderland', 'Lewis Carroll', 12)''')

title = ""
author = ""
Quantity = 0

print("Book Store Menu")
UserChoice = int(input("1. Enter Book" + "\n" +
					"2. Update Book" + "\n" +
					"3. Delete Book" + "\n" +
					"4. Search Books" + "\n" +
					"0. Exit "  + "\n" +
					"user choice: "))

if UserChoice == 1:
	title = input("Enter the Title of the book : ")
	author = input("Enter the author of the book : ")
	Quantity = input("Enter the Quantity of the book(s) : ")

	cursor.execute( '''INSERT INTO books(id, title, author, Qty)
	VALUES(?, ?, ?, ?)''', id+1, title, author, Quantity)
	print("Book Inserted.")
elif UserChoice == 2:
	Book_title = input("Which book do you want to update? ")
	updates = input("what do you wanna update? title, Author, or Quantity")

	if updates == "title":
		new_title = input("What is the new title of the book ?")
		cursor.execute('''
		UPDATE books 
		SET title = ? 
		WHERE title = ?
		''', new_title, updates)
	elif updates == "Author":
		new_author = input("What is that name of the new author ? ")
		cursor.execute('''
		UPDATE books 
		SET author = ? 
		WHERE title = ?
		''', new_author, updates)
	elif updates == "Quantity":
		new_QTY = input("What is the new quantity of the books? ")
		cursor.execute('''
		UPDATE books 
		SET Qty = ? 
		WHERE title = ?
		''', new_QTY, updates)
	print("Book Updated")
elif UserChoice== 3:
	title = input("Enter the Title of the book you want to Delete : ")
	cursor.execute( '''DELETE FROM books WHERE title = ?''',title)
	print("Book Deleted.")
elif UserChoice == 4:
	title = input("Enter the Title of the book you want to Search for : ")
	cursor.execute('''SELECT * FROM books WHERE title = ?''',title)
	S_books = cursor.fetchall()
	print("Search results : " + S_books)
elif UserChoice == 0:
	exit()