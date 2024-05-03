with open('input.txt', 'r') as f_1, open('output.txt', 'w') as f_2:
    count = 0
    locks = []
    number_of_locks = []
    counter = 0
    for line in f_1:
        count += 1
        if count == 1:
            a = line
            print(a[:-1])
        elif count == 2:
            b = line
            print(b[:-1])
        else:
            locks.append(line.split()[0])
            number_of_locks.append(line.split()[1])
    part_1 = int(a.split('.')[0])
    part_2 = int(a.split('.')[1])
    for _ in number_of_locks:
        part_3 = int(_.split('.')[0])
        part_4 = int(_.split('.')[1])
        if part_2 == part_4:
            if part_1 - part_3 > 3:
                counter += 1
        elif part_2 - part_4 == 1:
            if part_2 ==2 or part_4 == 2:
                if part_2 ==2:
                    number_1 = 31- part_3 +part_1
                    if number_1 >=4:
                        counter+=1
                else:
                    number_2 =28 -part_3 +part_1
                    if number_2 >= 4:
                        counter += 1
            else:
                number_3 = 31 -part_3+part_1
                if number_3>=4:
                    counter+=1
                
        elif part_2 - part_4 > 1:
            counter +=1


    print(counter, file=f_2)
    print(locks)
    print(number_of_locks)

