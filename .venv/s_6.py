with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    try:
        a = int(f_1.readline())
        length = len(f_1.readlines())
        print(a, length)
        if a == length:
            print('yes', file=f_2)
        else:
            print('no', file=f_2)
    except ValueError:
        print('error', file=f_2)