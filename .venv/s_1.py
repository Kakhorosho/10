with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    formated_text = f_1.read().upper()
    print(formated_text, file=f_2)
