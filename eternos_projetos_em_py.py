def identificador_impar() :
    resposta = True
    somador = 0
    while resposta == True :
        numero = int(input("Informe um número :"))
        if numero%2 == 0 :
            print("O número: " + str(numero) + " não é impar")
        else : 
            somador += numero
            print("O número: " + str(numero) + " é impar") 
         
        responsavel = int(input("Repetir? \n1- para sim\n2- para não\n"))
        if responsavel == 1 :
            resposta = True;
        else : 
            resposta = False;
    print("A soma dos número impares é :" + str(somador))
    menu_principal()
    
    
def identificador_par() : 
    soma_numero_pares = 0;
    numero = int(input("Informe um número: "));
    somador = 0 
    resposta = True 
    while resposta == True: 
        if numero%2 == 0 :
            print("O número" + str(numero) + "é par!");
            soma_numero_pares += numero;
        else :
            print("O número" + str(numero + "não é par!"));
        responsavel = int(input("Repetir? \n1- para sim\n2- para não\n"))
        if responsavel == 1 :
            resposta = True;
        else : 
            resposta = False;
    print("A soma dos número pares é :" + str(soma_numero_pares))
    resposta1 = input("gostaria de ir para o Menu?\n1 - Sim\n2 - Não\nR: ")
    if resposta1 == 1 :
        menu_principal()
    else :
        identificador_par()
            
def fatorial() :
    numero_para_fatoriar = int(input("gostaria de ir para o Menu?\n1 - Sim\n2 - Não\nR: "))
    n = numero_para_fatoriar
    contador = 1
    resultado1 = 0
    for i in range(numero_para_fatoriar) : 
        n = n * (numero_para_fatoriar - contador)
        resultado = n
        if resultado != 0 and resultado != resultado1:
            print(str(i+1)+"° = " + str(resultado))
        resultado1 = resultado
        contador += 1
        
    resposta1 = int(input("gostaria de ir para o Menu?\n1 - Sim\n2 - Não\nR: "))
    if resposta1 == 1 :
        menu_principal()
    else :
        fatorial()
    
def contador_caracter() :
    print("Em desenvolvimento")
    menu_principal()
    
        
def quadrificador() :
    
    n = int(input("Informe um número que você quer quadrificar!"))
    resultado = n*n
    print("O resoltado: " + str(resultado))
    resposta = int(input("Gostaria de ir para o Menu?\n1- Sim\n2 - Não"))
    if resposta == 1 :
        menu_principal()
    else : 
        quadrificador()
        
def somar_vetor() :
    print("Em desenvolvimento")
    menu_principal()
    
        
def escala_vetor() :
    print("Em desenvolvimento") 
    menu_principal()
    
        
def transpor_matriz() :             
    print("Em desenvolvimento")
    menu_principal()
    
        
def somar_matriz() :
    print("Em desenvolvimento")
    menu_principal()
    
        
def menu_principal() : 
    print("Informe qual dos projetos você quer executar: \n"+"1- Identificador de impares\n" +  "2- Identificador de pares\n" +"3- Fatorial\n"+ "4- Contador de caracter\n" + "5- Quadrados de 10 números(Escolha do Usuário)\n" +"6- Somador de vetores\n" +"7- Escala do vetor\n"+"8- Trasnpostar matriz\n"+   "9- Somar matriz\n")    
    resposta = int(input())

    match resposta :
        case 1 : 
            identificador_impar();
        case 2 :
            identificador_par();
        case 3 :   
            fatorial();
        case 4 :
            contador_caracter();
        case 5 :
            quadrificador();
        case 6 :
            somar_vetor();
        case 7 :
            escala_vetor();
        case 8 :
            transpor_matriz();
        case 9 :
            somar_matriz();
    
menu_principal();