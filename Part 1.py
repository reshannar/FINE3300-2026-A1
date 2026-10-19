import csv

dates = []

#Used this website to figure out the below code: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
with open("BankOfCanadaExchangeRate.2026.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        dates.append(row[0])

#displays options and uses the row numbers so the cell amounts for the exchange rates can be called later
for i, dates in enumerate(dates, start=1):
    print(i, dates)

    i = i + 1
#to increase row number to print all options 

row_input = int(input("Choose a date from the list (Please use the left hand number, i.e. '3'): "))
#storing the row number to use the exchange rate from that specific date

#allows me to read all of the values in each column in any given row
with open("BankOfCanadaExchangeRate.2026.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

print("You selected:", row_input, ", therefore the rate is: ", rows[row_input][26])
    
#for i, row_number in enumerate(rows) -- one thing i tried, didn't work
    
#trying to get the row number entered in based on the user's choice
#if dates == dates.append(row[1]):

from_currency = str(input("Enter in the currency you are converting from (USD or CAD): "))
to_currency = str(input("Enter in the currency you are converting to (USD or CAD): "))

if from_currency =="USD":
    rate = float(rows[row_input][26])
    
else:
    rate = 1 / float(rows[row_input][26])

#print(rate) -- checking that the math works

amount = int(input("Enter the amount you would like to convert: "))

class ExchangeRate:
    def __init__(self, from_currency, to_currency, rate, amount):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate
        self.amount = amount
        
    def convert(self):
        converted_amount = self.amount * self.rate
        return converted_amount

#print("Using an exchange rate of ", rate, " which was taken from the exchange rate on ", rows[row_input][0], ", ", amount, " which was in ", from_currency, " equals approximately ", convert(), " in", to_currency)
#^didn't work because I was calling the convert function as its own function and not as defined in a class

exchange = ExchangeRate(from_currency, to_currency, rate, amount)

print(
    "Using an exchange rate of ", exchange.rate,
    " taken from ", rows[row_input][0],
    ", ", exchange.amount, " in ", exchange.from_currency,
    " equals approximately ", exchange.convert(),
    " in ", exchange.to_currency
)

