def cumprimento(texto):
    return f"Olá, {texto}"
nome_do_aluno = input("Digite seu nome:")
print(cumprimento(nome_do_aluno))
import random
def media_dos_numeros():
    numeros = [random.randint(0, 100) for _ in range(3)]

    print("Números aleatórios sorteados:", numeros)

    media = sum(numeros) / len(numeros)

    return media


media = media_dos_numeros()
print("A média dos três números aleatórios é:", media)
