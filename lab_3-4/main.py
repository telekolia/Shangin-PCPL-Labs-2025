from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print("Первое задание:\n")
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
    print("\nКонец первого задания\n")

    print("Второе задание:\n")
    print(gen_random(5, 1, 10))
    print("\nКонец второго задания\n")

    print("Третье задание:\n")
    not_uniq_mass = [4, 18, 4, 8, 1, 18, "AAA", "bobo", "aa", "Bobo", "aaA", "aaa"]

    un_iterator = Unique(not_uniq_mass)
    low_un_iterator = Unique(not_uniq_mass, ignore_case=True)

    print("ignore_case = False/Not Stated\n")

    for i in range (len(un_iterator.unique_items)):
        print(un_iterator.__next__())

    print("\nignore_case = True\n")

    for i in range (len(low_un_iterator.unique_items)):
        print(low_un_iterator.__next__())

    print("\nКонец третьего задания\n")

    print("Четвёртое задание:\n")
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

    print("\nКонец четвёртого задания\n")

if __name__ == "__main__":
    main()
