class Budget:

    def __init__(self, income):
        self.income = income
        self.payments = {}

    def change_income(self, new_income):
        self.income = new_income

    def add_payment(self, name, amount, start_period, end_period):
        self.payments[name] = {'amount': amount, 'start_period': start_period, 'end_period': end_period}

    def remove_payment(self, name):
        if name in self.payments:
            del self.payments[name]

    def calculate_savings_for_item(self, item_cost, save_period):
        return item_cost / save_period

    def show_payments(self):
        for name, details in self.payments.items():
            print(f"Payment: {name}, Amount: {details['amount']}, Start period: {details['start_period']}, End period: {details['end_period']}")

    def calculate_total_payments(self):
        total = 0
        for details in self.payments.values():
            total += details['amount']
        return total

    def calculate_remaining_income(self):
        return self.income - self.calculate_total_payments()


if __name__ == "__main__":
    my_budget = Budget(5000)
    my_budget.add_payment("Rent", 1000, "2023-07-01", "2023-07-31")
    my_budget.add_payment("Utilities", 200, "2023-07-01", "2023-07-31")

    my_budget.show_payments()

    print("Total payments:", my_budget.calculate_total_payments())
    print("Remaining income:", my_budget.calculate_remaining_income())

    item_cost = 600
    save_period = 6  # Save for the item in 6 months
    print(f"Need to save {my_budget.calculate_savings_for_item(item_cost, save_period)} per month for your item.")

    my_budget.change_income(6000)  # Increase income
    print("New income:", my_budget.income)
    print("Remaining income after income adjustment:", my_budget.calculate_remaining_income())
