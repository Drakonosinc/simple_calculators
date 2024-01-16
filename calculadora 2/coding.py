while True:
    print()
    print("que ecuacion matematica quieres realizar")
    print("1:suma, 2:resta, 3:multiplicacion, 4:divicion, 5:elevar un numero")
    print("escribe uno de los numeros")
    try :
        e=int(input(" "))
        if e==1:
            number1=int(input("primer numero "))
            number2=int(input("segundo numero "))
            result=number1+number2
            print(f"este es el resultado {result}")
        elif e==2:
            number1=int(input("primer numero "))
            number2=int(input("segundo numero "))
            result=number1-number2
            print(f"este es el resultado {result}")
        elif e==3:
            number1=int(input("primer numero "))
            number2=int(input("segundo numero "))
            result=number1*number2
            print(f"este es el resultado {result}")
        elif e==4:
            number1=int(input("primer numero "))
            number2=int(input("segundo numero "))
            result=number1/number2
            print(f"este es el resultado {result}")
        elif e==5:
            number1=int(input("numero "))
            number2=int(input("numero al que se elevara "))
            result=number1**number2
            print(f"este es el resultado {result}")
        else:
            print("introduce una opcion valida")
    except:
        print("introduce un valor numerico")
