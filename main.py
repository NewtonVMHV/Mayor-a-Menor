def main():
    num1 = 0;
    num2 = 0;
    num3 = 0;
    num4 = 0;

    print("Ingrese 3 números reales y vea el resultado en orden de mayor a menor:\n");
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))
    num3 = float(input('Ingrese el tercer número: '))
    print('--------------------------')

    if num1 == num2 and num2 == num3:
        print("No hay razón por la que pidas esto!!!!!!\n");
    elif num1 >= num2 and num1 >= num3:
        print("El primer número es el más grande de todos.\nSolo tengo que ordenar los números 2 y 3.\n* La variable num1 permanece con el mismo valor.\n");
        num4 = num2
        if num2 < num3:
            num2 = num3
            num3 = num4
    elif num2 >= num3 and num2 >= num1:
        print("El segundo número es el más grande de todos.\nSolo tengo que ordenar los números 1 y 3, que ahora es el segundo y el tercero.\n* La variable num1 recibe el valor num2\n");
        num4 = num2
        if num1 <= num3:
            num2 = num3
            num3 = num1
        else:
            num2 = num1
        num1 = num4
    elif num3 >= num1 and num3 >= num2:
        print("El tercer número es el más grande de todos,\nSolo tengo que ordenar el primer y segundo número ingresado, que ahora es el segundo y el tercero.\nLa variable num1 recibe el valor num3\n");
        num4 = num3
        if num1 <= num2:
            num3 = num1
        else:
            num3 = num2
            num2 = num1
        num1 = num4;
    print('Resultado: ', num1, ' ', num2, ' ', num3)
    return 0


if __name__ == '__main__':
    main()
