#Proyecto 2 Base de Datos
#Sebastian Juarez 21471
#Creación de un porgrama que maneja a los usuarios de IHealth +
import sys
import psycopg2
conn= psycopg2.connect(database="Proyecto2",
    user='postgres',
    password='Fac3viche',
    host='localhost')
conn.autocommit=True

cursor=conn.cursor()

#----------main-----------

def main():
    print("-----Bienvenido----------\nEste es IHealth+ su aplicacion de ejercicios!\n")
    print("Para iniciar, que desea hacer:")
    print("1. Inciciar sesion\n2. Crear una nueva cuenta\n3. Salir")
    opcion1 = input()
    if (opcion1=="1"):
        Inicio()
    if (opcion1 == "2"):
        Crearcuenta()
    if (opcion1 == "3"):
        sys.exit
    else:
        print("numero equivocado") 

#--------cuentas: inicio de sesion y creacion de las cuentas----

def Inicio():
    print("-----Inicio de sesión--------")
    print("Por favor ingrese sus datos: ")
    user=input("Ingrese su numero de usuario: ")
    password = input("Ingrese su contraseña: ")
    cursor.execute("select nombre from usuario where user_id = %s and contra = %s", (user,password))
    existe=cursor.rowcount
    if existe == 1:
        nombre=cursor.fetchone()[0]
        cursor.execute("select acc_type from usuario where user_id = %s and contra = %s", (user, password))
        acctype=cursor.fetchone()[0]
        print("Bienvenido usuario: "+nombre+" numero: "+user)
        print("Tipo de cuenta: "+acctype)
        
        if acctype == "Administrador":
            Admin()
            
        elif acctype == "Miembro":
            Miembro()
            
    else:
        print("Este cliente no esta registrado!\nRegresando al inicio:")
        main()

def Crearcuenta():
    print("Gracias por preferirnos!")
    print("Registre algunos datos: ")
    contra1 = input("Escriba una contraseña: ")
    contra2 = input("verifique la contraseña: ")
    if contra1 == contra2:
        contra = contra1
    elif contra1 !=contra2:
        print("Contraseñas diferentes...")
        Crearcuenta()
    nombre=input("Ingrese su nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = input("Ingrese edad (solo numero): ")
    altura = input("Ingrese altura (ej. 1.50): ")
    calorias = input("Cuantas calorias diarias desea quemar?: ")
    peso_act = input("Cual es su pero actual en lb? (ej. 159.2): ")
    admincontra = input("admin? (si no, de un enter): ")
    if admincontra == "admin":
        acctype = "Administrador"
    else:
        acctype = "Miembro"
    cursor.execute("insert into usuario (nombre, apellido, edad, altura, calorias, peso_act, contra, acc_type) values (%s, %s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, edad, altura, calorias, peso_act, contra, acctype))
    cursor.execute("select user_id from usuario where nombre=%s and apellido = %s",(nombre,apellido))
    user_id=cursor.fetchone()[0]
    print("cuenta creada exitosamente\nSu numero de usuario (que debe ingresar en el inicio de sesión) es: %s"%(user_id))
    print("Se le llevará al inicio de sesión")
    Inicio()

def Admin():
    print("-----Permisos de administrador consedidos------")
    print("-----Menu de administrador------")
    print("Que desea hacer?: ")
    print("1. Modificar instructores\n2. Modificar sesiones\n3. Modificar usuarios")
    opcion1=input()
    if opcion1=="1":
        print("Elija entre las opciones:")
        print("1. Agregar un instructor\n2. Modificar un instructor\n3. Dar de baja a un instructor\n4. Regresar al inicio")
        opcion2=input()
        if opcion2=="1":
            print("Ingrese los datos del instructor a agregar:")
            inst_id = input("Numero de instructor: ")
            inst_nom= input("Nombre: ")
            inst_ape=input("Apellido del instructor: ")
            cursor.execute("insert into instructor (inst_id, inst_nombre, inst_apellido) values (%s, %s, %s)", (inst_id, inst_nom, inst_ape))
            print("Instructor agregado, regresando al menu")
            Admin()
        elif opcion2 =="2":
            instcod=input("Escriba el codigo del instructor que desa modificar: ")
            cursor.execute("select inst_id from instructor where inst_id = %s", (instcod))
            hay=cursor.rowcount
            if hay == 1:
                inst_nom= input("Nombre: ")
                nuenom=input("Nuevo nombre de instructor: ")
                inst_ape=input("Apellido del instructor: ")
                nueape=input("Nuevo apellido de instructor: ")
                cursor.execute("update instructor set inst_nombre=%s where inst_nombre=%s", (nuenom,inst_nom))
                cursor.execute("update instructor set inst_apellido=%s where inst_apellido=%s", (nueape,inst_ape))
                print("Se ha cambiado exitosamente\nVolviendo al menu")
                Admin()
            else:
                print("No existe este instructor\nVolviendo al menu")
                Admin()
        elif opcion2=="3":
            instcod=input("Escriba el codigo del instructor que desa dar de baja: ")
            cursor.execute("select inst_id from instructor where inst_id = %s", (instcod))
            hay=cursor.rowcount
            if hay == 1:
                cursor.execute("delete from instructor where inst_id=%s", (instcod))
                print("Se ha dado de baja exitosamente\nVolviendo al Menu")
                Admin()
            else:
                print("No existe este instructor\nVolviendo al menu")
                Admin()

    if opcion1=="2":
        Admin()
    if opcion1=="3":
        Admin()
    if opcion1=="4":
        main()

def Miembro():
    print("Esta es una prueba")
    main()
main()



    
        