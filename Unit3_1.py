boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = sorted(boys)
girls = sorted(girls)
if len(boys) == len(girls):
    print("Пары")
    couples = list(zip(boys, girls))
    for man, woman in couples:
        print(f'{man} - {woman}')
else:
    print("Кто то останется без пары")