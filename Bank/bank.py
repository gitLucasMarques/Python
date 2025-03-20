from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Union
from enum import Enum
from datetime import datetime
from random import randint
import random

class BancoError(Exception):
    def __init__(self, message: str = "An error occurred in the library system"):
        super().__init__(message)

class ErroSaldoInsuficienteCC(BancoError):
    def __init__(self, limiteChequeEspecial: float):
        message = f"Saldo insuficiente! A conta está utilizando o Limite do Cheque Especial! LCE = {limiteChequeEspecial}"
        super().__init__(message)

class ErroAplicarRendimentoCC(BancoError):
    def __init__(self, message: str = "Operação inválida para Conta Corrente (CC)!"):
        super().__init__(message)

class ErroSaldoInsuficienteCP(BancoError):
    def __init__(self, message: str = "Saldo inexistente nesta Conta Poupança!"):
        super().__init__(message)

class ErroNumSaquesDiariosCP(BancoError):
    def __init__(self, message: str = "Número de saques atingido nesta Conta Poupança!"):
        super().__init__(message)

class ErroSaldoContaExcCC(BancoError):
    def __init__(self, message: str = "Faça o saque/pagamento (LCE) do saldo na conta para prosseguir!"):
        super().__init__(message)

class ErroSaldoContaExcCP(BancoError):
    def __init__(self, message: str = "Faça o saque do saldo na conta para prosseguir!"):
        super().__init__(message)

class ErroContaNaoPertenceAoCliente(BancoError):
    def __init__(self, message: str = "Esta conta não pertence a este cliente!"):
        super().__init__(message)

class ErroOpcaoPadrao(BancoError):
    def __init__(self, message: str = "Caso Padrão"):
        super().__init__(message)


class tipoContas(Enum):
    CONTA_CORRENTE = 1
    CONTA_POUPANCA = 2
    
class ContaBancaria(ABC):
    
    @abstractmethod
    def debitar(self, valorDebitado: float):
        pass
    
    @abstractmethod
    def creditar(self, valorCreditado: float):
        pass 
    
    @abstractmethod
    def consultarSaldo(self):
        pass
    
    @abstractmethod
    def saque(self, ValorSaque: float):
        pass

    @abstractmethod
    def aplicarRendimento(self):
        pass

    @abstractmethod
    def extratoBancario(self):
        pass
    
@dataclass
class Enderecos():
    pais: str
    telefone: str

class Cliente():
    nome: str
    cpf: str
    enderecos: List[Enderecos] = []
    contas: List[Union["ContaCorrente", "ContaPoupança"]] = []
    
    def adicionarConta(self, contaNova: ContaBancaria):
        return self.contas.append(contaNova)
    
    def removerConta(self, numeroConta: str):
        for contas in self.contas:
            if contas.numero == numeroConta and (contas.limiteChequeEspecial != 0 or contas.saldo != 0):
                raise ErroSaldoContaExcCC()

        for contas in self.contas:
            if contas.numero == numeroConta:
                self.contas.remove(contas)
                return True
            
        return ErroContaNaoPertenceAoCliente()
    
    def listarContas(self):
        print("\nCONTAS DE", self.nome, ":")
        for conta in self.contas:
            print(conta)      
        return True

