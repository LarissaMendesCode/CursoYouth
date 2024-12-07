class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor  
    
    def sacar(self, valor):
        self.saldo -= valor

titular = input('Informe o nome do titular: ')  
conta = ContaBancaria(titular, 100)  
deposito = int(input('Informe o valor do depósito: '))
conta.depositar(deposito)
saque= int((input('Informe o valor do do saque: ')))
conta.saque (saque)

# Exibindo o saldo atualizado
print(f'O saldo atual de {conta.titular} é R$ {conta.saldo}')



