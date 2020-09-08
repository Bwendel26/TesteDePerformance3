# -*- coding: utf-8 -*-

def verificaVencedor():
    comprimento = 5
    nomes = []
    notas = []
    contador = 0
    notaMaior = 0
    stringResultado = "O(a) vencedor(a) foi {} com nota {:.2f}!"
    stringEmpate = "Empate!!! Os vencedores foram: "

    for i in range(comprimento):
        contador += 1

        nome = str(input('Informe nome do {}º participante: '.format(contador)))
        nota = int(input('Informe nota do {}º participante: '.format(contador)))
        while (nota > 10 or nota < 0):
            nota = int(input('Informe nota do {}º participante: '.format(contador)))

        nomes.append(nome)
        notas.append(nota)

    for i in range(comprimento):
        if (notas[i] > notaMaior):
            notaMaior = notas[i]
            stringResultado = stringResultado.format(nomes[i], notas[i])
            stringEmpate = stringResultado

        elif (notas[i] == notaMaior):
            stringEmpate += "\n{} com nota {:.2f}".format(nomes[i], notas[i])
            stringResultado = stringEmpate
        else:
            pass

    print(stringResultado)


verificaVencedor()
