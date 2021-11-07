from donations_pkg.homepage import *
from donations_pkg.user import *

# setting up initial state
database = {
  "admin" : "password123",
}

donations = []
authorized_user = ""

# checking if user is authorized
if authorized_user == "":
  print("You must be logged in to donate.")
else:
  print("Logged in as:", authorized_user)


while True:
  show_homepage()
  user_choice = input("\nChoose a number from the menu above: ")
  
  if user_choice == "1":
    print('one')
    authorized_user = login(database)

  elif user_choice == "2":

    # if there is a new user, update the database and set current user to that user's name
    newDatabase = register(database)
    if newDatabase:
      database = newDatabase
      authorized_user = list(database)[-1]

  elif user_choice == "3":
    if authorized_user == "":
      print("You're not logged in. Please log in to donate! It's free!\n")
      continue
    donations.append(donate(authorized_user))

  elif user_choice == "4":
    show_donations(donations)

  elif user_choice == "5":
    exit_program()
  else:
    print("Invalid input. Please select a number from the menu.")