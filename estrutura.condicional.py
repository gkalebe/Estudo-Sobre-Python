MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, possível tirar habilitação")

elif idade <= IDADE_ESPECIAL:
    print("Possível fazer aulas teorícas, mas não práticas. ")

else:
    print("Ainda não pode tirar a CNH. ")


if idade >= MAIOR_IDADE:
    print("Maior de idade, possível tirar habilitação")

else:
    print("não pode tirar habilitação")


