Liste = [
    ("Ahmet", "Yılmaz", "25"),
    ("Ayşe", "Demir", "30"),
    ("Mehmet", "Kaya", "28"),
    ("Elif", "Çelik", "22"),
    ("Can", "Aydın", "35"),
    ("Zeynep", "Şahin", "27"),
    ("Burak", "Koç", "32"),
    ("Selin", "Arslan", "24"),
    ("Emre", "Doğan", "29"),
    ("Gamze", "Aksoy", "26")
]

# for i in range(10):
#     for x in range(1):
    
#         name=input('Enter name :')
#         surname=input('Enter surname :')
#         age=input('Enter persons age :')
#         print('\n')

#         person= name,surname,age
#         Liste.append(person)

print('\n',Liste)

a=True

while a is True:
    wantedname=input('Enter the name you want to search (or press Enter to exit): ')
    wantedsurname=input('Enter the surname you want to search (or press Enter to exit): ')
    
    if wantedname == '' or wantedsurname == '':
        break
    
    check = False
    for person in Liste:
        if wantedname == person[0] and wantedsurname == person[1]:
            print('Person\'s age =', person[2])
            check = True
            break

    if not check:
        print('\nIncorrect input')

print('\nThanks')