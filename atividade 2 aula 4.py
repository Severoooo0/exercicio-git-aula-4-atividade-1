try:
    saldo = float(input("Informe o saldo da conta: R$ "))
    saque = float(input("Informe o valor do saque: R$ "))

    if saque <= 0:
        raise Exception("O valor do saque deve ser maior que zero.")

    if saque > saldo:
        raise Exception("Saldo insuficiente para realizar o saque.")

    saldo_restante = saldo - saque

    print("Saque realizado com sucesso!")
    print(f"Saldo restante: R$ {saldo_restante:.2f}")

except ValueError:
    print("Erro: informe apenas valores numéricos.")

except Exception as erro:
    print(f"Erro: {erro}")

finally:
    print("Operação bancária finalizada.")