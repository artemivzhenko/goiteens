students = [['Andrii', 'Frankov'], ['Andrii'], ['Vasya', 'Gangster'], ["Andrii", 'Not'], ["Andrii", 'Groznyu'], ['Andrii']]
count = 0
for i in range(len(students)):
    for y in range(len(students[i])):
        if(students[i][y] == 'Andrii'):
            count += 1
        y += 1
    i += 1

print(f'Андріїв: {count}')