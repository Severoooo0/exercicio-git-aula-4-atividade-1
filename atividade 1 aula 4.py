try:
    primeiro = float(input("Digite o primeiro número: "))
    segundo = float(input("Digite o segundo número: "))

    resultado = primeiro / segundo

    print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: digite apenas números.")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

finally:
    print("Operação finalizada.")