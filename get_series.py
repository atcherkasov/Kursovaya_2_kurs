import numpy as np
from poly_functions import add, make_equlation, show
from parsers import parser


def equations_to_series(equations: list, n: int):
    x = [np.poly1d([1]), np.poly1d([0])]

    variable = {}
    f = add(x, [np.poly1d([0])])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [np.poly1d([0])]

    for i in range(1, n - 1):
        new_variable = {}
        for j in range(1, len(variable)):
            new_variable[j] = make_equlation(variable[equations[j - 1][1]],
                                             variable[equations[j - 1][2]],
                                             variable[equations[j - 1][3]],
                                             variable[equations[j - 1][4]])
        for j in range(1, len(variable)):
            variable[j] = new_variable[j]

        f = add(x, variable[1])
        variable[0] = f

    new_a = make_equlation(variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]])
    a = new_a
    f = add(x, a)
    cut_f = f[(-2 * i - 4):]
    return show(cut_f)


if __name__ == '__main__':
    import time
    start = time.time()
    groups = parser()
    # series = set()
    series = []


    for group in groups:
        length = len(series)
        current = equations_to_series(group[1:], 9)
        is_uniq = True
        for el in series:
            if el[1] == current:
                is_uniq = False
                print('>>>>>>>>>>>>>>>')
                print(el[0])
                print(group[0])
                print(current)
                print()
        if is_uniq:
            series.append((group[0], current))
print('ALL TIME:', time.time() - start)
