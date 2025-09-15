Saldo = 0
Limite = 500
Extrato = ""
Numero_saques = 0
Limite_saques = 3
valor = 0
usuarios = []
contas = []

def menu(): 
    
    menu="""
=== MENU ===
[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
"""
    print(menu)

def realizar_deposito(valor):
    global Saldo, Extrato
    
    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        Saldo += valor
        Extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    
    else:
        print("Operação falhou! O valor informado é inválido.")

def realizar_saque(valor):
    global Saldo, Extrato, Numero_saques

    if Numero_saques >= Limite_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")

    else:
        valor = float(input("Digite o valor do saque: "))

        if valor > Saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif valor > Limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            Numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    global Saldo, Extrato

    print("\n=== Extrato ===")

    if Extrato == "":
        print("Não foram realizadas movimentações.")

    else:
        print(Extrato)

    print(f"Saldo: R$ {Saldo:.2f}")
    print("================")

def criar_usuario():
    
    cpf = input("Digite o CPF (somente números): ")

    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
        return

    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    usuarios.append(usuario)

    print("Usuário criado com sucesso!")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Endereço: {endereco}")

def criar_conta():
    if not usuarios:
        print("Nenhum usuário cadastrado. Por favor, crie um usuário antes de criar uma conta.")
        return

    cpf = input("Digite o CPF do usuário para associar à conta: ")

    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario is None:
        print("Usuário não encontrado. Por favor, verifique o CPF e tente novamente.")
        return

    numero_conta = len(contas) + 1
    agencia = "0001"
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)

    print("Conta criada com sucesso!")
    print(f"Agência: {agencia}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Titular: {usuario['nome']}")

def main():
    menu()
    while True:

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            break

        elif opcao == "1":
            realizar_deposito(valor)
        
        elif opcao == "2":
            realizar_saque(valor)

        elif opcao == "3":
            exibir_extrato()
    
        elif opcao == "4":
            criar_usuario()

        elif opcao == "5":
            criar_conta()

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()