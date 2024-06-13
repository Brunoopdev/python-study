# Exibe números presentes entre dois outros números

# num1 = int(input('Digite um número inteiro\n'));
# num2 = int(input('Digite outro número inteiro\n'));
# print('');

# contador = 0;

# for contador in range(num1, num2 + 1):
#     print(f'{contador}');


#  Dias das colônias

# colonia A cresce 3% e inicia com 4.
# colonia B cresce 1,5% e inicia com 10.

# coloniaA = 4;
# coloniaB = 10;
# dias = 0;

# while coloniaA <= coloniaB:
#         coloniaA += coloniaA * 0.03;
#         coloniaB += coloniaB * 0.015;
#         dias += 1;
# print(f'Levou exatos: {dias} dias');


# 15 notas 

contador = 1;
nota = 0;

for contador in range(1,4):
    nota = int(input('Escreva uma nota entre 0 e 5 \n'));

    if nota < 0 or nota > 5:
        print('Valor inválido! Favor, inserir o valor correto!');
    else:
        print('Valor válido! Siga para o próximo!');