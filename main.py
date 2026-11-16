# 2. tenha a variável pontos criada antes do loop;
pontos = 0

# 1. tenha as duas listas com 5 perguntas e 5 respostas;
perguntas = [
    'Quantos átomos de Hidrogênio tem a água? ',
    'Qual a aceleração da gravidade na superfície da Terra em m/s? ',
    'Qual a fórmula química do sal de cozinha (Cloreto de Sódio)? ',
    'Quantos planetas temos no Sistema Solar? ',
    'Qual o maior órgão do corpo humano? '
]
respostas = [
    '2',
    '9.8',
    'NaCl',
    '8',
    'pele'
]

# 3. use for com range(5) para percorrer as 5 perguntas;
for i in range(5):
    # 4. dentro do loop, use input para receber a resposta e if/else para verificar;
    resposta = input(perguntas[i])
    if resposta == respostas[i]:
        # 5. atualize a pontuação a cada acerto;
        pontos += 1
        print('Resposta correta!')
    else:
        print('Resposta errada!')

# 6. depois do loop, mostre a pontuação final;
print(f'Placar final: {pontos} pontos.')

# 7. depois do loop, use if/elif/else para mostrar a mensagem personalizada.
if pontos == 5:
    print('Perfeito! Você é um expert em ciências!')
elif pontos >= 3:
    print('Bom trabalho! Você mandou bem.')
elif pontos >= 1:
    print('Foi por pouco! Continue tentando.')
else:
    print('Que tal estudar mais um pouco?')