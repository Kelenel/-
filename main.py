def name():
    print('Вбей уменьшительную форму своего имени из 4 букв, типа Вася, Даня, Миша и т.д.')
    global namae
    namae = input()
    if len(namae) != 4:
        print ("Ты дебил? Сказано же, 4 буквы!")
        name()
def po():
    print("Теперь вбей первую согласную своей фамилии и первую гласную после неё")
    global pso
    pso = input()
    if len(pso) != 2:
        print("Две буквы, ДВЕ БЛЯТЬ, первая согласная твоей фамилии и первая гласная после неё!")
        po()
name()
po()
x = namae[0]
z = namae[1]
y = namae[2]
t = namae[3]
print(x.upper()+z.lower()+y.lower()+t.lower(),x.upper()+t.lower()+pso.lower()+y.lower()+z.lower())
input("Enter чтобы выйти")