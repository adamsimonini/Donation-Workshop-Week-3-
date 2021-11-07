def show_homepage():
  print("\n        === DonateMe Homepage ===          ")
  print("---------------------------------------------")
  print("| 1.    Login       | 2.    Register         |")
  print("---------------------------------------------")
  print("| 3.    Donate      | 4.    Show Donations  |")
  print("---------------------------------------------")
  print("|                 5.   Exit                  |")
  print("---------------------------------------------")


def donate(username):
  amt_to_donate = input("Enter amount to donate: ")
  amt_to_donate = float(amt_to_donate)

  donation = {
    "name": username,
    "amount": amt_to_donate
  }
  print(f"Thank you for your donation of ${amt_to_donate}!")
  return donation
  

def show_donations(donations):
  total_donations = 0
  if len(donations) == 0:
    print("Sad face! No donations!")
  print("\n--- All Donations ---")
  for donation in donations:
    # need to parse donations, since it's a string (bad data design)
    # total_donations += float(donation)
    print(f"{donation['name']} donated ${donation['amount']}")
    total_donations += float(donation["amount"])
  print(f"\nTotal donations: ${total_donations}")

def exit_program():
  print("Program ending. Goodbye!")
  exit()