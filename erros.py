while True:

    try:
        n = int(input("Numerador: "))
        n2 = int(input("Denominador: "))
        result = n/n2
        if n<0 or n2<0:
            raise TypeError
    except ValueError: 
        print('Digite apenas números! ')
        print('Tente novamente...')
    except ZeroDivisionError:
        print('Denominador deve ser DIFERENTE DE ZERO!')
    except TypeError:
        print('O valor informado é negativo!')
    except Exception:
        print('Ocorreu um erro!')
    else:
        print(f'Resultado: {result:.2f}')
    finally:
        print("Tchau, obrigado.")