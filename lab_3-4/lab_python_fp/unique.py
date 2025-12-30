# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.unique_items = []
        for item in items:
            compare_item = item
            if "ignore_case" in kwargs and isinstance(item, str):
                if kwargs["ignore_case"]:
                    compare_item = item.lower()
            if compare_item not in self.unique_items:
                self.unique_items.append(compare_item)
        self.current_index = 0

    def __next__(self):
        if self.current_index < len(self.unique_items):
            result = self.unique_items[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self

if __name__ == "__main__":
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
