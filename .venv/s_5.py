with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    try:
        a = int(f_1.readline())
        b = int(f_1.readline(2))
        c = int(f_1.readline(3))
        print(a+b+c, file=f_2)
    except ValueError:
        print('data error', file=f_2)
    except ZeroDivisionError:
        print('division by 0', file=f_2)
