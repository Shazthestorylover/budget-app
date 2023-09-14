'''
    Author: Shazzam Austin
    Course: Scientific Computing with Python
    Project: Budget App
    Website: FreeCodeCamp.org
    
    Date (Start): April 03, 2023
    Date (End): April 07, 2023
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

    # Grand total --> needed to calculate the percentage
    total = 0
    # Dictionary that has: key -> category, val -> total_withdrawl for the category 
    category_dict = {}
    
    for cat in categories:
        # total withdrawls for each category
        category_total = 0
        
        for item in cat.ledger:
            amount = item['amount']

            if amount < 0:
                total += abs(amount)
                category_total += abs(amount)

        category_dict[cat.category_name] = abs(category_total)

    category_dict = {
        key: (val/total) * 100
        for key, val in category_dict.items()
    }

    dash_width = len(category_dict) * 3 + 1
    spaces = dash_width - 1
    

    for i in range(100, 0, -10):
        bar_chart += f"{i:<3}| "
        bar_row = []
        row_val_count = 0

        #-------------------------issues start here-------------------
        for val in category_dict.values():
            row_val = [' '] * 3
            if val >= i:
                row_val[row_val_count] = "o"
                row_val_count += 1
                bar_row += row_val
        bar_chart += f"{''.join(bar_row)}{' ' * (spaces - len(bar_row))}\n"

    bar_chart += f"{' ' * 4}{'-' * dash_width}\n"
    #------------------------------------------------------------------
    
    category_names = [list(cat_name) for cat_name in category_dict]

    while any(category_names):
        bar_chart += f"{' ' * 4}"
        for cat_name in category_names:
            bar_chart += f" {' ' if not cat_name else cat_name.pop(0)} "
        bar_chart += " \n"
    
    # Used strip to remove the newline character for the last line and then add back the spaces.
    bar_chart = bar_chart.strip() + '  '
    #print("############################")
    #print(bar_chart)
    #print("############################")

    return bar_chart
    
    #return "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    
        

   
            
    
        
        