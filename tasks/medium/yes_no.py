"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1: list):
    new_list = set(list_1)
    if len(new_list) == len(list_1):
        print("Yes")
    else:
        print("No")


yes_or_no([1, 2, 3, 2, 5, 3, 2, 1])
