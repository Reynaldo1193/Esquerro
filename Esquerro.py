import mysql.connector
from mysql.connector import errorcode

class Usuario(object):
    """docstring for Usuario."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def Menu():
    print("\t\t\t MENU")
    print("Que deseas hacer: ")
    print("1.Insertar un Usuario ")
    print("2.Replicar una base de datos \n")

    opcion = int(input(""))

    if opcion == 1 :
        usuario = PedirUsuario();

        if usuario.edad>30:
            Distribuir(cnx2,usuario)
        else :
            Distribuir(cnx,usuario)
    elif opcion == 2:
        print("\t\t REPLICAR UNA BASE DE DATOS")
        print("Que base de datos desea replicar")
        print("1.Edad menor o igual a 30 años ")
        print("2.Edad mayor a 30 años ")

        condition = int(input(""))

        if condition == 1:
            Replica(cnx)
        elif condition == 2:
            Replica(cnx2)
        else:
            print("Esa no es una base de Datos Valida")
    else:
        print("Esa no es una opcion Valida")



def PedirUsuario():
    print("\t\tINSERTAR USUARIO")
    nombre = str( input("Nombre del usuario: "))
    edad = int (input("Edad del usuario: "))
    return Usuario(nombre,edad)



def Distribuir(cnx,usuario):
    print("nombre: "+usuario.nombre+"\nedad: "+str(usuario.edad))
    cursor = cnx.cursor()
    addUsuario = ("INSERT INTO usuario  (id, nombre, edad) VALUES (%s, %s, %s)")
    dataUsuario = ("0",usuario.nombre,str(usuario.edad));

    try:
        cursor.execute(addUsuario, dataUsuario)
        #ultimoUsuario = cursor.lastrowid
        cnx.commit()
        pass
    except Exception as e:
        print(e)

    cursor.close()



def Replica(cnx):
    cursor = cnx.cursor()
    selectQ = ("Select max(id) From replica")

    cursor.execute(selectQ)
    for (id) in cursor:
        idV = id
        print("id :"+str(idV[0]))
    replicQ = ("INSERT INTO replica (id,nombre,edad) Select * From usuario u1 Where u1.id > %s")

    try:
        cursor.execute(replicQ, (idV[0],))
        print("Se ah replicado la base de datos")
        cnx.commit()
        pass
    except Exception as e:
        if e.errno == errorcode.ER_DUP_ENTRY:
            print("No hay datos para replicar")
        else:
            print(e)

    cursor.close()


    print("Hello From Replicaaaaaaaa")

try:
    cnx = mysql.connector.connect(user='armando',password='n0m3l0',host='54.81.81.169',database="Esquerro")
    cnx2 = mysql.connector.connect(user='rey',password='n0m3l0',host='54.167.126.234',database="Esquerro")
    pass
except mysql.connector.Error as err:
    print(err)

Menu()


cnx.close()
cnx2.close()
