saldo = 500
saque = 200
limite = 75
conta_especial = True

print (saldo >= saque)
print (saque <= limite)

print (saldo >= saque and saque <= limite)
print (saldo >= saque or saque <= limite)

print (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (saldo >= saque and saque <= limite or conta_especial and saldo >= saque)