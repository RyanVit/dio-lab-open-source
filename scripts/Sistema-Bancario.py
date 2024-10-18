class SistemaBancario:
    def __init__(self):
        # Inicializa as variáveis de controle
        self.saldo = 0.0  # Armazena o saldo atual da conta
        self.extrato = []  # Lista que irá armazenar as operações de depósito e saque
        self.limite_saques_diarios = 3  # Limite de saques que podem ser feitos por dia
        self.limite_saque_valor = 500.0  # Valor máximo permitido por saque
        self.saques_realizados = 0  # Contador de saques realizados no dia

    def depositar(self, valor):
        # Verifica se o valor do depósito é positivo
        if valor > 0:
            self.saldo += valor  # Adiciona o valor ao saldo
            self.extrato.append(f"Depósito: R$ {valor:.2f}")  # Registra o depósito no extrato
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            # Exibe mensagem de erro caso o valor seja inválido (negativo ou zero)
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        # Verifica se o usuário já realizou o limite máximo de saques diários
        if self.saques_realizados >= self.limite_saques_diarios:
            print("Limite diário de saques atingido.")
        # Verifica se o valor solicitado para saque excede o limite permitido
        elif valor > self.limite_saque_valor:
            print(f"Valor máximo para saque é R$ {self.limite_saque_valor:.2f}.")
        # Verifica se o saldo é suficiente para realizar o saque
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        # Verifica se o valor do saque é positivo
        elif valor > 0:
            self.saldo -= valor  # Subtrai o valor do saldo
            self.saques_realizados += 1  # Incrementa o contador de saques realizados
            self.extrato.append(f"Saque: R$ {valor:.2f}")  # Registra o saque no extrato
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            # Exibe mensagem de erro caso o valor do saque seja inválido
            print("Valor inválido para saque.")

    def exibir_extrato(self):
        # Verifica se o extrato está vazio
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            # Exibe todas as operações de depósito e saque
            print("\nExtrato:")
            for movimento in self.extrato:
                print(movimento)
            # Exibe o saldo atual da conta
            print(f"Saldo atual: R$ {self.saldo:.2f}")

def main():
    # Cria uma instância da classe SistemaBancario
    conta = SistemaBancario()

    while True:
        # Exibe o menu de operações para o usuário
        print("\n=== Sistema Bancário ===")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        
        # Recebe a escolha do usuário
        opcao = input("Escolha uma operação (1/2/3/4): ")

        # Verifica qual operação o usuário escolheu
        if opcao == '1':
            # Pede ao usuário para digitar o valor do depósito
            valor = float(input("Digite o valor para depósito: R$ "))
            conta.depositar(valor)  # Chama o método de depósito
        elif opcao == '2':
            # Pede ao usuário para digitar o valor do saque
            valor = float(input("Digite o valor para saque: R$ "))
            conta.sacar(valor)  # Chama o método de saque
        elif opcao == '3':
            conta.exibir_extrato()  # Chama o método para exibir o extrato
        elif opcao == '4':
            # Encerra o loop e, consequentemente, o sistema
            print("Encerrando o sistema. Até logo!")
            break
        else:
            # Exibe mensagem de erro caso o usuário insira uma opção inválida
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o sistema
