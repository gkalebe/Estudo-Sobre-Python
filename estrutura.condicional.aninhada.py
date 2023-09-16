conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 1000
saque = 100
cheque_especial= 200

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso:")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o seu saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso ")
    else:
        print("Saldo Insuficiente")

elif conta_especial:

    print("Conta especial selecionada")
else:
    print("Sistema não reconheceu o tipo de sua conta, entre em contato com o SAQ")