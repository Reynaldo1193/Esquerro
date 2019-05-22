import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='armando',password='n0m3l0',host='54.81.81.169',database="Esquerro")
    cnx2 = mysql.connector.connect(user='rey',password='n0m3l0',host='54.167.126.234',database="Esquerro")
    pass
except mysql.connector.Error as err:
    print(err)


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

    opcion = input()

    switch


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
    no_usuario = str(cursor.lastrowid)
    replicQ = ("INSERT INTO replica (id,nombre,edad) Select * From usuario u1 Where u1.id > %s")

    try:
        cursor.execute(replicQ, (no_usuario,))
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

# usuario = PedirUsuario();
#
# if usuario.edad>30:
#     Distribuir(cnx2,usuario)
# else :
#     Distribuir(cnx,usuario)

#Replica(cnx2)


cnx.close()
cnx2.close()
