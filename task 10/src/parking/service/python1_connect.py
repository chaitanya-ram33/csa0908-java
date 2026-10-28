import sqlite3
con = sqlite3.connect("collage.db")
print("database connected successfully")
con.close()