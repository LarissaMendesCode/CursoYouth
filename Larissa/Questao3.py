class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, num1, num2):
        # Retorna o resultado da soma
        return num1 + num2
    
    def subtrair(self, num1, num2):
        # Retorna o resultado da subtração
        return num1 - num2
    def multiplicar(self, num1, num2):
        # Retorna o resultado da subtração
        return num1*num2
    def dividir(self, num1, num2):
        # Retorna o resultado da subtração
        return num1/num2

print("Escolha a opcao da calculadora:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Divisão")

# Solicita a operação desejada
operacao = input("Informe a operação desejada (1,2,3,4): ")

# Solicita os números ao usuário
num1 = float(input("Informe o numero 1: "))
num2 = float(input("Informe o numero 2: "))

# Cria uma instância da classe Calculadora
calculadora = Calculadora()

if operacao == '1':  # Verifica se a opção é somar
    # Chama o método somar e exibe o resultado
    resultado_soma = calculadora.somar(num1, num2)
    print(f'A soma de {num1} e {num2} é {resultado_soma}')
elif operacao == '2':  # Verifica se a opção é subtrair
    # Chama o método subtrair e exibe o resultado
    resultado_subtrair = calculadora.subtrair(num1, num2)
    print(f'A subtração de {num1} e {num2} é {resultado_subtrair}')
elif operacao == '3':  # Verifica se a opção é subtrair
    # Chama o método subtrair e exibe o resultado
    resultado_multiplicar = calculadora.multiplicar(num1, num2)
    print(f'A multiplicação de {num1} e {num2} é {resultado_multiplicar}')
elif operacao == '4':  # Verifica se a opção é subtrair
    # Chama o método subtrair e exibe o resultado
    resultado_dividir = calculadora.dividir(num1, num2)
    print(f'A Divisão de {num1} e {num2} é {resultado_dividir}')

else:
    print("Opção inválida! Por favor, escolha 1,2,3 ou 4.")
