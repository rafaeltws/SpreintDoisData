import random
import time

limiteEnergia = 40

sessoes = []


def calcularTarifa(horario, quantidadeVeiculos, tipoUsuario):

    valorTarifa = 1.20

    if horario >= 18 and horario <= 22:
        valorTarifa += 0.80

    if quantidadeVeiculos >= 3:
        valorTarifa += 0.50

    if tipoUsuario == "premium":
        valorTarifa -= 0.30

    return valorTarifa


def controlarEnergia():

    sessoesAtivas = []

    for sessao in sessoes:

        if sessao["status"] == "Carregando":
            sessoesAtivas.append(sessao)

    if len(sessoesAtivas) == 0:
        return

    potenciaPorVeiculo = limiteEnergia / len(sessoesAtivas)

    for sessao in sessoesAtivas:
        sessao["potencia"] = round(potenciaPorVeiculo, 2)

    print("\nControle de energia ativado")

    if len(sessoesAtivas) >= 3:
        print("Muitos veículos conectados")


def iniciarSessao():

    print("\nNova sessão")

    nomeUsuario = input("Nome: ")

    tipoUsuario = input("Tipo (comum/premium): ").lower()

    horarioAtual = int(input("Horario atual: "))

    sessao = {
        "nome": nomeUsuario,
        "tipo": tipoUsuario,
        "horario": horarioAtual,
        "energia": 0,
        "potencia": 0,
        "status": "Carregando"
    }

    sessoes.append(sessao)

    controlarEnergia()

    print("Sessão iniciada")


def simularRecarga():

    if len(sessoes) == 0:
        print("Nenhuma sessão")
        return

    tempoRecarga = int(input("Tempo de recarga: "))

    controlarEnergia()

    for minuto in range(1, tempoRecarga + 1):

        print(f"\nMinuto {minuto}")

        for sessao in sessoes:

            if sessao["status"] == "Carregando":

                sessao["energia"] += sessao["potencia"] / 60

                print(
                    sessao["nome"],
                    "-",
                    round(sessao["energia"], 2),
                    "kWh"
                )

        time.sleep(0.5)

    print("\nRecarga finalizada")


def finalizarSessao():

    nomeUsuario = input("Nome do usuário: ")

    for sessao in sessoes:

        if sessao["nome"].lower() == nomeUsuario.lower():

            sessao["status"] = "Finalizada"

            valorTarifa = calcularTarifa(
                sessao["horario"],
                len(sessoes),
                sessao["tipo"]
            )

            valorTotal = sessao["energia"] * valorTarifa

            print("\nResumo")
            print("Usuario:", sessao["nome"])
            print("Energia:", round(sessao["energia"], 2), "kWh")
            print("Valor:", round(valorTotal, 2))

            print("\n[OCPP]")
            print("Enviando dados...")

            print({
                "usuario": sessao["nome"],
                "energia": round(sessao["energia"], 2),
                "status": sessao["status"]
            })

            print("[MODBUS]")

            print(random.choice([
                "OK",
                "Dados recebidos",
                "Sessão salva"
            ]))

            controlarEnergia()

            return

    print("Usuário não encontrado")


def gerarRelatorio():

    print("\nRelatorio Geral")

    energiaTotal = 0

    for sessao in sessoes:

        energiaTotal += sessao["energia"]

        print("----------------")
        print("Nome:", sessao["nome"])
        print("Tipo:", sessao["tipo"])
        print("Status:", sessao["status"])
        print("Energia:", round(sessao["energia"], 2))

    print("\nEnergia total:", round(energiaTotal, 2))
    print("Sessões:", len(sessoes))


while True:

    print("\n====== MENU ======")
    print("1 - Nova sessão")
    print("2 - Simular recarga")
    print("3 - Finalizar sessão")
    print("4 - Relatório")
    print("5 - Sair")

    opcao = input("Opção: ")

    match opcao:

        case "1":
            iniciarSessao()

        case "2":
            simularRecarga()

        case "3":
            finalizarSessao()

        case "4":
            gerarRelatorio()

        case "5":
            print("Sistema encerrado")
            break

        case _:
            print("Opção inválida")