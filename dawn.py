import sqlite3

# dawn.query_unnamed_items()
# dawn.add_item_prices()

# dawn.display()





def add_receipt():
    # Connect to the database
    conn = sqlite3.connect('receipt_database.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    
    # Create a cursor
    c = conn.cursor()
    
    # If the table doesn't already exist, create it
    c.execute("""CREATE TABLE IF NOT EXISTS receipts(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              store_name TEXT NOT NULL, 
              date TEXT NOT NULL,
              amount_spent REAL NOT NULL,
              taxes REAL NOT NULL,
              item_count INTEGER NOT NULL)
            """)
    
    c.execute("""CREATE TABLE IF NOT EXISTS items(
              store_number INTEGER PRIMARY KEY,
              store_code TEXT  NOT NULL UNIQUE, 
              description TEXT UNIQUE)
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS items_prices(
              receipt_id INTEGER NOT NULL, 
              item_id REAL NOT NULL,
              price REAL NOT NULL,
              FOREIGN KEY (receipt_id) REFERENCES receipts (id) ON DELETE CASCADE, 
              FOREIGN KEY (item_id) REFERENCES items (store_number) ON DELETE CASCADE,
              PRIMARY KEY (receipt_id, item_id)
              )
            """)#the knowledge and even this code on how to link tables I got from ChatGPT

    store_name = input("Store name: ").strip().upper() 
    date = input("Date of receipt (mm dd yyyy): ") 
    amount_spent = float(input("Amount spent: "))
    taxes = float(input("Taxes part of the total: ")) 
    item_count = int(input("Number of items bought: "))
    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.execute("INSERT INTO receipts (store_name, date, amount_spent, taxes, item_count) VALUES (?,?,?,?,?)", (store_name, date, amount_spent, taxes, item_count))
    receipt_id = c.lastrowid

    exit = ""
    item_list = []
    price_list = []
    while exit != "done":
        normal_desc = input("your description (hit enter if unknown): ")
        c.execute("SELECT store_code FROM items WHERE description = ?", (normal_desc,))
        current_item = c.fetchone()
        if current_item is None:
            store_desc = input("Store description: ").strip().upper()
            current_item = int(input("Store description number part: "))
        else:
            current_item = current_item[0]
        
        price = float(input("price of items bought: "))
        item_list.append((current_item, store_desc, normal_desc))  
        price_list.append((receipt_id, current_item, price))
        exit = input("Press Enter to add another item or type 'done' to finish: ").strip().lower()



    # Insert the item into the table (exclude id since it's auto-incrementing)
    c.executemany("INSERT OR IGNORE INTO items (store_number, store_code, description) VALUES (?,?,?)", item_list)
    c.executemany("INSERT INTO items_prices VALUES (?,?,?)", price_list)

    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()



def show_all():
    #connect to the data base
    conn = sqlite3.connect('receipt_database.db')
    #create a cursor
    c = conn.cursor()
    #selects the data and row ID from the table
    c.execute("SELECT rowid, * FROM receipts")
    # turns that data into a table
    items = c.fetchall()
    #prints the table row by row
    for item in items:
        print(item)
    #Commit's the command
    
    #closes our connection
    conn.close()
    

