with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    count = 0
    for lines in f_1:
        count += 1
        if count % 2 == 0:
            print(lines, end='', file=f_2)
