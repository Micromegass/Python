from random import randint as ra

a = open("simulados.csv","w",encoding='ISO-8859-1')
a.write("idciudad;idproducto;idcantidad\n")
for i in range(5000):
      linea  = ""
      linea += str(ra(1,10)) + ";"
      linea += str(ra(1,20)) + ";"
      linea += str(ra(1,30)) + "\n"
      a.write(linea)
a.close()


## generate a libro de excel for every city
# every city has


## read every line
## split the info
## every city into a new csv files


##resumen de los productos
