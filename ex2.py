def calcular_moda(vetor):
    contagem = {}
    for elemento in vetor:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    max_frequencia = max(contagem.values(), default=0)
    moda = [k for k, v in contagem.items() if v == max_frequencia]
    return moda[0] if len(moda) == 1 else "Não existe moda"
entrada_usuario = input("Digite os números separados por espaço: ")
vetor_usuario = list(map(int, entrada_usuario.split()))
resultado = calcular_moda(vetor_usuario)
print(resultado)