class Customers:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'


customer = Customers('Иван', 'Петров', 'Москва', 50)
print(customer)