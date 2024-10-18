from abc import ABC, abstractmethod
from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)
        else:
            print("Conta não pertence ao cliente.")

# Classe PessoaFisica, herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Classe abstrata Transacao (interface)
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque, implementa a interface Transacao
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
        else:
            print("Saque não realizado.")

# Classe Deposito, implementa a interface Transacao
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
        else:
            print("Depósito não realizado.")

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {"transacao": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now()}
        )

# Classe Conta
class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            print("Valor inválido para depósito.")
            return False

    def saldo(self):
        return self.saldo

# Classe ContaCorrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite=500, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques and valor <= self.limite:
            if super().sacar(valor):
                self.saques_realizados += 1
                return True
        else:
            print(f"Limite de saques atingido ou valor maior que o permitido ({self.limite}).")
            return False

# Exemplo de uso do sistema
def main():
    # Criando cliente
    cliente = PessoaFisica(nome="João Silva", cpf="123456789", data_nascimento="01/01/1980", endereco="Rua ABC")

    # Criando conta
    conta_corrente = ContaCorrente(cliente, numero=12345, agencia="001")

    # Adicionando conta ao cliente
    cliente.adicionar_conta(conta_corrente)

    # Realizando depósitos
    deposito1 = Deposito(1000)
    cliente.realizar_transacao(conta_corrente, deposito1)

    # Realizando saques
    saque1 = Saque(200)
    cliente.realizar_transacao(conta_corrente, saque1)

    # Mostrando saldo
    print(f"Saldo atual: R$ {conta_corrente.saldo:.2f}")

    # Exibindo o extrato
    print("\nExtrato:")
    for transacao in conta_corrente.historico.transacoes:
        print(f"{transacao['transacao']} de R$ {transacao['valor']:.2f} em {transacao['data']}")

if __name__ == "__main__":
    main()
