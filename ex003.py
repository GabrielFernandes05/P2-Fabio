def fibos(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibos(n - 1) + fibos(n - 2)

def Numero():
    while True:
        try:
            n = int(input("Digite um número para ver seu correspondente na sequência de Fibonacci: "))
            return n
        except ValueError:
            print("Digite um númeo valido!")

def Continuar():
    while True:
        op = input("Deseja continuar? [S/N]").upper()
        match op:
            case 'S':
                return True
            case 'N':
                return False
            case _:
                print("Invalido!")

def Main():
    while True:
        n = Numero()
        print(f"O número correspondente é {fibos(n)}")
        continuar = Continuar()
        if continuar == False:
            print("Fim do programa!")
            break

Main()