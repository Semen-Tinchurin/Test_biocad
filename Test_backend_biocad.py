import json


def open_file():
    with open('test.json', 'r', encoding='utf-8') as file:
        file = json.load(file)
    return file


def pretty_print(file):
    number_of_columns = 0
    max_columns = []
    for key, column in file.items():
        len_el = [len(key)]
        [len_el.append(len(str(el))) for el in column]
        max_columns.append(max(len_el))

    for list_of_values in list(file.values()):
        if len(list_of_values) > number_of_columns:
            number_of_columns = len(list_of_values)

    # print title of table
    tablehead = list(file.keys())
    for n, head in enumerate(tablehead):
        print(f"{head:^{max_columns[n] + 1}}|", end='')
    print()
    print(f"{'=' * sum(max_columns) + '=' * 2 * len(tablehead)}")

    # print table body
    row = 0
    while row < number_of_columns:
        for num, list_of_values in enumerate(list(file.values())):
            try:
                str_to_print = f"{list_of_values[row]:>{max_columns[num]}} |"
                print(str_to_print, end='')
            except IndexError:
                str_to_print = " " * (max_columns[num] + 1) + "|"
                print(str_to_print, end='')
        row += 1
        print()
    print(f"{'-' * sum(max_columns) + '-' * 2 * len(tablehead)}")


pretty_print(open_file())


def fibonachi(N):
    fib1 = 0
    fib2 = 1
    counter = 0
    while counter <= N:
        print(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        counter += 1


fibonachi(N=11)
