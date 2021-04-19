print("Usa esta calculadora para: Somar, Subtrair, Dividir e Multiplicar.")

numero1 = int(input("Primeiro Número:"))
operacao = input("Escolha a operação Matemática: + | - | / | * :")
numero2 = int(input("Segundo Número:"))

if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "/":
    print(numero1 / numero2)
elif operacao == "*":
    print(numero1 * numero2)