@dataclass
class ContaCorrente(ContaBancaria):
    saldo: float
    saldo = 0
    numero: str
    numero = '0'

    historicoCC = []

    limiteChequeEspecial: float
    limiteChequeEspecial = 0
    
    def debitar(self, valorDebitado: float) -> float:
        saldo_final = self.saldo - valorDebitado

        if saldo_final >= 0:
            self.saldo = self.saldo - valorDebitado
            hora_transacao = str(datetime.now())
            self.historicoCC.append(f"Débito: -{valorDebitado}             | {hora_transacao[0:19]}")
            return True
        
        else:
            self.saldo = 0
            self.limiteChequeEspecial = self.limiteChequeEspecial + (-saldo_final)
            raise ErroSaldoInsuficienteCC(self.limiteChequeEspecial)
    
    def creditar(self, valorCreditado: float) -> float:
        self.saldo = self.saldo + valorCreditado
        hora_transacao = str(datetime.now())
        self.historicoCC.append(f"Crédito: +{valorCreditado}            | {hora_transacao[0:19]}")
        return True
    
    def consultarSaldo(self):
        if self.saldo == None:
            raise ErroSaldoInsuficienteCC(self.limiteChequeEspecial)
        return print("Saldo atual (CC):", self.saldo, "LCE:", self.limiteChequeEspecial)
    
    def saque(self, valorSaque: float):
        saldo_final = self.saldo - valorSaque

        if saldo_final >= 0:
            self.saldo = self.saldo - valorSaque
            hora_transacao = str(datetime.now())
            self.historicoCC.append(f"Saque: -{valorSaque}              | {hora_transacao[0:19]}")
            return print("Saldo atual após o saque (CC):", self.saldo)
        
        else:
            self.saldo = 0
            self.limiteChequeEspecial = self.limiteChequeEspecial + (-saldo_final)
            hora_transacao = str(datetime.now())
            self.historicoCC.append(f"Saque (LCE): -{valorSaque}        | {hora_transacao[0:19]}")
            raise ErroSaldoInsuficienteCC(self.limiteChequeEspecial)

    def aplicarRendimento(self, taxaRendimento: int):
        raise ErroAplicarRendimentoCC()

    def extratoBancario(self):
        print("\n\nHISTÓRICO DA CONTA CORRENTE (CC) Num:", self.numero, "\n")
        for mov in self.historicoCC:
            print(mov)
        return True

@dataclass
class ContaPoupança(ContaBancaria):
    saldo: float
    saldo = 0
    numero: str
    numero = '0'

    historicoCP = []

    numSaquesDiarios: int
    numSaquesDiarios = 0
    taxaRendimento: float
    taxaRendimento = 0
    
    def debitar(self, valorDebitado: float) -> float:
        saldo_final = self.saldo - valorDebitado

        if saldo_final >= 0:
            self.saldo = self.saldo - valorDebitado
            hora_transacao = str(datetime.now())
            self.historicoCP.append(f"Débito: -{valorDebitado}             | {hora_transacao[0:19]}")
            return True
        raise ErroSaldoInsuficienteCP()
    
    def creditar(self, valorCreditado: float) -> float:
        self.saldo = self.saldo + valorCreditado
        hora_transacao = str(datetime.now())
        self.historicoCP.append(f"Crédito: +{valorCreditado}            | {hora_transacao[0:19]}")
        return True
    
    def consultarSaldo(self):
        if self.saldo == None:
            raise ErroSaldoInsuficienteCP()
        return print("Saldo atual (CP):", self.saldo)
    
    def saque(self, valorSaque: float):

        if self.numSaquesDiarios < 3:
            saldo_final = self.saldo - valorSaque

            if saldo_final >= 0:
                self.saldo = self.saldo - valorSaque
                self.numSaquesDiarios += 1
                hora_transacao = str(datetime.now())
                self.historicoCP.append(f"Saque: -{valorSaque}              | {hora_transacao[0:19]}")
                print("Saldo atual após o saque (CP):", self.saldo)
                return True
            else:
                raise ErroSaldoInsuficienteCP()
        else:
            raise ErroNumSaquesDiariosCP()
    
    def aplicarRendimento(self, taxaRendimento: int):
        valorInicial = self.saldo
        self.saldo = self.saldo + (self.saldo * taxaRendimento)
        hora_transacao = str(datetime.now())
        self.historicoCP.append(f"Rendimento: {valorInicial * taxaRendimento}       | {hora_transacao[0:19]}")
        return True

    def extratoBancario(self):
        print("\n\nHISTÓRICO DA CONTA POUPANÇA (CP) Num:", self.numero, "\n")
        for mov in self.historicoCP:
            print(mov)
        return True
    
