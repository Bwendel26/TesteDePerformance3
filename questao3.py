# -*- coding: utf-8 -*-

# Questão 03

# Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5
# participantes e suas respectivas notas, variando de 0 até 10. Crie uma 
# função que leia os nomes dos participantes e, ao final, apresente apenas 
# o nome e a nota do vencedor.

#   Fluxo de exceção: 
#   O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

#   Exemplo de saída do programa:
# Informe nome do 1º participante: Zefrônio
# Informe nota do 1º participante: 8.5
# Informe nome do 2º participante: Oliúde
# Informe nota do 2º participante: 6.0
# Informe nome do 3º participante: Xonotrônfila
# Informe nota do 3º participante: 7.8
# Informe nome do 4º participante: Carbúncleo
# Informe nota do 4º participante: 8.6
# Informe nome do 5º participante: Zeugma
# Informe nota do 5º participante: 9.4

# O(a) vencedor(a) foi Zeugma com nota 9.4!

def verificaVencedor():
    
    comprimento = 5
    nomes = []
    notas = []
    contador = 0
    notaMaior = 0
    vencedor = []
    stringResultado = "O(a) vencedor(a) foi {} com nota {:.2f}!"
    #stringEmpate = "Empate!!! Os vencedores foram: "
    
    for i in range(comprimento):
        contador += 1

        nome = str(input('Informe nome do {}º participante: '.format(contador)))
        nota = int(input('Informe nota do {}º participante: '.format(contador)))
        while(nota > 10 or nota < 0):
            nota = int(input('Informe nota do {}º participante: '.format(contador)))

        nomes.append(nome)
        notas.append(nota)
    
    for i in range(comprimento):
        if(notas[i] > notaMaior):
            notaMaior = notas[i]
            vencedor = [nomes[i], notas[i]]

        #elif(notas[i] == notaMaior):
            #vencedor += [nomes[i], notas[i]]
            #stringEmpate += "\n{} com nota {:.2f}"
            #stringResultado = stringEmpate
        else:
            pass

    print(stringResultado.format(vencedor[0], vencedor[1]))
    return None

verificaVencedor()