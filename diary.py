from replit import db
import os, time, datetime, random

def add_entry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("Type an entry: ")
  db[timestamp] = entry


def view_entries():
  keys = db.keys()
  keys = list(keys)[::-1]
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key} {db[key]}""")
    print()
    more = input("Do you want to view next entry or exit to main menu?\n> ")
    if more[0].lower() == 'e':
      break

keys = db.keys()
if len(keys) < 1:
  print("First time? Create an account")
  name = input("Username: ")
  password = input("Password: ")
  salt = random.randint(0, 9999)
  newPassword = hash(f"{password}{salt}")
  db[name] = {
    "password": newPassword,
    "salt": salt
  }
else:
  print("Log in")
  name = input("Username: ")
  password = input("Password: ")
  if name not in keys:
    print("Incorrect username or password")
    exit()
  salt = db[name]["salt"]
  newPassword = hash(f"{password}{salt}")
  if db[name]["password"] != newPassword:
    print("Incorrect username or password")
    exit()

while True:
  os.system("clear")
  menu = int(input("1.Add an entry\n2.View entries\n> "))
  if menu == 1:
    add_entry()
  else:
    view_entries()
