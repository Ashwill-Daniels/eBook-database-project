"""This program is used by a bookstore clerk. The program allows the 
 clerk to:
 - Add new books to the database.
 - Update book information.
 - Delete books from the database.
 - Search the database to find a specific book.
"""

# Import the SQLite3 module.
import sqlite3


# A class that holds methods that execute all required SQL statements.
class Sequel():

    def insert_book(self, id, title, author, quantity):
        """Insert a new book into the database table.""" 

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""INSERT INTO book (id, title, author, qty)
                                VALUES (?, ?, ?, ?)""", (id, title, 
                                                        author, quantity))
            
            print("Book added successfully.")

            # Save any changes.
            database.commit()

        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error
        
        finally:
            # Close the database.
            database.close()
    
    def update_book_title(self, new_title, title):
        """Update a book's title in the database table."""

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""UPDATE book SET title = ? WHERE title = ?""", 
                                (new_title, title))
            
            print("Book title updated successfully.")

            # Save any changes.
            database.commit()

        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error
        
        finally:
            # Close the database.
            database.close()

    def update_book_author(self, new_author, title):
        """Update a book's author in the database table."""

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""UPDATE book SET author = ? WHERE title = ?""", 
                                (new_author, title))
            
            print("Book author updated successfully.")
            
            # Save any changes.
            database.commit()

        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error
        
        finally:
            # Close the database.
            database.close()

    def update_book_quantity(self, new_qty, title):
        """Update a book's quantity in the database table."""

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""UPDATE book SET qty = ? WHERE title = ?""", 
                                (new_qty, title))
            
            print("Book quantity updated successfully.")
            
            # Save any changes.
            database.commit()

        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error
        
        finally:
            # Close the database.
            database.close()

    def delete_book(self, title):
        """Delete a book from the database table."""

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""DELETE FROM book WHERE title = ?""", (title, ))

            print("Book deleted successfully.")

            # Save any changes.
            database.commit()

        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error
        
        finally:
            # Close the database.
            database.close()

    def check_for_title(self):
        """Checks if a book title is in the database table."""

        while True:
            book_title = input("Please enter the book title: ")
            if book_title in book_title_list:
                break
            else:
                print("There is no record of such a title in the database.")

        return book_title

    def book_details(self, title):
        """Fetches book details from the database table."""

        try:
            # Connect to the database and create a database object.
            database = sqlite3.connect("ebookstore.db")

            # The cursor is used to execute SQL queries/statements.
            cursor = database.cursor()

            cursor.execute("""SELECT * FROM book WHERE title = ?""", (title, )) 
            book_info = cursor.fetchone()
            
            book_info = f"""ID:\t\t{book_info[0]}
Title:\t\t{book_info[1]}
Author:\t\t{book_info[2]}
Quantity:\t{book_info[3]}"""
            
            return book_info
        
        # Catch any database errors.
        except sqlite3.Error as error:
            # Roll back any changes.
            database.rollback()
            raise error

        finally:
            # Close the database.
            database.close()


# An instance of the Sequel class
sql_object = Sequel()
    
while True:

    try:
        # Connect to the database and create a database object.
        database = sqlite3.connect("ebookstore.db")

        # The cursor is used to execute SQL queries/statements.
        cursor = database.cursor()

        # Obtain the last record's id in the table.
        # Reference : https://www.geeksforgeeks.org/sql-select-last/
        cursor.execute("""SELECT id FROM book ORDER BY id DESC LIMIT 1""")
        last_book_ID = cursor.fetchone()

        # Data is returned as a tuple with one entry.
        last_book_ID = int(last_book_ID[0])

        # Create a list of all book titles within the database table.
        cursor.execute("""SELECT title FROM book""")
        book_title_tuples = cursor.fetchall()

        # Access 1st element from tuples in a list.
        # Reference: https://www.geeksforgeeks.org/python-accessing-nth-
        # element-from-tuples-in-list/
        book_title_list = [title[0] for title in book_title_tuples]

    # Catch any database errors.
    except sqlite3.Error as error:
        # Roll back any changes.
        database.rollback()
        raise error
    
    finally:
        # Close the database.
        database.close()

    user_input = input("""----------------EBOOKSTORE DATABASE----------------
Welcome to the ebookstore database.  
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
Enter a number to make a selection: """)
    
    # ----Add a book----
    if user_input == "1":
        # Prompt the user for the book information.    
        book_title = input("Please enter the book title: ")
        book_author = input("Please enter the book author: ")
        while True:

            try:
                book_quantity = int(input("How many copies of the book is \
there? "))
                if book_quantity > 0:
                    break
                else:
                    print("Please enter a number amount.")

            # Catch any Value errors.
            except ValueError:
                print("Please enter a number amount.")

        # Update the last book ID.
        last_book_ID += 1

        # Call the insert method.   
        sql_object.insert_book(last_book_ID, book_title, book_author, 
                               book_quantity)
        
    # ---Update a book---
    elif user_input == "2":
        # Verify that the book info exists in the database.
        book_title = sql_object.check_for_title()

        while True:
            
            try:
                update_choice = int(input("""Would you like to:
1. Update the title.
2. Update the author.
3. Update the quantity.
Please enter a number: """))
                # Check that the entered number is relevant.
                if update_choice > 0 and update_choice < 4:
                    break
                else:
                    print("Please enter a number between 1 and 3.")    

            # Catch any Value errors.                
            except ValueError:
                print("Please enter a number between 1 and 3.")

        # Call the appropriate update method based on the user's choice.
        if update_choice == 1:
            new_title = input("Please enter the new title:\n ")
            sql_object.update_book_title(new_title, book_title)

        elif update_choice == 2:
            new_author = input("Please enter the new author:\n ")
            sql_object.update_book_author(new_author, book_title)

        elif update_choice == 3:
            while True:

                try:
                    new_qty = int(input("Please enter the new quantity:\n "))
                    # Prevent negative numbers.
                    if new_qty > 0:
                        break
                    else:
                        print("Please enter an apropriate amount.")

                # Catch any Value errors.        
                except ValueError:
                    print("Please enter an apropriate amount.")

            sql_object.update_book_quantity(new_qty, book_title)
                
    # ---Delete a book---
    elif user_input == "3":
        # Verify that the book info exists in the database.
        book_title = sql_object.check_for_title()

        # Call the delete method.
        sql_object.delete_book(book_title)
    
    # ---Search for a book---
    elif user_input == "4":
        # Verify that the book info exists in the database.
        book_title = sql_object.check_for_title()

        # Call the book details method and print the result.
        print(sql_object.book_details(book_title))
    
    # ---Exit the program---
    elif user_input == "0":
        print("Thank you for using our service. Please come again.")

        # Exit the program.
        break

    # ---Incorrect input---
    else:
        print("Incorrect input. Please enter an appropriate number.")
    
