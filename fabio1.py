import json


def AdicionarNome(nome, endereço, telefone):
    with open("nomes.json", "r") as arquivo:
        dados = json.load(arquivo)
    dado_completo = {nome: {"endereço": endereço, "telefone": telefone}}
    if dado_completo not in dados["nomes"]:
        dados["nomes"].append(
            {str(nome): {"endereço": str(endereço), "telefone": str(telefone)}}
        )
        with open("nomes.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("Nome cadastrado com sucesso!")
        return True
    else:
        print("Nome já cadastrado!")
        return False


def RemoverNome(nome, endereço, telefone):
    with open("nomes.json", "r") as arquivo:
        dados = json.load(arquivo)
    dado_completo = {nome: {"endereço": endereço, "telefone": telefone}}
    if dado_completo in dados["nomes"]:
        dados["nomes"] = [
            item
            for item in dados["nomes"]
            if not (
                nome in item
                and item[nome]["endereço"] == endereço
                and item[nome]["telefone"] == telefone
            )
        ]
        with open("nomes.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
            print("Nome removido com sucesso!")
            return True
    else:
        print("Nome não cadastrado!")
        return False

def ConsultarNome(nome):
    with open("nomes.json", "r") as arquivo:
        dados = json.load(arquivo)

        for item in dados["nomes"]:
            if str(nome) in item:
                print(f"Nome encontrado: {nome}")

                print(f"Endereço: {item[nome]['endereço']}")

                print(f"Telefone: {item[nome]['telefone']}")
        else:
            print("Nome não encontrado!")


def ListarNomes():
    with open("nomes.json", "r") as arquivo:
        dados = json.load(arquivo)

        print(f"Total de nomes: {len(dados['nomes'])}")

        for i, item in enumerate(dados["nomes"], start=1):
            for nome, detalhes in item.items():
                print(f"{i}. Nome: {nome}")

                print(f"   Endereço: {detalhes['endereço']}")

                print(f"   Telefone: {detalhes['telefone']}")


def ZerarAgenda():
    with open("nomes.json", "r") as arquivo:
        dados = json.load(arquivo)

        dados["nomes"].clear()

    with open("nomes.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Agenda zerada!")


def Desenvolvedores():
    print(
        f"""
--------------------------------------------------------------------------------

Gabriel Fernandes de Freitas Moreira Duarte de Lima - 202310648 - 2º período

Renan Auguto Santos Silva - 202311388 - 2º período

Maria Eduarda Franklin Barbosa - 202310532

--------------------------------------------------------------------------------
          """
    )


def Menu():
    print(
        f"""
#------------------------------------------------------#
# A G E N D A D E E N D E R E Ç O S #
#------------------------------------------------------#
# OPÇÕES #
# 1 – CADASTRAR NOME #
# 2 – CONSULTAR NOME #
# 3 – EXCLUIR NOME #
# 4 – LISTAR TODOS OS NOMES #
# 5 – ZERAR AGENDA #
# 6 - DESENVOLVEDORES #
# 7 – SAIR #
#------------------------------------------------------#
DIGITE A OPÇÃO DESEJADA (1 A 6):
"""
    )


# AdicionarNome(nome, endereço, email)
# ConsultarNome(nome)
# RemoverNome(nome, endereço, email)
# ListarNomes()
# ZerarAgenda()
# Desenvolvedores()
# Menu()

while True:
    Menu()
    op = input()
    match op:
        case "1":
            while True:
                nome = input("Digite o nome: ")
                endereço = input("Digite o endereço: ")
                telefone = input("Digite o telefone: ")
                a = AdicionarNome(nome, endereço, telefone)
                if a == True:
                    break
        case "2":
            nome = input("Digite o nome: ")
            ConsultarNome(nome)
        case "3":
            while True:
                nome = input("Digite o nome: ")
                endereço = input("Digite o endereço: ")
                telefone = input("Digite o telefone: ")
                a = RemoverNome(nome, endereço, telefone)
                if a == True:
                    break
        case "4":
            ListarNomes()
        case "5":
            ZerarAgenda()
        case "6":
            Desenvolvedores()
        case "7":
            break
        case _:
            print("Opção inválida!")
