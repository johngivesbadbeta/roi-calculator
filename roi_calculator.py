class roiCalculator():

    # Input monthly income
    def monthlyIncome(self):
        self.rental = int(input('How much are you charging monthly for rent? $'))
        if self.rental < 0:
            print("Invalid. Must be 0 or more.")
            self.rental()
        self.laundry = int(input('How much are you charging monthly for laundry? $'))
        if self.laundry < 0:
            print("Invalid. Must be 0 or more.")
            self.laundry()
        self.storage = int(input('How much are you charging monthly for storage? $'))
        if self.storage < 0:
            print("Invalid. Must be 0 or more.")
            self.storage()
        self.misc = int(input('How much are you charging monthly for misc. items? $'))
        if self.misc < 0:
            print("Invalid. Must be 0 or more.")
            self.misc()
        self.monthly_income = self.rental + self.laundry + self.misc
        print(f'Your monthly income is: ${self.monthly_income}')
        self.totalExpenses()
        
    # Input monthly expenses
    def totalExpenses(self):
        self.taxes = int(input('How much are you paying monthly in taxes? $'))
        if self.taxes < 0:
            print("Invalid. Must be 0 or more.")
            self.taxes()
        self.insurance = int(input('How much are you paying monthly for insurance? $'))
        if self.insurance < 0:
            print("Invalid. Must be 0 or more.")
            self.insurance()
        self.utilities = int(input('How much are you paying monthly for utilities? $'))
        if self.utilities < 0:
            print("Invalid. Must be 0 or more.")
            self.utilities()
        self.hoa = int(input('How much are you paying monthly to the HOA? $'))
        if self.hoa < 0:
            print("Invalid. Must be 0 or more.")
            self.hoa()
        self.landscape = int(input('How much are you paying monthly for landscaping? $'))
        if self.landscape < 0:
            print('Invalid. Must be 0 or more.')
            self.landscape()
        self.vacancy = int(input('How much are you paying monthly for vacancy? $'))
        if self.vacancy < 0:
            print('Invalid. Must be 0 or more.')
            self.vacancy()
        self.repairs = int(input('How much are you paying monthly for repairs? $'))
        if self.repairs < 0:
            print('Invalid. Must be 0 or more.')
            self.repairs()
        self.capex = int(input('How much is your monthy CapEx? $'))
        if self.capex < 0:
            print('Invalid. Must be 0 or more.')
            self.capex()
        self.mortgage = int(input('How much is your monthly mortgage? $'))
        if self.mortgage < 0:
            print('Invalid. Must be 0 or more.')
            self.mortgage()
        self.property_management = int(input('How much do you pay monthly for property management? $'))
        if self.property_management < 0:
            print('Invalid. Must be 0 or more.')
            self.property_management()
        self.monthly_expenses = self.taxes + self.insurance + self.utilities + self.hoa + self.landscape + self.vacancy + self.repairs + self.capex + self.mortgage + self.property_management
        print(f'Your expenses total ${self.monthly_expenses} per month.')
        self.calcCashFlow()

    # Calculate cash flow
    def calcCashFlow(self):
        self.cash_flow = self.monthly_income - self.monthly_expenses
        print(f'Your cash flow is ${self.cash_flow} per month.')
        self.cashOnCash()

    # cash on cash ROI
    def cashOnCash(self):
        self.down_payment = int(input('How much was your down payment on your property? $'))
        if self.down_payment < 0:
            print('Invalid. Must be 0 or more.')
            self.down_payment()
        self.closing_cost = int(input('What was your closing cost for your property? $'))
        if self.closing_cost < 0:
            print('Invalid. Must be 0 or more.')
            self.closing_cost()
        self.rehab_budget = int(input('What was your rehab budget? $'))
        if self.rehab_budget < 0:
            print('Invalid. Must be 0 or more.')
            self.rehab_budget()
        self.misc_cost = int(input('How much did you pay for any misc. cost? $'))
        if self.misc_cost < 0:
            print('Invalid. Must be 0 or more.')
            self.misc_cost()
        self.total_investment = self.down_payment + self.closing_cost + self.rehab_budget + self.misc_cost
        self.annual_cashflow = self.cash_flow * 12
        self.roi = (self.annual_cashflow / self.total_investment) * 100
        print(f'Based on your total investment of ${self.total_investment} and annual cash flow of ${self.annual_cashflow}, your ROI is {self.roi}%.')
        
incomeAndExpenses = roiCalculator()

def calculateROI():
    while True:
        response = input("Woud you like to calculate your ROI? yes/no ")
        if response.lower() == 'yes':
            incomeAndExpenses.monthlyIncome()
        if response.lower() == 'no':
            print("Thank you. Goodbye.")
            break
        
calculateROI()