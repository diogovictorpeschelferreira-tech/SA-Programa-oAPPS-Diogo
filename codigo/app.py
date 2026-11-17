
import os, time

#cria uma função para validar a nota dos alunos, da linha 48 até a 60
def pedir_nota(mensagem):
    nota = int(input(mensagem))

    while nota < 0 or nota > 10:
        print("Erro! A nota deve estar entre 0 e 10.")
        nota = int(input("Digite novamente: "))

    return nota


#aqui cria uma função para validar a idade dos alunos, da linha 35 ate a 45
def pedir_idade(mensagem):
    idade = int(input(mensagem))

    while idade < 14 or idade > 18:
        print("Erro! O aluno deve ter entre 14 e 18 anos.")
        idade = int(input("Digite novamente: "))

    return idade

os.system("cls")

#inicio do programa
print("==================================")
print("    Seja bem vindo a Escola       ")
print("==================================")
time.sleep(1)
os.system("cls")

#aqui ele pede para você criar os nomes dos alunos
nome1 = input("Digite o primeiro nome do aluno: ")
time.sleep(1)
print(f"O primeiro aluno se chama: {nome1}\n")

nome2 = input("Digite o Segundo nome do aluno: ")
print(f"O segundo aluno se chama: {nome2}\n")

nome3 = input("Digite o terceiro nome do aluno: ")
print(f"O terceiro aluno se chama: {nome3}")
time.sleep(1)
os.system("cls")

#aqui ele pede para digitar a idade dos alunos e te mostra logo em  seguida
idade1 = pedir_idade(f"\nDigite a idade do {nome1}: ")
time.sleep(1)
print(f"{nome1} tem {idade1} anos")
time.sleep(1)
idade2 = pedir_idade(f"\nDigite a idade do {nome2}: ")
print(f"{nome2} tem {idade2} anos")
time.sleep(1)
idade3 = pedir_idade(f"\nDigite a idade do {nome3}: ")
print(f"{nome3} tem {idade3} anos")
time.sleep(1)
os.system("cls")


print("================================")
print("Agora vamos estabelecer as notas")
print("================================")
time.sleep(1)

#aqui ele pede a nota do aluno1
nota11 = pedir_nota(f"\nDigite a primeira nota do {nome1}: ")
nota12 = pedir_nota(f"Digite a segunda nota do {nome1}: ")
nota13 = pedir_nota(f"Digite a terceira nota do {nome1}: ")
time.sleep(1)

#aqui ele pede a nota do aluno2
nota21 = pedir_nota(f"\nDigite a primeira nota do {nome2}: ")
nota22 = pedir_nota(f"Digite a segunda nota do {nome2}: ")
nota23 = pedir_nota(f"Digite a terceira nota do {nome2}: ")
time.sleep(1)

#aqui ele pede a nota do aluno3
nota31 = pedir_nota(f"\nDigite a primeira nota do {nome3}: ")
nota32 = pedir_nota(f"Digite a segunda nota do {nome3}: ")
nota33 = pedir_nota(f"Digite a terceira nota do {nome3}: ")
time.sleep(3)
os.system("cls")

#aqui soma as notas dos alunos e divide por 3
soma_do_aluno1 = (nota11 + nota12 + nota13) /3
soma_do_aluno2 = (nota21 + nota22 + nota23) /3
soma_do_aluno3 = (nota31 + nota32 + nota33) /3

#mostra as notas finais no boletim dos alunos
print(f"O boletin de notas do {nome1}, ficou {soma_do_aluno1:.2f}")
time.sleep(1)
print(f"O boletin de notas do {nome2}, ficou {soma_do_aluno2:.2f}")
time.sleep(1)
print(f"O boletin de notas do {nome3}, ficou {soma_do_aluno3:.2f}")
time.sleep(3)
os.system("cls")

print("==========================================")
print("os alunos ficaram nessa situação no final ")
print("==========================================")
#aqui mostra se os alunos foram reprovados ou não
time.sleep(1)
if soma_do_aluno1 >= 7:
    print(f"{nome1}:FOI APROVADO")
elif soma_do_aluno1 >= 5:
    print(f"{nome1}: FICOU EM RECUPERAÇÃO")
else:
    print(f"{nome1}:FOI REPROVADO")
time.sleep(3)

if soma_do_aluno2 >= 7:
    print(f"{nome2}:FOI APROVADO")
elif soma_do_aluno2 >= 5:
    print(f"{nome2}: FICOU EM RECUPERAÇÃO")
else:
    print(f"{nome2}:FOI REPROVADO")
time.sleep(3)

if soma_do_aluno3 >= 7:
    print(f"{nome2}:FOI  APROVADO")
elif soma_do_aluno3 >= 5:
    print(f"{nome2}: FICOU EM RECUPERAÇÃO")
else:
    print(f"{nome2}:FOI REPROVADO")