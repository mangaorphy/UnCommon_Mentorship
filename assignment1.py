# Function to calculate tax
def calculate_tax(income):
    if income < 1000:
        tax = 0
    elif income <= 5000:
        tax = income * 0.10
    else:
        tax = income * 0.20
    return tax


# Class representing a Citizen
class Citizen:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def get_tax_amount(self):
        return calculate_tax(self.income)

    def display_info(self):
        tax_due = self.get_tax_amount()
        print("\n--- Tax Information ---")
        print(f"Citizen: {self.name}")
        print(f"Income: ${self.income}")
        print(f"Tax Due: ${tax_due}")
        print("-----------------------")


# Main part that runs when the file is executed
def main():
    print("Welcome to the Revenue Tax Calculator 💰")

    # Ask user for input
    name = input("Enter your name: ")
    
    # Loop until a valid income is entered
    while True:
        try:
            income = float(input("Enter your income: "))
            if income < 0:
                print("Income cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for income.")

    # Create a Citizen object and display their tax info
    citizen = Citizen(name, income)
    citizen.display_info()


# This ensures main() runs only when the file is executed directly
if __name__ == "__main__":
    main()
