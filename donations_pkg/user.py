def login(database):
  username = input("Enter username: ").lower()
  password = input("Enter password: ")

  # handle username not found
  if not username in database.keys():
    print("Username not found. Register new user.")
  else:
    # handle password not found
    if not password == database[username]:
      print("Password is incorrect.")
      return ""
    else:
      print(f"Welcome back {username}")
      return username

def register(database):
  username = input("\nEnter username under 10 characters to register: ").lower()
  
  # username validation
  if username in database.keys():
    print("ERROR: this user already exists. Returning to main menu...")
    return False
  while len(username) > 10:
    username = input("ERROR: username must be under 10 characters. Please try again: ").lower()

  password = input("\nEnter a password over 5 characters long: ")
  # password validation
  while len(password) < 5:
      password = input("Error: password is too short. Please enter a password at least 5 characters long: ")

  database[username] = password
  print(f"New user {username} registered")
  return database
