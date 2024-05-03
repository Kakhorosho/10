with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    for line in f_1:
        if line == '100\n':
            pass
        else:
            print(line, file=f_2, end='')