# -*- coding: utf-8 -*-

def contaConsumo(totalConta, numPessoas, percentualServico):

    validacao = numPessoas > 0 and percentualServico >= 0 and percentualServico <= 100

    if(validacao):
        contaMaisServico = float(totalConta + (totalConta * percentualServico/100))
        contaIndividual = float(contaMaisServico / numPessoas)

        contaMaisServicoString = str(contaMaisServico)
        contaMaisServicoString.replace(".", ",")
        contaIndividualString = str(contaIndividual)
        contaIndividualString.replace(".", ",")

        print('\nO valor total da conta, com a taxa de serviço, será de R$ {}.\n'.format(contaMaisServicoString))
        print('Dividindo a conta por {} pessoa(s), cada pessoa deverá pagar R$ {}.'.format(numPessoas , contaIndividualString))

    else: 
        print("Valor(es) inválido(s)!")

        
valorConta = float(input("Informe o valor total do consumo: R$ "))
qtdPessoas = int(input("Informe o total de pessoas: "))
taxaServico = float(input("Informe o percentual do serviço, entre 0 e 100: "))

contaConsumo(valorConta, qtdPessoas, taxaServico)