class Banco():
    listaClientes: List[Cliente] = []
    numContasBanco: int

    def dadosCliente(self, nome: str, cpf: str, endereco : Enderecos):
        novoCliente = Cliente()
        novoCliente.nome = nome
        novoCliente.cpf = cpf
        novoCliente.enderecos = endereco
        novoCliente.contas = []
        return novoCliente
    
    def novoCliente(self, cliente: Cliente):
        return self.listaClientes.append(cliente)

    def excluirCliente(self, cliente: Cliente):
        for contas in cliente.contas:
            if contas.tipo == 1 and (contas.limiteChequeEspecial != 0 or contas.saldo != 0):
                raise ErroSaldoContaExcCC()
            
            if contas.tipo == 2 and contas.saldo != 0:
                raise ErroSaldoContaExcCP()
            
        for contas in self.listaClientes:
            if contas.cpf == cliente.cpf:
                self.listaClientes.remove(contas)
                return print("\nCliente excluído!") 

    def novaConta(self, cliente: Cliente, tipoConta: tipoContas, saldoConta: float):
        if tipoConta == 1:
            novaConta = ContaCorrente()
            novaConta.limiteChequeEspecial = 0
        else:
            novaConta = ContaPoupança()
        
        novaConta.titular = cliente
        novaConta.tipo = tipoConta
        novaConta.saldo = saldoConta
        novaConta.numero = self.numContasBanco + 1
        self.numContasBanco += 1
        cliente.adicionarConta(novaConta)
        return True
    
    def excluirConta(self, cliente: Cliente, numeroConta: int):
        if cliente.removerConta(numeroConta) == True:
            return True
        return ErroContaNaoPertenceAoCliente()
    
    def deposito(self, conta: ContaBancaria, valorDeposito: float):
        return conta.creditar(valorDeposito)
        
    def saque(self, conta: ContaBancaria, valorSaque: float):
        return conta.saque(valorSaque)
    
    def transferencia(self, contaOrig: ContaCorrente, contaDest: ContaCorrente, valorDeposito: float):
        if contaOrig.tipo == 1:
            contaOrig.debitar(valorDeposito)
            contaDest.creditar(valorDeposito)
            return True

        if contaOrig.tipo == 2 and contaOrig.debitar(valorDeposito) == True:
            contaDest.creditar(valorDeposito)
            return True
        
        return False
    
    def aplicarRendimento(self, conta: ContaPoupança, taxaRendimento: int):
        return conta.aplicarRendimento(taxaRendimento)
    
    def listarContas(self):
        for cliente in self.listaClientes:
            cliente.listarContas()   

