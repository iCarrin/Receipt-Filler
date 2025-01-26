import sqlite3

# dawn.query_unnamed_items()
# dawn.add_item_prices()

# dawn.display()


def add_item(gibberish, real=" "):
    # Connect to the database
    conn = sqlite3.connect('receipt_database.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Create a cursor
    c = conn.cursor()
    
    # If the table doesn't already exist, create it
    c.execute("""CREATE TABLE IF NOT EXISTS items(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              store_code TEXT NOT NULL UNIQUE, 
              description TEXT)
            """)
    
    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.execute("INSERT INTO items (store_code, description) VALUES (?, ?)", (gibberish, real))
   
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()


def add_items():
    exit = ""
    list = []
    while exit != "done":
        store = input("store description: ")
        human = input("you're description: ")
        list.append((store, human))
        exit = input("type done to be done on hit enter to continue: ")

    
    
    
    #Connect to the database
    conn = sqlite3.connect('receipt_database.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Create a cursor
    c = conn.cursor()
    
    # If the table doesn't already exist, create it
    c.execute("""CREATE TABLE IF NOT EXISTS items(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              store_code TEXT NOT NULL UNIQUE, 
              description TEXT)
            """)
    
    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.executemany("INSERT INTO items (store_code, description) VALUES (?, ?)", list)
   
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()


def add_receipt(store, date, amount_spent, taxes, item_count):
    # Connect to the database
    conn = sqlite3.connect('receipt_database.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Create a cursor
    c = conn.cursor()
    
    # If the table doesn't already exist, create it
    c.execute("""CREATE TABLE IF NOT EXISTS receipts(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              store TEXT NOT NULL, 
              date TEXT NOT NULL,
              amount_spent INTEGER NOT NULL,
              taxes INTEGER NOT NULL,
              item_count INTEGER NOT NULL)
            """)
    
    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.execute("INSERT INTO items (store, date, amount_spent, taxes, item_count) VALUES (?,?,?,?,?)", (store, date, amount_spent, taxes, item_count))
   
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

#show all records
def show_all():
    #connect to the data base
    conn = sqlite3.connect('receipt_database.db')
    #create a cursor
    c = conn.cursor()
    #selects the data and row ID from the table
    c.execute("select rowid, * FROM receipt_database")
    # turns that data into a table
    items = c.fetchall()
    #prints the table row by row
    for item in items:
        print(item)
    #Commit's the command
    conn.commit()
    #closes our connection
    conn.close()

def add_item_price(receipt, item, price):
    conn = sqlite3.connect('receipt_database.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Create a cursor
    c = conn.cursor()
    
    # If the table doesn't already exist, create it
    c.execute("""CREATE TABLE IF NOT EXISTS items_prices(
              receipt_id INTEGER NOT NULL, 
              item_id INTEGER NOT NULL,
              price REAL NOT NULL,
              FOREIGN KEY (receipt_id) REFERENCES receipts (id) ON DELETE CASCADE, #the knowledge and even this code on how to link tables I got from ChatGPT
              FOREIGN KEY (item_id) REFERENCES items (id) ON DELETE CASCADE,
              PRIMARY KEY (receipt_id, item_id)
              )
            """)
    
    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.execute("INSERT INTO items_prices VALUES (?,?,?)", (receipt, item, price))
   
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
