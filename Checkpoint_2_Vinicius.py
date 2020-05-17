# Checkpoint 2/ Vinicius de Jesus Correia - RM 85570
email = {}

print("\nOlá ! usuario, por favor digite um dos seguintes numeros para alguma atividade do código: ","\nAdicionar email: 1","\nBuscar email: 2", "\nMostrar emails: 3", "\nApagar algum email: 4","\nPara interromper o funcionamento do programa: 0")

while True:
    comec = int(input("\nQual funçao deseja?"))
    if comec == 1:
        tag = input("Qual a tag o e-mail vazado:")
        mail = input("Digite o e-mail vazado:")
        sen = input("Qual a senha desse email vazado?")
        vali = input("Qual a validade desse vazamento:")
        email[tag] ={"e-mail" : mail, "Senha" : sen, "Validade" : vali}

    if comec == 2: 
        mail = input("Qual e-mail deseja buscar? (digite a tag dele)")
        if mail in email:
            print("Este e-mail foi vazado as suas informações:")
            print(email[mail])
        else:
            print("Este e-mail não esta listado no dicionario")

    if comec == 3: 
         print(email)
         
    if comec == 4:                 
        saiu = input("Qual e-mail gostaria de remover lista de vazamentos?(Digite a tag referente)")
        email.pop(saiu)
        print(email)                               
    if comec == 0:
        break
