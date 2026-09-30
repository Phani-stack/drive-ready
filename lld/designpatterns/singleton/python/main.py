from database import Database

d1 = Database("url1", "")
d2 = Database()

print(d1 is d2)
