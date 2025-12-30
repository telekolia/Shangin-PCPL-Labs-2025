# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0

    result = []
    for item in items:
        dict = {}
        for arg in args:
            if arg in item:
                dict[arg] = item[arg]

        if len(args) == 1:
            result.append(dict[args[0]])
        else:
            result.append(dict)

    return result

if __name__ == "__main__":
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print("Первое задание:\n")
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
    print("\nКонец первого задания\n")
