# Calculadora básica em Python

def soma(x, y):
    """Retorna a soma de x e y"""
    return x + y

def subtracao(x, y):
    """Retorna a subtração de x e y"""
    return x - y

def multiplicacao(x, y):
    """Retorna a multiplicação de x e y"""
    return x * y

def divisao(x, y):
    """Retorna a divisão de x e y"""
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y

def calculadora():
    print("Calculadora básica em Python")
    print("----------------------------")

    while True:
        print("Selecione uma opção:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            print("Resultado:", soma(x, y))
        elif opcao == "2":
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            print("Resultado:", subtracao(x, y))
        elif opcao == "3":
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            print("Resultado:", multiplicacao(x, y))
        elif opcao == "4":
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            print("Resultado:", divisao(x, y))
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    calculadora()
