class Customers:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance}.'

    def get_customer(self):
        return f'{self.first_name} {self.last_name}. {self.city}.'


costomer_1 = Customers('Иван','Петров','Москва', 100)
costomer_2 = Customers('Петр','Иванов','Ярославль', 200)
costomer_3 = Customers('Jacques','Dubois','Paris', 300)

customer_list = [costomer_1, costomer_2, costomer_3]
for customer in customer_list:
    print(customer.get_customer())