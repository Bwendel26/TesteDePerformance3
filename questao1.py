# -*- coding: utf-8 -*-

# Desenvolva uma função que calcule a divisão de uma conta de consumo
# (conta de restaurante ou bar), em reais, considerando o número de pessoas 
# que estavam consumindo e a taxa de serviço que será paga ao garçom.

# Ao usuário do programa serão solicitados o valor total do consumo, 
# em reais, o número total de pessoas e o percentual do serviço prestado, 
# entre 0 e 100.

# Fluxo de exceção: 

#     O programa deve verificar se o número total de pessoas é maior do que zero.
#     O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#     Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o 
#     programa deve ser interrompido.

# Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), 
# usando vírgula como separador de casa decimal, em vez de pontos.
# Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, 
# substitua os pontos por vírgulas com replace('.',','). Exemplo:

# valor = 1.99 # Valor numérico 
# valor = str(valor) # Converte o valor para uma string
# valor.replace('.', ',') # Substitui pontos por vírgulas
# print(valor) # Imprimirá 1,99

# Exemplo de saída do programa:
# Informe o valor total do consumo: R$ 100.00
# Informe o total de pessoas: 2
# Informe o percentual do serviço, entre 0 e 100: 10
# O valor total da conta, com a taxa de serviço, será de R$ 110,00.
# Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.


def contaConsumo(totalConta, numPessoas, percentualServico):

    validacao = numPessoas > 0 and percentualServico >= 0 and percentualServico <= 100

    if(validacao):
        contaMaisServico = float(totalConta + (totalConta * percentualServico/100))
        contaIndividual = float(contaMaisServico / numPessoas)

        contaMaisServicoString = str(contaMaisServico)
        contaMaisServicoString.replace(".", ",")
        contaIndividualString = str(contaIndividual)
        contaIndividualString.replace(".", ",")

        print('O valor total da conta, com a taxa de serviço, será de R$ {}.\n'.format(contaMaisServicoString))
        print('Dividindo a conta por {} pessoa(s), cada pessoa deverá pagar R$ {}.'.format(numPessoas , contaIndividualString))

    else: 
        print("Valor(es) inválido(s)!")

    # Informe o valor total do consumo: R$ 100.00
    # Informe o total de pessoas: 2
    # Informe o percentual do serviço, entre 0 e 100: 10
    # O valor total da conta, com a taxa de serviço, será de R$ 110,00.
    # Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.

# teste:
contaConsumo(360, 3, 20)