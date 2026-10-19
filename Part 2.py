#Prompt: create a python program that reads a csv file titled "BankOfCanadaExchangeRate.2026.csv", finds the 
#exchange rate for a given date by the user, finds the USD to CAD conversion rate listed under 
#the column labeled “FXAUSDCAD”, prompts the user to enter which conversion they would like 
#to do, either USD to CAD or CAD to USD, prompts the user for the amount they would like to 
#convert, and alters the USD to CAD conversion rate given in the csv file depending on if the 
#user would like to convert from USD to CAD or from CAD to USD. Display the results of the 
#conversion. Be sure to use a class named “ExchangeRate” and a method named “Convert” 

#This was created using Claude.ai


import csv
from datetime import datetime, timedelta

CSV_FILE = "BankOfCanadaExchangeRate.2026.csv"
RATE_COLUMN = "FXAUSDCAD"            # column name requested
FALLBACK_COLUMNS = ("FXUSDCAD",)     # Bank of Canada's actual column name
DATE_COLUMN = "date"


class ExchangeRate:
    """Looks up a USD/CAD rate in a Bank of Canada CSV and converts amounts."""

    def __init__(self, csv_path=CSV_FILE):
        self.csv_path = csv_path
        self.rates = {}          # {date string "YYYY-MM-DD": USD->CAD rate}
        self.rate = None         # USD -> CAD rate for the selected date
        self.rate_date = None    # the date the rate actually came from
        self._load()

    def _load(self):
        """Read the CSV into a dictionary of date -> USD-to-CAD rate."""
        with open(self.csv_path, newline="", encoding="utf-8-sig") as f:
            lines = f.readlines()

        # Bank of Canada files may have metadata lines above the header row,
        # so find the row that starts with the date column.
        header_index = next(
            (i for i, line in enumerate(lines)
             if line.strip().lower().startswith(DATE_COLUMN)),
            None,
        )
        if header_index is None:
            raise ValueError(f"Could not find a '{DATE_COLUMN}' header row in the CSV.")

        reader = csv.DictReader(lines[header_index:])
        fields = [name.strip() for name in reader.fieldnames]

        rate_col = next(
            (c for c in (RATE_COLUMN, *FALLBACK_COLUMNS) if c in fields), None
        )
        if rate_col is None:
            raise ValueError(f"Column '{RATE_COLUMN}' was not found in the CSV.")

        for row in reader:
            row = {k.strip(): (v or "").strip() for k, v in row.items() if k}
            date, value = row.get(DATE_COLUMN, ""), row.get(rate_col, "")
            if date and value:
                try:
                    self.rates[date] = float(value)
                except ValueError:
                    continue  # skip blank/non-numeric entries

    def get_rate(self, date_str, look_back_days=7):
        """Set and return the USD->CAD rate for a date (YYYY-MM-DD).

        If the date has no rate (weekend/holiday), uses the most recent
        earlier date within look_back_days. Returns None if nothing is found.
        """
        date = datetime.strptime(date_str, "%Y-%m-%d")
        for offset in range(look_back_days + 1):
            candidate = (date - timedelta(days=offset)).strftime("%Y-%m-%d")
            if candidate in self.rates:
                self.rate = self.rates[candidate]
                self.rate_date = candidate
                return self.rate
        self.rate = self.rate_date = None
        return None

    def Convert(self, amount, direction):
        """Convert an amount using the selected date's rate.

        direction: "USD to CAD" -> amount * rate
                   "CAD to USD" -> amount / rate (rate is inverted)
        """
        if self.rate is None:
            raise ValueError("No exchange rate selected. Call get_rate() first.")

        if direction == "USD to CAD":
            return amount * self.rate
        if direction == "CAD to USD":
            return amount / self.rate
        raise ValueError("Direction must be 'USD to CAD' or 'CAD to USD'.")


def prompt_date():
    while True:
        text = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def prompt_direction():
    while True:
        print("\nWhich conversion would you like to do?")
        print("  1) USD to CAD")
        print("  2) CAD to USD")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            return "USD to CAD"
        if choice == "2":
            return "CAD to USD"
        print("Please enter 1 or 2.")


def prompt_amount(currency):
    while True:
        text = input(f"Enter the amount in {currency} to convert: ").strip().replace(",", "")
        try:
            amount = float(text)
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def main():
    try:
        converter = ExchangeRate(CSV_FILE)
    except FileNotFoundError:
        print(f"Error: could not find '{CSV_FILE}'. Place it in the same folder as this script.")
        return
    except ValueError as e:
        print(f"Error reading CSV: {e}")
        return

    # Find the rate for the user's date
    while True:
        date_str = prompt_date()
        rate = converter.get_rate(date_str)
        if rate is not None:
            break
        print(f"No exchange rate found for {date_str}. Try another date.")

    if converter.rate_date != date_str:
        print(f"No rate published for {date_str} (weekend/holiday). "
              f"Using the most recent rate from {converter.rate_date}.")
    print(f"\nUSD to CAD rate on {converter.rate_date}: {rate:.4f}")

    direction = prompt_direction()
    from_cur, to_cur = direction.split(" to ")
    amount = prompt_amount(from_cur)

    result = converter.Convert(amount, direction)

    print("\n--- Result ---")
    print(f"Date used:       {converter.rate_date}")
    if direction == "USD to CAD":
        print(f"Rate applied:    1 USD = {rate:.4f} CAD")
    else:
        print(f"Rate applied:    1 CAD = {1 / rate:.4f} USD (inverse of {rate:.4f})")
    print(f"{amount:,.2f} {from_cur} = {result:,.2f} {to_cur}")


if __name__ == "__main__":
    main()