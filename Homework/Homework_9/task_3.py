# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
purchase = 0
purchases_list = []
with open('test_file/task_3.txt', 'r', encoding="utf-8") as f:
    for i in f.readlines():
        if i != '\n':
            purchase += int(i)
        else:
            purchases_list.append(purchase)
            purchase = 0
purchases_list.sort(reverse=True)
three_most_expensive_purchases = sum(purchases_list[:3])
assert three_most_expensive_purchases == 202346
