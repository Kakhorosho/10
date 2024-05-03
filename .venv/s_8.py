with open('input.txt', 'r+') as f_1, open('output.txt', 'w') as f_2:
    count = 0
    month = []
    months = []
    av_number = [0]*12
    for line in f_1:
        count += 1
        if count <= 31:
            a = line
            av_number[0] += int(a[:-1])
        if 31 < count <= 59:
            a = line
            av_number[1] += int(a[:-1])
        if count > 59:
            for i in range(3, len(av_number)+1):
                if i % 2 != 0:
                    b = 59 + 31*(i-3) - 1
                    c = b + 31
                    if b < count <= c:
                        a = line
                        if a[:-1] == '\n':
                            number = a[:-1]
                            av_number[i-1] += int(number)
                        else:
                            av_number[i - 1] += int(a)
                if i % 2 == 0:
                    b = 59 + 31 * (i - 4) + 1
                    c = b + 31
                    if b < count <= c:
                        a = line
                        if a[:-1] == '\n':
                            number = a[:-1]
                            av_number[i - 1] += int(number)
                        else:
                            av_number[i - 1] += int(a)
    print(av_number)
    for i in range(len(av_number)):
        if i == 1:
            av_number[i-1] //= 31
        elif i == 2:
            av_number[i-1] //= 28
        else:
            if i % 2 != 0:
                av_number[i-1] //= 31
            else:
                av_number[i-1] //= 30
    for i in range(len(av_number)):
        print(av_number[i-1], file=f_2)