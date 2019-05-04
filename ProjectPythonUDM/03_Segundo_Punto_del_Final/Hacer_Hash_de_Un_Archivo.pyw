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


# declarando un metodo con el nombre prtu
def prtu():
	# declarando una variable con el nombre lra que ahora es una cadena vacia
	lra = ""
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
		#un archivo. En este caso todos tipos de archivos son permitidos. (por el *). Para mi este no funciona
        # puede ser un problema con el mac.
		fta = [('Todos los archivos', '.txt'), ]
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

		# la variable lra que antes era un string vacia ahora contiene la routa (como cadena) que retorna el metodo dentro ru.
        # mejor dicho contiene la routa hacia el archivo que seleccione el usario
		lra = ru
	#Si un error occure en el try-block el programa va a saltar dentro del exception-block.
	# La exception tiene ahora un alias E. Este codigo nunca va a ejecutar cuando en el try-block
	# no hay errores
	except Exception as E:
		#imprime INICIO---ERROR-------------------------- en el terminal. (pt es el alias para el metodo print())
		pt("INICIO---ERROR--------------------------")
		#Ahora imprime el error que occure
		pt(E)
		# Imprime "FIN---ERROR--------------------------" en la consola.
		pt("FIN---ERROR--------------------------")
	# un finally-block es un bloque de codigo que siempre va a ejecutar. Entonces
	# el codigo retorna la routa eligido del usario como cadena, o, si hay errores, una cadena vacia
	finally:
		return lra


#declarando un metodo con el nombre md5ha, cual, recibe un argumento. Este argumento es obligatorio
def md5ha(ram5):
    #de la libreria hashlib importa el metodo md5 (que es para crear hashes seguros) con el alias m
    from hashlib import md5 as m
    # la variable tth esta asignado una cadena vacia
    tth = ""
    ## la variable gh esta asignado el metodo m(), significa el metodo md5() para crear un hash seguro
    gh = m()
    # abre un archivo ram5 (cuando uno llama la funcion tiene que pasar el archivo como argumento), y lo lee en bytes.
    a = open(ram5,"rb")
    # lee el contenido del archivo en 2048 bytes.
    bloque = a.read(2048)
    #este bucle hace lo seguiente: Sigue leyendo en 2048 bytes el archivo
    #hasta no hay mas de leer. Es decir lee que lee el archivo completo
    #en bytes. Siempre, despues habia leido 2048 bytes, llama
    # el metodo m().update, significa md5.update Eso hace un update del hash que esta creando
    # con el nuevo contenido y transorma el contenido en un hash-string
    # Despues cierre el archivo con el metodo close(). Despues este bucle
    # el archivo completo, o mejor dicho el contenido del archivo es un hash-string.
    while bloque:
        gh.update(bloque)
        bloque = a.read(2048)
    a.close()
    ## hexdigest() esta creando un hex-valor del md5 hash-string. Sin este metodo
    # el md5 hash seria algo como <md5 HASH object @ 0x10eca64e0>. Llamando este
    #metodo lo transforma en algo como 41a695256e70813cf8c32bc677149ffe que es
    #un hex-valor del hash-string
    return  gh.hexdigest()

## declarando un metodo hha sin argumentos
def hha():
    # esta importando el metodo messagebox de la libreria tkinter y esta poniendo un alias msg para ahorrar codigo
    from tkinter import messagebox as msg
    # La variable rda esta asignado a el metodo prtu de anterior, que retorna una cadena vacia o una ventana la ventana con toda la informacion
    # del metodo que he comentado antes
    rda = prtu()
    ## el metodo path.basename('una/routa') retorna la cola de un path. Por ejemplo path.basename('una/routa/un_archivo.txt')
    # retornaria 'un_archivo.txt'. Aca path.basename recibe como argumento la routa que eligi el usario cuando
    # el metodo prtu() esta llamado. O, si hay errores en el metodo prtu, una cadena vacia.
    ## Entonces dentro nar guardamos la cola de esta routa. El archivo que eligio el usario
    nar = p.basename(p.realpath(rda))
    #esta imprimiendo la routa hacia el archivo que eligio el usario dentro simple comillas. O solo simple comillas (si habian errores)
    pt("'"+rda+"'")
    ## en la variable hx esta guardado el resultado de metodo md5ha con el argumento rda. El argumento rda, como
    # ya he explicado, es una cadena.
    ## Esa cadena esta transformado en un hashstring, algo como 41a695256e70813cf8c32bc677149ffe. Ahora hx es igual a este hashstring
    hx = md5ha(rda)
    ## Imprime el hashstring en la consola
    pt(hx)
    ## En la variable rdh que esta declarado, se guarda el resultado del metodo cdsp. El resultado del metodo
    # cdsp es una cadena de la routa hacia la carpeta donde esta ubicado el archivo
    rdh = cdsp()
    ## Aca estamos concatenando a la routa que contiene la variable rdh, el symbolo / (con el metodo p.sep).
    # Despues estamos concatenando el archivo que eligio el usario. Puede ser algo como
    # /Users/micromegas/Desktop/ProjectPythonUDM/03_Segundo__Punto_del_Final/test.txt
    rdh += p.sep + nar
    ## A la cadena ahora estamos concatenando la cadena md5sum.txt. Efectivamente cambiamos el nombre del archivo.
    # Puede ser algo como  '/Users/micromegas/Desktop/ProjectPythonUDM/03_Segundo__Punto_del_Final/test.txt__md5sum.txt'
    rdh += "__md5sum.txt"
    ## Imprime la routa (la cadena que es la routa)
    pt(rdh)
    ## Abre el archivo que se encuentre en la routa rdh. Por ejemplo abre
    # test.txt__md5sum.txt de la routa '/Users/micromegas/Desktop/ProjectPythonUDM/03_Segundo__Punto_del_Final/test.txt__md5sum.txt'
    ## en el modo escrito. Si no existe el archivo lo esta creando.
    a = open(rdh,"w")
    # en la variable declarado linea, se guarda el hashstring que esta guardado en la variable hx, mas dos espacios mas
    ## la routa hacia el archivo que eligio el usario
    linea = hx + "  " + nar
    ## Escribe el hashstring que esta guardado en la variable hx, mas dos espacios mas
    ## la routa hacia el archivo que eligio el usario en el archivo
    a.write(linea)
    ## Cierre el archivo
    a.close()
    ## Abre una ventana que dice como titulo TERMINE y como contenido la routa hasta el archivo. Por ejemplo
    # TERMINE /Users/micromegas/Desktop/ProjectPythonUDM/03_Segundo__Punto_del_Final/test.txt__md5sum.txt
    msg.showinfo("TERMINE",rdh)

## Esta declarando un metodo pp() que tiene la unica funcion en llamar el metodo hha()
def pp():
    ## llama el metodo hha()
    hha()

## Este sintaxis siginifica que corre el script solo si no es importado pero el 'main entry point' del programa.
# O mejor dicho este script NO va a correr si esta importado en otro script.
if __name__ == "__main__":
    pp()
