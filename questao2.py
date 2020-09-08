# -*- coding: utf-8 -*-


def verificaEleitor(idade):
    
    if(idade > 0):
        if(idade >= 18 and idade < 70):
            print("Tem obrigação de votar.")

        elif((idade >= 16 and idade < 18) or idade > 70 and idade < 130):
            print("Não tem obrigação de votar.")

        elif(idade < 16):
            print("Não tem direito a voto.")

        else:
            pass

idade = int(input("Informe a idade: "))

verificaEleitor(idade)
