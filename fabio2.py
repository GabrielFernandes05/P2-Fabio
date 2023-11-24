def ponto1():
    x = 0
    y = 0
    for i in range(1, 3):
        while True:
            try:
                if i == 1:
                    x = float(input("Qual o 'x' do primeiro ponto: "))
                    break
                elif i == 2:
                    y = float(input("Qual o 'y' do primeiro ponto: "))
                    break
            except ValueError:
                print("Digite números validos!")
    return x, y


def ponto2():
    x = 0
    y = 0
    for i in range(1, 3):
        while True:
            try:
                if i == 1:
                    x = float(input("Qual o 'x' do segundo ponto: "))
                    break
                elif i == 2:
                    y = float(input("Qual o 'y' do segundo ponto: "))
                    break
            except ValueError:
                print("Digite números validos!")
    return x, y


def ver_distância():
    while True:
        print("Deseja ver o valor exato da distância? [S/N]")
        op = input("----> ").upper()
        match op:
            case "S":
                return True
            case "N":
                return False
            case _:
                print("Digite uma opção valida!")


def Continuar():
    while True:
        print("Deseja calcular outro valor? [S/N]")
        op = input("----> ").upper()
        match op:
            case "S":
                return True
            case "N":
                return False
            case _:
                print("Digite uma opção valida!")


def Main():
    while True:
        x1, y1 = ponto1()
        x2, y2 = ponto2()
        distância = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        print(
            f"A distância entre o ponto ({x1}, {y1}) e o ponto ({x2}, {y2}) é {distância:.2f}(aproximadamtente)"
        )
        b = ver_distância()
        if b == True:
            print(f"A distância exata é {distância}")
        a = Continuar()
        if a == False:
            print("Obrigado por usar o programa!")
            break


Main()
