from random import randint


def dados():
    # a função randint retorna as combinações de forma uniforme
    return randint(1, 6), randint(1, 6)


def probabilidade(n, delta):
    sucesso = 0
    for _ in range(n):
        dado, dado2 = dados()
        if dado == delta or dado2 == delta or dado + dado2 == delta:
            sucesso += 1

    return f'Porcentagem {(sucesso / n) * 100}'




if __name__ == '__main__':
    for i in range(1, 13):
        print(f'{i} = {probabilidade(1000000, i)}')