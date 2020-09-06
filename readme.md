<h2>Este é o TP03 da disciplina de Lógica, Computação e Algoritmos. Este teste está organizado em questões, para que você possa demonstrar as competências trabalhadas até aqui nas ETAPAS 5 e 6 da disciplina.</h2>

<h3>Questão 01</h3>

<p>Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.</p>

<p>Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.</p>

<p><b>Fluxo de exceção:</b></p>

    O programa deve verificar se o número total de pessoas é maior do que zero.
    O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
    Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.

 Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de casa decimal, em vez de pontos.

Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas com replace('.',','). Exemplo:
valor = 1.99 # Valor numérico 
valor = str(valor) # Converte o valor para uma string
valor.replace('.', ',') # Substitui pontos por vírgulas
print(valor) # Imprimirá 1,99

 

Exemplo de saída do programa:

Informe o valor total do consumo: R$ 100.00

Informe o total de pessoas: 2

Informe o percentual do serviço, entre 0 e 100: 10

O valor total da conta, com a taxa de serviço, será de R$ 110,00.

Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.

<h3>Questão 02</h3>

 Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:

    Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
    Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
    Não tem direito a voto (menor de 16 anos).

Fluxo de exceção: 

    O programa deve verificar se a idade da pessoa é maior do que zero.

Exemplos de saída do programa:

Informe a idade: 25 

Tem obrigação de votar.

Informe a idade: 75

Não tem obrigação de votar.

Informe a idade: 12

Não tem direito a voto.

 

<h3>Questão 03</h3>

Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

 Fluxo de exceção: 

    O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

 Exemplo de saída do programa:

Informe nome do 1º participante: Zefrônio

Informe nota do 1º participante: 8.5

Informe nome do 2º participante: Oliúde

Informe nota do 2º participante: 6.0

Informe nome do 3º participante: Xonotrônfila

Informe nota do 3º participante: 7.8

Informe nome do 4º participante: Carbúncleo

Informe nota do 4º participante: 8.6

Informe nome do 5º participante: Zeugma

Informe nota do 5º participante: 9.4

O(a) vencedor(a) foi Zeugma com nota 9.4!

Salve seus códigos, junte-os em um arquivo zip e poste-os na tarefa do Moodle, respeitando a seguinte nomenclatura: “nome_sobrenome_DR1_TP3.zip”. 

Você pode, alternativamente, enviar os códigos através de um repositório git, uma IDE online, como o Repl.it ou um caderno Jupyter, como o Colab. Neste caso, assegure-se de que o conteúdo está público, e publique o link em um arquivo de texto na tarefa do Moodle, respeitando a seguinte nomenclatura: “nome_sobrenome_DR1_TP3.txt”.