menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
LIMITE = 500
LIMITE_SAQUE = 3
extrato = ""
numero_saques = 0

while True:
    input_usuario = input(menu)

    if input_usuario == "d":
        saldo += float(input("Digite o valor do depósito: "))
        extrato += f"+ {saldo}\n"
    
    if input_usuario == "s":
        if numero_saques < LIMITE_SAQUE:
            saque = float(input("Digite o valor do saque: "))
            if saque <= saldo and saque <= LIMITE:
                saldo -= saque
                extrato += f"- {saque}\n"
                numero_saques += 1
            elif saque > LIMITE:
                print("Limite de saque ultrapassado")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diários atingido")
    if input_usuario == "e":
        print(f"Saldo: {saldo}\n{extrato}")
    if input_usuario == "q":
        break
print("Fim do programa")