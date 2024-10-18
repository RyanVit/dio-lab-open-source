class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saques_diarios = 3
        self.limite_saque_valor = 500.0
        self.saques_realizados = 0

def depositar(conta, valor):
    """Função para realizar depósitos."""
    if valor > 0:
        conta.saldo += valor
        conta.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(conta, valor):
    """Função para realizar saques."""
    if conta.saques_realizados >= conta.limite_saques_diarios:
        print("Limite diário de saques atingido.")
    elif valor > conta.limite_saque_valor:
        print(f"Valor máximo para saque é R$ {conta.limite_saque_valor:.2f}.")
    elif valor > conta.saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > 0:
        conta.saldo -= valor
        conta.saques_realizados += 1
        conta.extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")

def exibir_extrato(conta):
    """Função para exibir o extrato."""
    if not conta.extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for movimento in conta.extrato:
            print(movimento)
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

def cadastrar_usuario(usuarios):
    """Função para cadastrar um novo usuário (cliente)."""
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    usuario = Usuario(nome, cpf)
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuario

def cadastrar_conta(usuario):
    """Função para cadastrar uma nova conta bancária para um usuário."""
    conta = ContaBancaria()
    usuario.adicionar_conta(conta)
    print(f"Conta bancária criada para o usuário {usuario.nome}!")
    return conta

def main():
    usuarios = []  # Lista para armazenar os usuários cadastrados
    
    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Cadastrar usuário")
        print("2. Cadastrar conta bancária")
        print("3. Depósito")
        print("4. Saque")
        print("5. Extrato")
        print("6. Sair")
        opcao = input("Escolha uma operação (1/2/3/4/5/6): ")

        if opcao == '1':
            # Cadastrar um novo usuário
            cadastrar_usuario(usuarios)

        elif opcao == '2':
            # Associar uma conta a um usuário existente
            cpf = input("Digite o CPF do cliente: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                cadastrar_conta(usuario)
            else:
                print("Usuário não encontrado. Cadastre o usuário primeiro.")
                
        elif opcao == '3':
            # Realizar depósito
            cpf = input("Digite o CPF do cliente: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                valor = float(input("Digite o valor para depósito: R$ "))
                depositar(usuario.contas[0], valor)  # Usando a primeira conta como exemplo
            else:
                print("Usuário ou conta não encontrado.")
                
        elif opcao == '4':
            # Realizar saque
            cpf = input("Digite o CPF do cliente: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                valor = float(input("Digite o valor para saque: R$ "))
                sacar(usuario.contas[0], valor)  # Usando a primeira conta como exemplo
            else:
                print("Usuário ou conta não encontrado.")
                
        elif opcao == '5':
            # Exibir extrato
            cpf = input("Digite o CPF do cliente: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                exibir_extrato(usuario.contas[0])  # Usando a primeira conta como exemplo
            else:
                print("Usuário ou conta não encontrado.")
                
        elif opcao == '6':
            # Encerrar o sistema
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
if __name__ == "__main__":
    main()
