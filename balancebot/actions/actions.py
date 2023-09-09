from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

people = {
    "123456789": {
        "name": "John Doe",
        "phone_number": "555-555-5555",
        "balance": 2155.00,
        "transaction_history": [
            {"date": "2023-09-08", "description": "Initial deposit", "amount": 1000.00},
            {"date": "2023-09-10", "description": "Coffee shop", "amount": -5.50},
            {"date": "2023-09-12", "description": "Groceries", "amount": -40.00},
            {"date": "2023-09-15", "description": "Paycheck", "amount": 1200.00}
        ]
    },
    "987654321": {
        "name": "Jane Doe",
        "phone_number": "555-555-5556",
        "balance": 3425.00,
        "transaction_history": [
            {"date": "2023-09-08", "description": "Initial deposit", "amount": 1500.00},
            {"date": "2023-09-10", "description": "Restaurant", "amount": -30.00},
            {"date": "2023-09-13", "description": "Gas station", "amount": -45.00},
            {"date": "2023-09-18", "description": "Salary", "amount": 2000.00}
        ]
    },
    "135792468": {
        "name": "Bob Smith",
        "phone_number": "555-555-5557",
        "balance": 980.00,
        "transaction_history": [
            {"date": "2023-09-09", "description": "Initial deposit", "amount": 800.00},
            {"date": "2023-09-11", "description": "Bookstore", "amount": -20.00},
            {"date": "2023-09-14", "description": "Electronics store", "amount": -100.00},
            {"date": "2023-09-16", "description": "Freelance work", "amount": 300.00}
        ]
    },
    "864209731": {
        "name": "Mary Johnson",
        "phone_number": "555-555-5558",
        "balance": 2395.00,
        "transaction_history": [
            {"date": "2023-09-10", "description": "Initial deposit", "amount": 2000.00},
            {"date": "2023-09-12", "description": "Clothing store", "amount": -80.00},
            {"date": "2023-09-14", "description": "Pharmacy", "amount": -25.00},
            {"date": "2023-09-20", "description": "Bonus", "amount": 500.00}
        ]
    }
}







class ActionVerifyInfo(Action):
    def name(self):
        return "action_verify_info"

    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")
        phone_number = tracker.get_slot("phone_number")

        if account_number in people and people[account_number]["phone_number"] == phone_number:
            user_name = people[account_number]["name"]
            dispatcher.utter_message(template="utter_greet_user", name=user_name)
        else:
            dispatcher.utter_message("Sorry, I couldn't verify your information. Please try again.")

class ActionCheckBalance(Action):
    def name(self):
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")
        phone_number = tracker.get_slot("phone_number")

        if account_number in people and people[account_number]["phone_number"] == phone_number:
            balance = people[account_number]["balance"]
            user_name = people[account_number]["name"]
            dispatcher.utter_message(f"Dear {user_name} your {account_number} has balance of ${balance:.2f}")
        else:
            dispatcher.utter_message("Sorry, I couldn't find your account. Please provide valid information.")

class ActionTransactionHistory(Action):
    def name(self):
        return "action_transaction_history"

    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")

        if account_number in people:
            transactions = people[account_number]["transaction_history"]
            history_message = "Here are your recent transactions:\n"
            for transaction in transactions:
                history_message += f"Date: {transaction['date']}, Description: {transaction['description']}, Amount: ${transaction['amount']:.2f}\n"
            dispatcher.utter_message(history_message)
        else:
            dispatcher.utter_message("Sorry, I couldn't find your account. Please provide valid information.")
