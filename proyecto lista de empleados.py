#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERÍAS NECESARIAS.
from array import array
from tkinter import *
import os
from setuptools import Command
import mysql.connector
#base de datos
def conexion_base_de_datos():
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
    cursor = conexion.cursor()
     # tabla datosP Rut	nombre	apellido	sexo	direccion	telefono
    cursor.execute("CREATE TABLE IF NOT EXISTS datos_personales(rut INT(10) NOT NULL PRIMARY KEY, clave VARCHAR(45),nombre VARCHAR(45),apellido VARCHAR(45),sexo VARCHAR(10),direccion VARCHAR(45),telefono VARCHAR(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS cargas_Familiares(rut_carga INT(10) NOT NULL PRIMARY KEY,nombre_carga VARCHAR(45),apellido_carga VARCHAR(45),parentezco VARCHAR(10),direccion VARCHAR(45),telefono VARCHAR(10),sexo VARCHAR(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS datos_laborales(id_datosL INT(10) NOT NULL PRIMARY KEY,cargo VARCHAR(45),fecha_ingreso date,area_perteneciente VARCHAR(40),departamento_perteneciente VARCHAR(45))")
    cursor.execute("CREATE TABLE IF NOT EXISTS contacto_emergencia(rut_contacto INT(10) NOT NULL PRIMARY KEY,nombre_contacto VARCHAR(45),apellido_contacto VARCHAR(45),sexo VARCHAR(10),relacion_con_trabajador VARCHAR(45),telefono VARCHAR(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS rol(id INT(10) NOT NULL PRIMARY KEY,rol VARCHAR(45))")
    cursor.execute("CREATE TABLE IF NOT EXISTS perfil(id INT(10) NOT NULL PRIMARY KEY,permisos varchar(45))")
    cursor.execute("CREATE TABLE IF NOT EXISTS formulario(id INT(10) NOT NULL PRIMARY KEY,rut_datosP int(10) NOT NULL,CONSTRAINT fk_dp FOREIGN KEY (rut_datosP) REFERENCES datos_personales(rut),rut_carga int(10) NOT NULL, CONSTRAINT fk_cf FOREIGN KEY (rut_carga) REFERENCES cargas_familiares(rut_carga),rut_contacto int(10) NOT NULL,CONSTRAINT fk_contacto FOREIGN KEY (rut_contacto) REFERENCES contacto_emergencia(rut_contacto),id_perfil int(10) NOT NULL,CONSTRAINT fk_idp FOREIGN KEY (id_perfil) REFERENCES perfil(id),id_datosL int(10) NOT NULL,CONSTRAINT fk_dL FOREIGN KEY (id_datosL) REFERENCES datos_laborales(id_datosL))")
    conexion.commit()
    conexion.close()

def insertar_bd():
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="empleados")
    cursor = conexion.cursor()
  #  print("esta es la opcion", opcion)
    #if opcion=="registro": 
    cursor.execute("INSERT INTO datos_personales(rut,clave,nombre,apellido,sexo,direccion,telefono) VALUES(%s,%s,%s,%s,%s,%s,%s)",(rut.get(),clave.get(),nombre_usuario.get(),apellido.get(),sexo.get(),direccion.get(),telefono.get()))
    #if opcion=="carga":
     #   cursor.execute("")
    conexion.commit()
    conexion.close()

def Ventana_modificar_datos():
    global ventana_modificar_datos
    ventana_modificar_datos = Toplevel(ventana_inicio)
    ventana_modificar_datos.title("Modificar datos")
    ventana_modificar_datos.geometry("300x250")
    Label(ventana_modificar_datos, text="Modificar datos").pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar datos", command=modificar_datos_personales).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar cargas familiares", command=modificar_cargas_familiares).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar contacto emergencia", command=modificar_contacto_emergencia).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar datos laborales", command=modificar_datos_laborales).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar rol", command=modificar_rol).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar perfil", command=modificar_perfil).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Modificar formulario", command=modificar_formulario).pack()
    Label(ventana_modificar_datos, text="").pack()
    Button(ventana_modificar_datos, text="Volver", command=ventana_inicio).pack()


#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
   # modificar_datos()
    conexion_base_de_datos()
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Inicio de sesion")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()



#CREAMOS VENTANA PARA REGISTRO.
def registro():
    ventana_principal.withdraw()
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x550")

    usuarios = []
    global nombre_usuario
    global apellido
    global sexo
    global direccion
    global telefono
    global clave
    global rut

    global entrada_nombre
    global entrada_clave
    global entrada_rut
    global entrada_apellido
    global entrada_sexo
    global entrada_direccion
    global entrada_telefono

    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
    rut = IntVar() #DECLARAMOS "int" COMO TIPO DE DATO PARA "rut"
    apellido = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "apellido"
    sexo = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "sexo"
    direccion = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "direccion"
    telefono = StringVar() #DECLARAMOS "STRING" COMO TIPO DE DATO PARA "telefono"

    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()

    etiqueta_apellido=Label(ventana_registro, text="Apellido * ")
    etiqueta_apellido.pack()
    entrada_apellido=Entry(ventana_registro, textvariable=apellido)
    entrada_apellido.pack()


    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()

    etiqueta_rut=Label(ventana_registro, text="Rut * ")
    etiqueta_rut.pack()
    entrada_rut=Entry(ventana_registro, textvariable=rut)
    entrada_rut.pack()

    etiqueta_sexo=Label(ventana_registro, text="Sexo * ")
    etiqueta_sexo.pack()
    entrada_sexo=Entry(ventana_registro, textvariable=sexo)
    entrada_sexo.pack()

    etiqueta_direccion=Label(ventana_registro, text="Dirección * ")
    etiqueta_direccion.pack()
    entrada_direccion=Entry(ventana_registro, textvariable=direccion)
    entrada_direccion.pack()

    etiqueta_telefono=Label(ventana_registro, text="Teléfono * ")
    etiqueta_telefono.pack()
    entrada_telefono=Entry(ventana_registro, textvariable=telefono)
    entrada_telefono.pack()

    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = insertar_bd).pack() #BOTÓN "Registrarse"
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Volver", width=10, height=1, bg="LightGreen", command = ventana_registro.withdraw).pack() #BOTÓN "Volver al menu"
#CREAMOS VENTANA PARA LOGIN.

def login():
    ventana_principal.withdraw()
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 

ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.

