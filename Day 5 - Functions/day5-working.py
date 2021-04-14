items1 = ["Mic", "Mouse", 550, "KeyBoard", 420, "USB", 299.55]
items2 = ["Mike", 25.235, "James", "Wade", 445]

def parseList(items_list):
    str_items = []
    num_items = []

    for i in items_list:
        if isinstance(i, int) or isinstance(i, float):
            num_items.append(i)
        elif isinstance(i, str):
            str_items.append(i)
        else:
            pass
    return str_items, num_items

print(parseList(items1))  
print(parseList(items2))


def calculate_sum(items_list):
    total = 0
    for i in items_list:
        if isinstance(i, int) or isinstance(i, float):
            total += i
            pass
    return total

print(calculate_sum(items1))  
print(calculate_sum(items2))    