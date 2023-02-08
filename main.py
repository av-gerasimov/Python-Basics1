money = float(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())
new_list = [i * money for i in per_cent_list]
deposit = list(map(int, new_list))
print("deposit - ", deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))