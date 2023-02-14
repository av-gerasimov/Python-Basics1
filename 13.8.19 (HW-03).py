amount_tickets = int(input('Введите количество билетов: '))
age_list = [int(input('Введите возраст посетителей: \n')) for i in range(amount_tickets)]
cost_tickets = 0
for i in age_list:
    if 1 < 18:
        cost_tickets += 0
    if 18 <= i <= 25:
        cost_tickets += 990
    if i > 25:
        cost_tickets += 1390
if amount_tickets > 3:
    print('Стоимость билетов:', cost_tickets * 0.9)
else:
    print('Стоимость билетов:', cost_tickets)
