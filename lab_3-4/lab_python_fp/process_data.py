import json

from pathlib import Path

from field import field
from gen_random import gen_random
from unique import Unique
from cm_timer import cm_timer_1
from print_result import print_result

path = Path("lab_python_fp/data/data_light.json")

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding="utf-8") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(data):
    return list(Unique(field(data, "job-name"), ignore_case=True))


@print_result
def f2(data):
    return list(filter(lambda data_el: data_el.lower().startswith("программист"), data))


@print_result
def f3(data):
    return list(map(lambda data_el: f"{data_el} с опытом Python", data))


@print_result
def f4(data):
    return list(map(lambda x: f"{x[0]}, зарплата {x[1]} руб", zip(data, gen_random(len(data), 100000, 200000))))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
