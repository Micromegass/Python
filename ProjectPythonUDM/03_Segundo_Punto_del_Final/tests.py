def write_file(rdh):
	a = open(rdh, "w")
	rdh.write("Me creas si no existe?")
	a.close()


write_file("test2.txt")



def md5ha(ram5):
    #de la libreria hashlib importa el metodo md5 (que es para crear hashes seguros) con el alias m
    from hashlib import md5 as m
    # la variable tth esta asignado una cadena vacia
    tth = ""
    ## la variable gh esta asignado el metodo m(), significa el metodo md5() para crear un hash sesguro
    gh = m()
    # abre un archivo ram5, y si no existe lo esta creando, y lo lee en bytes
    a = open(ram5,"rb")
    # lee
    bloque = a.read(2048)
    while bloque:
        gh.update(bloque)
        bloque = a.read(2048)
    a.close()
    ## hexdigest() esta creando un hex-valor del md5 hash-string
    print(gh.hexdigest())
    return  gh.hexdigest()


# md5ha('test.txt')


# -*- coding: utf-8 -*-
# esta importando el paquete 'path' de la libreria os y dando un alias p
from os import path as p

# esta dando un alias pt al metodo nativo print de python (para confundir y para ahorrar codigo)
pt = print


# declarando un metodo con el nombre cdsp
def cdsp():
	# primero el p.realpath(__file__) retorna la routa hacia el archivo. La notacion __file__
	# segura que funciona en todas las sistemas operativas. En mi caso retornaria por ejemplo
	# / Users/micromegas/Desktop/ProjectPythonUDM/03Segundo_Punto_del_Final/Hacer_hash_de_un_archivo.
	# Despues llama el metodo dirname de esta routa. Entonces retorna el path hacia
	# la carpeta en cual esta ubicada el archivo.
	# En mi caso por ejemplo / Users/micromegas/Desktop/ProjectPythonUDM/03Segundo_Punto_del_Final
	return p.dirname(p.realpath(__file__))



def prtu():
	# declarando una variable con el nombre lra que ahora es una cadena vacia
	lra = "mistale"
	# decalarano un try-block. El programa va a probar el codigo dentro del try-block.
	# si sirve bien, si no sirve el codigo va a controlar el error y ejecuta el codigo
	# en el except-statement.
	try:
		# de la libreria Tkinter esta importando el interface Tk y da un alias t
		# tambien de la libreria tkinter esta importando el metodo filedialog y da un alias fd.
		from tkinter import Tk as t, filedialog as fd
		#el variable v esta declarado como el metodo t(). Significa el metodo Tk(). El metodo Tk() esta
		#creando la ventana principal
		v = t()
		#es necesario para no tener inconvenientes por ejemplo que muestra el terminal
		v.withdraw()
		#la variable fta esta declarado con una list que tiene un tuple dentro. Asi se puede
		#eligir los tipos de archivos que se permite cuando mas tarde el usario va a selecionar
		#un archivo. En este caso todos tipos de archivos son permitidos. (por el *)
		fta = [
			('All files', '.*'),
		]

		#la variable titulo contiene el titulo de la ventana.
		titulo = 'Por Favor Seleccione el Archivo, al que se le calculara el hash md5'
		#se llama el metodo cdsp() que se declaro antes. La variable cds ahora contiene la
		#routa hacia el archivo donde el archivo esta ubicado.
		cds = cdsp()
		#la variable ru esta declarado. Contiene el metodo fd.askopenfilename(). Este metodo
		#abre ahora una ventana. El ventana esta creado con parent=v, en cual v es el metodo
		#Tk(). Esta ventana se abre con la direccion cds, signigica con cdsp, significa con
		#la routa en cual esta ubicado el archivo (Hacer_Hash....). Se abre alla por el argumento
		#initialdir=cds. El titulo de la ventana es la variable titulo y se puede eligir todos
		#los archivos que uno desea por filetypes=fta.
		ru = fd.askopenfilename(parent=v,
		                        initialdir=cds,
		                        title=titulo,
		                        filetypes=fta)
		print(ru)

		# la variable lra que antes era un string vacia ahora contiene la routa (como cadena) que retorna el metodo dentro ru.
		lra = ru
	#Si un error occure en el try-block el programa va a saltar dentro del exception-block.
	# La exception tiene ahora un alias E. Este codigo nunca va a ejecutar cuando en el try-block
	# no hay errores
	except Exception as E:
		#imprime INICIO---ERROR-------------------------- en el terminal. (pt es el alias para el metodo print())
		print("INICIO---ERROR--------------------------")
		#Ahora imprime el error que occure
		print(E)
		# Imprime "FIN---ERROR--------------------------" en la consola.
		print("FIN---ERROR--------------------------")
	# un finally-block es un bloque de codigo que siempre va a ejecutar. Entonces
	# el codigo retorna la routa , o, si hay errores, una cadena vacia
	finally:
		print(lra)
		return lra


prtu()


