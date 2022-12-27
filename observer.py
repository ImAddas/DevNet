

class BusniessCustomer:

    def __init__(self, acct_id, money_owed):

        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self):

        if self.money_owed > 0:
            print(f"{self.acct_id}: Call the company's finance department")
        else:
            print(f"{self.acct_id}: Corporate balance piad")


class ConsumerCustomer:

    def __init__(self, acct_id, money_owed):

        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self):

        if self.money_owed > 0:
            print(f"{self.acct_id}: Send a polite reminder email")
        else:
            print(f"{self.acct_id}: Individual balance paid")

class AccountingSystem:

    def __init__(self):

        self.customers = set()

    def register(self,customer):

        self.customers.add(customer)

    def unregister(self, customer):

        self.customers.remove(customer)

    def notify(self):

        for customer in self.customers:
            customer.update()

        
def main():

    cust1 = BusniessCustomer("ACCT100", 10)
    cust2 = BusniessCustomer("ACCT200", 0)
    cust3 = ConsumerCustomer("ACCT300", -10)
    cust4 = ConsumerCustomer("ACCT400", 20)


    accouting_sys = AccountingSystem()
    accouting_sys.register(cust1)
    accouting_sys.register(cust2)
    accouting_sys.register(cust3)
    accouting_sys.register(cust4)


    accouting_sys.notify()

    print("** cust2 has cancelled their account")
    accouting_sys.unregister(cust2)

    accouting_sys.notify()


if __name__ == "__main__":
    main()