class main():
    banco = Banco()
    banco.numContasBanco = 0

    enderecos = [
        Enderecos('Alemanha', '56432413231'),
        Enderecos('Itália', '1232442342'),
        Enderecos('Espanha', '27786534242'),
        Enderecos('Japão', '123368968763')
    ]

    cliente1 = banco.dadosCliente('Lucas Marques', '532145632345', enderecos[0])
    banco.novoCliente(cliente1)
    banco.novaConta(cliente1, 1, 10000)

    cliente2 = banco.dadosCliente('João Augusto', '65445567446', enderecos[1])
    banco.novoCliente(cliente2)
    banco.novaConta(cliente2, 1, 10000)

    cliente3 = banco.dadosCliente('Christian Vinicius', '2543243646456', enderecos[2])
    banco.novoCliente(cliente3)
    banco.novaConta(cliente3, 1, 10000)

    cliente4 = banco.dadosCliente('Ramon Makiyama', '2436453212`', enderecos[3])
    banco.novoCliente(cliente4)
    banco.novaConta(cliente4, 1, 10000)

    banco.listarContas()

    ##---------------------------------------- main() otimizada para diversos casos diferentes ---------------------------------------------------##

    for i in range(30):
        
        index_clientes = randint(0, len(banco.listaClientes) - 1)
        index_tipoConta = tipoContas(randint(1, 2))

        if len(banco.listaClientes[index_clientes].contas) > 0:
            index_numconta = randint(0, len(banco.listaClientes[index_clientes].contas) - 1)
        else:
            index_numconta = 0

        index_saldo = randint(0, 100)
        index_acao = randint(1, 8)
        index_taxa = random.uniform(0.01, 0.1)

        print(f"Ação {index_acao} para o cliente {banco.listaClientes[index_clientes].nome}")

        if index_acao == 1:
            banco.excluirCliente(banco.listaClientes[index_clientes])
            print(f"Cliente {banco.listaClientes[index_clientes].nome} excluído!")

        elif index_acao == 2:
            banco.novaConta(banco.listaClientes[index_clientes], index_tipoConta, index_saldo)
            tipo = str(index_tipoConta)
            print(f"Nova {tipo[11:]} adicionada a {banco.listaClientes[index_clientes].nome}!")

        elif index_acao == 3:
            if len(banco.listaClientes[index_clientes].contas) > 0:
                banco.excluirConta(banco.listaClientes[index_clientes], banco.listaClientes[index_clientes].contas[index_numconta].numero)
                print(f"Conta Num. {banco.listaClientes[index_clientes].contas[index_numconta].numero} excluída do perfil de {banco.listaClientes[index_clientes].nome}!")
            else:
                print(f"Cliente {banco.listaClientes[index_clientes].nome} não possui contas para excluir.")

        elif index_acao == 4:
            if len(banco.listaClientes[index_clientes].contas) > 0:
                banco.deposito(banco.listaClientes[index_clientes].contas[index_numconta], index_saldo)
                print(f"Saldo de {index_saldo} adicionado à conta {banco.listaClientes[index_clientes].contas[index_numconta].numero}, do cliente {banco.listaClientes[index_clientes].nome}!")
            else:
                print(f"Cliente {banco.listaClientes[index_clientes].nome} não possui contas para depósito.")

        elif index_acao == 5:
            if len(banco.listaClientes[index_clientes].contas) > 0:
                banco.saque(banco.listaClientes[index_clientes].contas[index_numconta], index_saldo)
                print(f"Saque de {index_saldo} efetuado na conta {banco.listaClientes[index_clientes].contas[index_numconta].numero}, do cliente {banco.listaClientes[index_clientes].nome}!")
            else:
                print(f"Cliente {banco.listaClientes[index_clientes].nome} não possui contas para saque.")

        elif index_acao == 6:
            if len(banco.listaClientes[index_clientes].contas) > 1:
                banco.transferencia(banco.listaClientes[index_clientes].contas[index_numconta], banco.listaClientes[len(banco.listaClientes) - 1].contas[0], index_saldo)
                print(f"Transferência de {index_saldo} efetuada da conta {banco.listaClientes[index_clientes].contas[index_numconta].numero} para a conta {banco.listaClientes[len(banco.listaClientes) - 1].contas[0].numero}!")
            else:
                print(f"Cliente {banco.listaClientes[index_clientes].nome} não possui contas suficientes para realizar a transferência.")

        elif index_acao == 7:
            if len(banco.listaClientes[index_clientes].contas) > 0:
                banco.aplicarRendimento(banco.listaClientes[index_clientes].contas[index_numconta], index_taxa)
                print(f"Rendimento aplicado na conta {banco.listaClientes[index_clientes].contas[index_numconta].numero}, gerando {banco.listaClientes[index_clientes].contas[index_numconta].saldo}!")
            else:
                print(f"Cliente {banco.listaClientes[index_clientes].nome} não possui contas para aplicar rendimento.")

        elif index_acao == 8:
            banco.listarContas()

        elif index_acao > 8 or index_acao < 1:
            raise ErroOpcaoPadrao()
        

    ##--------------------------------------------------- main() básica para mostrar funcionamento das funções -----------------------------------------## 
    
    # banco.novaConta(cliente1, 2, 300)
    # banco.transferencia(cliente2.contas[0], cliente1.contas[1], 200)
    # cliente1.contas[1].extratoBancario()
    # cliente2.contas[0].extratoBancario()

    # banco.saque(cliente3.contas[0], 400)
    # banco.novaConta(cliente3, 2, 200)
    # banco.aplicarRendimento(cliente3.contas[1], 0.2)
    # cliente3.contas[0].extratoBancario()
    # cliente3.contas[1].extratoBancario()

    # banco.novaConta(cliente2, 2, 6000)
    # banco.saque(cliente2.contas[0], cliente2.contas[0].saldo)
    # banco.excluirConta(cliente2, cliente2.contas[0].numero)

    # banco.listarContas()

main()