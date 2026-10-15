def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def main():
    print("=== Calculadora ===")
    num1 = float(input("Ingresa el primer numero: "))
    operacion = input("Elige una operacion (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo numero: "))

    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        resultado = dividir(num1, num2)
    else:
        resultado = "Operacion no valida"

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()