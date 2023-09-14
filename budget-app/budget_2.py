'''
    Author: Shazzam Austin
    Course: Scientific Computing with Python
    Project: Budget App
    Website: FreeCodeCamp.org
    
    Date (Start): April 03, 2023
    Date (End): April 11, 2023
'''

class Category:
    # Class attributes

    '''Constructor'''
    # Instance attributes
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __str__(self):
        budget_obj = f'{self.category_name:*^30}\n'
        sum = 0.0

        for item in self.ledger:
            budget_obj += f"{item['description'][0:23]:<23}" + f"{item['amount']:>7.2f}" +"\n"
            sum += item['amount']

        budget_obj += f"Total: {float(sum):.2f}"
        return budget_obj
        
        
    '''Methods'''

    # The method should append an object to the ledger list 
    # in the form of {"amount": amount, "description": description}.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Note: amount --> MUST be stored in ledger as a negative number.
    # If there are not enough funds, nothing should be added to the ledger. 
    # This method should return "True" if the withdrawal took place, and "False" otherwise.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
        else:
            return False

    # Outputs the current balance of the budget category based on the 
    # deposits and withdrawals that have occurred.
    def get_balance(self):
        total_balance = 0

        for obj in self.ledger:
            total_balance += obj["amount"]

        return total_balance

        
    # The method should add a withdrawal with the amount and the description 
    # "Transfer to [Destination Budget Category]".
    #
    # method should then add a deposit to the other budget category with the amount 
    # and the description "Transfer from [Source Budget Category]".
    #
    #  If there are not enough funds, nothing should be added to either ledgers. 
    # This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination_category.category_name}')
            destination_category.deposit(amount, f'Transfer from {self.category_name}')
            return True
        else:
            return False

    # accepts an amount as an argument. 
    # It returns False if the amount is greater than the 
    # balance of the budget category and returns True otherwise.
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

#########################################################################################################################

# Used to show the percentage spent in each category passed in to the function.

def create_spend_chart(categories):
    bar_chart = "Percentage spent by category\n"
    
    total = 0
    cat_dict = {}
    for cat in categories:
        category_total = 0
        for item in cat.ledger:
          amount = item["amount"]
          if amount < 0:
            total += abs(amount)
            category_total += abs(amount)
    
        cat_dict[cat.category_name] = category_total
    
    cat_dict = {
        k: (v / total) * 100
        for k, v in cat_dict.items()
    }
    
    dash_width = len(cat_dict) * 3 + 1
    spaces = dash_width - 1
    for n in range(100, -1, -10):
        bar_chart += f"{n:>3}| "
        bar_row = []
        for val in cat_dict.values():
          row_val = [' '] * 3
          if val >= n:
            row_val[0] = "o"
          bar_row += row_val
        bar_chart += f"{''.join(bar_row)}{' ' * (spaces - len(bar_row))}\n"
        
    bar_chart += f"{' ' * 4}{'-' * dash_width}\n"
    
    category_names = [list(name) for name in cat_dict]
    while any(category_names):
        bar_chart += f"{' ' * 4}"
        for name in category_names:
          bar_chart += f" {' ' if not name else name.pop(0)} "
        bar_chart += " \n"
   # Used strip to remove the newline character for the last line and then add back the spaces.
    bar_chart = bar_chart.strip() + '  '
    
    return bar_chart

        

   
            
    
        
        