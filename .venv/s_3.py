with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    for lines in f_1:
        letter = lines[0]
        print(letter, file=f_2, end='')