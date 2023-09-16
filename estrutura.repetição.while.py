opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar\n[2]Extrato\n[0]Sair\n:"))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo seu extrato...")
else: 
    print("Obrigado por fazer parte de nós! Tenha um ótimo dia!!!")