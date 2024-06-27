import time

butacas = 50;

def sala_cine(butacas): #<----- funcion que agrega butacas a una lista 
    return [asientos +1 for asientos in range(butacas)]; 

sala = sala_cine(butacas); #<-- variable que almacena la sala de cine y la cantidad e butacas

def mostrar_sala(sala): #<----- funcion que muestra las butacas de manera ordenada
    for asientos, asiento in enumerate(sala, start=1):
        print(asiento, end=" ");
        if asientos % 10 == 0:
            print("\t");

def venta(): #<----------- funcion que realizara la venta de entradas, marcara los asientos comprados y ocupados, ademas de entregar por pantalla un valor total  temporal de entradas compradas
    
    venta_total = 0; #<--------- funcion que almacena temporalmente las ventas de entradas
    valor_asientos = 0; #<--------- funcion que almacena el valor de los asientos de manera temporal
    
    try: 
        while True: #<---- while que condiciona un maximo de 2 entradas de compra
            cantidad_entradas = int(input("Ingrese cuantas entradas desea comprar: "));
            if 0 < cantidad_entradas <= 2:
                break;
            else:
                print("Puede comprar entre 1 y 2 entradas maximo");
                
        for entrada in range(cantidad_entradas): #<-------- for que itera por la cantidad de entradas ingresadas
            
            rut = int(input("Ingrese su rut(sin punto ni digito verificador): "));
   
            print(f"\t***PANTALLA***\n{mostrar_sala(sala)}\n");
            asiento = int(input("\nIngrese el numero de asiento a comprar: "));
            
            if 1 <= asiento <= butacas: #<---- verifica que que asiento sea mayor a 1 y este en el rango de la cantidad de butacas
                if asiento >= 1 and asiento <= 20:
                    valor_asientos += 100000;

                elif asiento >= 21 and asiento <= 30:
                    valor_asientos += 50000;
                        
                else:
                    valor_asientos += 10000;
                
                if sala[asiento - 1] == "[X]":  #<--------------- valida si el asiento esta o no ocupado.
                    print("Asiento ocupado, vuelva a intentarlo")
                    break
                else:
                    sala[asiento - 1] = "[X]" #<----------------------- asigna una x al asiento comprado 
                print(f"El asiento N°{asiento} a sido comprado satisfactoriamente\n Total: {valor_asientos}\n");  
                datos_compra.append({'rut': rut,                   #<----------- guarda los datos en una lista, de directorios, mas abajo para ser consultada mas adelante
                                    'asiento':asiento,
                                    'total_compra':valor_asientos});
                
                datos_lista.append({'rut': rut,
                                    'asiento':asiento});

                venta_total += valor_asientos;
            
    except ValueError:
        print("Lo siento a ocurrido un error de: ",ValueError);
        
datos_compra = []; #<---------------- lista de diccionarios que almacena los datos de compras
datos_lista = [];


def total_compra(datos_compra): #<--------- funcion que calcula el total de todas las entradas compradas
    total_entradas = 0;
    for compras in datos_compra: #<------------ "for" que recorre la lista 'datos compra'
        total_entradas += compras['total_compra']; #<------------ sumador del valor, total compra, dentro de la lista
        
    return total_entradas;

def liastado_asistentes(datos_lista): #<---------------- funcion que Muestra los asistentes
    lista = []

    for datos in datos_lista:
        lista += datos['rut'], datos['asiento']
        print(f"El rut: {datos['rut']} tiene el asiento: {datos['asiento']}")








try:  #<-----Inicio excepcion-------------------------------------------------------------------------------------------------
    while True:
        opciones = 0; #<-----Variable repeticion menu inicial
        while opciones == 0:
            print("\tBienvenido a Concierto Michael Jackson");
            print("\t---ingrese una opcion a continuacion---\n");
            print("\t[1]Comprar Entrada\n\t[2]Mostrar Ubicaciones disponibles\n\t[3]Ver listado de asistentes\n\t[4]Mostrar ganancias totales\n\t[5]Salir\n");
            opciones = int(input("\tOpcion: "));
            if opciones >= 5 and opciones <= 0:
                print("Selecciono una opcion invalida");
            else:
                break;

        match opciones: #<------ inicio menu opciones con match --------------------------------------------------------------------------------------------
            case 1: #Opcion Compra Entradas ----------------------------------------------------------------------------------------------------------------------------------------

                venta();
            
            case 2: #Opcion dMostrar ubicaciones -----------------------------------------------------------------------------------------
                opc_sala = 0;  #<------ variable menu mostrar sala

                print(f"\t***Escenario***\n{mostrar_sala(sala)}");

                opc_sala = int(input("¿Desea Volver atras?\n [1] Si\n [2] Cerrar\n ")); #<----- opcion volver menu principal

                if opc_sala == 1:

                    continue;
                else:
                    break;
                
            case 3: # Muestra el listado de asistentes ----------------------------------------------------------------------------------------------------------------------

                opc_ventasTotal = 0;  #<------ variable menu mostrar Listado asistentes
                
                print(liastado_asistentes(datos_lista))
                
                opc_ventasTotal = int(input("¿Desea Volver atras?\n [1] Si\n [2] Cerrar\n ")); #<----- opcion volver menu principal
                if opc_ventasTotal == 1:
                    continue;
                else:
                    break;
            
            case 4: # Muestra las ganancias totales -----------------------------------------------------------------------------------------------------------------------
                opc_ventasTotal = 0;  #<------ variable menu mostrar venta

                print(f"El total de ventas es: ${total_compra(datos_compra)}"); #<------------ llamado a funcion que muestra el total de las ventas

                opc_ventasTotal = int(input("¿Desea Volver atras?\n [1] Si\n [2] Cerrar\n ")); #<----- opcion volver menu principal
                if opc_ventasTotal == 1:
                    continue;
                else:
                    break;
                
            case _: #<-------------------Termino menu match ----------------------------------------------------------------------------------------------
                print("----Muchas gracias vuelva pronto---")
                print("----Diego Arias---")
                tiempo = time.localtime()
                fecha = time.asctime(tiempo)
                print(fecha)
                
                break
            
except ValueError: #Termino excepcion --------------------------------------------------------------------------------------------------------------------------
    print("Ha ocurrido un error, a ingresado un valor incorrecto", ValueError);
    print("---------------------Gracias por preferirnos---------------------");
