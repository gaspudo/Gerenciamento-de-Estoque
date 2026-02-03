def Calcular(a, b, c):
    if b == '+':
       resultado = a + c
    elif b == '-':
        resultado = a - c
    elif b == '*' or 'x':
        resultado = a * c
    elif b == '/':
        resultado = a / c
    print(f'{a} {b} {c} = {resultado}')

while True:
    try:
        numero1 = int(input("Digite o primeiro numero. \n(Para Sair digite '000')\n "))
        calculo = input('escolha o tipo de calculo(+ , - , * ou / )').strip
        numero2 = int(input('Digite o segundo numero: '))
        if numero1 == 000:
            break
        Calcular(numero1, calculo, numero2)
    except ValueError:
        print('DIGITE UM VALOR VÁLIDO!!!')
    