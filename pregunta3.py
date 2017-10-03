import sqlite3

#Creacion de las clases
class Cine:

    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre

class Pelicula:
    def __init__(self, id, nombre, idCinesito):
        self.id=id
        self.nombre=nombre
        self.idCinesito=idCinesito

class Funcion:
    def __init__(self, id, horario, idPeli):
        self.id=id
        self.horario=horario
        self.idPeli=idPeli

class Entrada:
    def __init__(self, idEntrada, idFuncionsita):
        self.idEntrada=idEntrada
        self.idFuncionsita=idFuncionsita


#Clase gestora (cumpliendo con fachada)
class GestorDeBD:
    def __init__(self, nombreDB):
        self.nombreDB=nombreDB
        self.conn = sqlite3.connect(self.nombreDB)
        self.c=self.conn.cursor()

    def eliminarTabla(self,nombre):
        sql='DROP TABLE IF EXISTS {}'.format(nombre)
        self.c.execute(sql)
        print('Tabla Eliminada')
    def crearTablaCine(self):
        sql = 'CREATE TABLE IF NOT EXISTS cine(id INTEGER PRIMARY KEY NOT NULL, nombreCine TEXT)'
        self.c.execute(sql)
        print("Tabla creada con exito")

    def crearTablaPelicula(self):
        sql = """CREATE TABLE IF NOT EXISTS pelicula(id INTEGER PRIMARY KEY NOT NULL, nombrePeli TEXT,
        idCine INTEGER, FOREIGN KEY(idCine) REFERENCES  cine(id))"""
        self.c.execute(sql)
        print("Tabla creada con exito")

    def crearTablaFuncion(self):
        sql = """CREATE TABLE IF NOT EXISTS funcion(id INTEGER PRIMARY KEY NOT NULL, horario TEXT,
        idPelicula INTEGER, FOREIGN KEY(idPelicula) REFERENCES  pelicula(id))"""
        self.c.execute(sql)
        print("Tabla creada con exito")

    def crearTablaEntrada(self):
        sql = """CREATE TABLE IF NOT EXISTS entrada(id INTEGER PRIMARY KEY NOT NULL,
        idFuncion INTEGER, FOREIGN KEY(idFuncion) REFERENCES funcion(id))"""
        self.c.execute(sql)
        print("Tabla creada con exito")

    def insertarNuevoCine(self, id, nombre):
        sql="INSERT INTO cine VALUES(?,?)"
        self.c.execute(sql,(id,nombre))
        print("Insercion con exito")

    def insertarNuevaPelicula(self, id, nombre, id_cine):
        sql="INSERT INTO pelicula VALUES(?,?,?)"
        self.c.execute(sql,(id,nombre,id_cine))
        print("Insercion con exito")

    def insertarNuevaFuncion(self, id, horario, id_pelicula):
        sql="INSERT INTO funcion VALUES(?,?,?)"
        self.c.execute(sql, (id, horario, id_pelicula))

    def insertarNuevaEntrada(self, id, id_funcion):
        sql="INSERT INTO entrada VALUES(?,?)"
        self.c.execute(sql,(id,id_funcion))
        print("Insercion con exito")

    def verCines(self):
        lista=[]
        for fila in self.c.execute('SELECT * FROM cine'):
            lista.append(fila)
        return lista

    def verPeliculasPorCine(self, cineId):
        lista=[]
        for f in self.c.execute('SELECT * FROM pelicula where idCine=?',(cineId,)):
            lista.append(f)
        return lista

    def verFuncionesPorPelicula(self,peliculaId):
        lista=[]
        for f in self.c.execute('SELECT * FROM funcion where idPelicula=?',(peliculaId,)):
            lista.append(f)
        return lista

    def verEntradasVendidasPorFuncion(self,horarioFuncionId):
        lista=[]
        for f in self.c.execute('SELECT * FROM entrada where idFuncion=?',(horarioFuncionId,)):
            lista.append(f)
        return lista

    def buscarElementoPorId(self,Buscado):
        self.c.execute('SELECT * FROM cine WHERE id=?',(Buscado,))
        res=self.c.fetchone()
        return res


    def finalizar(self):
        self.conn.commit()
        self.conn.close()

def main():

    #Incializacion basica
    Negocio=GestorDeBD('Tarea2.bd')
    NombredelaBD=Negocio.nombreDB
    conexion=Negocio.conn
    cursor=Negocio.c

    Negocio.eliminarTabla('cine')
    Negocio.eliminarTabla('pelicula')
    Negocio.eliminarTabla('funcion')
    Negocio.eliminarTabla('entrada')

    #Crear Tablas
    Negocio.crearTablaCine()
    Negocio.crearTablaPelicula()
    Negocio.crearTablaFuncion()
    Negocio.crearTablaEntrada()

    #Obejtos e inserciones en la BD
    cs=Cine(1,'Cine Stark')
    cp=Cine(2,'Cine Planeta')


    Negocio.insertarNuevoCine(cs.id,cs.nombre)
    Negocio.insertarNuevoCine(cp.id,cp.nombre)

    pel1=Pelicula(1,'El Desparecido',1)
    pel2=Pelicula(2,'Deep el Pulpo',1)
    pel3=Pelicula(3,'IT',2)
    pel4=Pelicula(4,'La Hora Final',2)

    Negocio.insertarNuevaPelicula(pel1.id,pel1.nombre,pel1.idCinesito)
    Negocio.insertarNuevaPelicula(pel2.id,pel2.nombre,pel2.idCinesito)
    Negocio.insertarNuevaPelicula(pel3.id,pel3.nombre,pel3.idCinesito)
    Negocio.insertarNuevaPelicula(pel4.id,pel4.nombre,pel4.idCinesito)



    fu1=Funcion(1,'19:00',3)
    fu2=Funcion(2,'20:30',3)
    fu3=Funcion(3,'22:00',3)
    fu4=Funcion(4,'21:00',4)
    fu5=Funcion(5,'20:00',1)
    fu6=Funcion(6,'23:00',1)
    fu7=Funcion(7,'16:00',2)
    fu8=Funcion(8,'21:00',1)
    fu9=Funcion(9,'20:00',2)

    Negocio.insertarNuevaFuncion(fu1.id,fu1.horario,fu1.idPeli)
    Negocio.insertarNuevaFuncion(fu2.id,fu2.horario,fu2.idPeli)
    Negocio.insertarNuevaFuncion(fu3.id,fu3.horario,fu3.idPeli)
    Negocio.insertarNuevaFuncion(fu4.id,fu4.horario,fu4.idPeli)
    Negocio.insertarNuevaFuncion(fu5.id,fu5.horario,fu5.idPeli)
    Negocio.insertarNuevaFuncion(fu6.id,fu6.horario,fu6.idPeli)
    Negocio.insertarNuevaFuncion(fu7.id,fu7.horario,fu7.idPeli)
    Negocio.insertarNuevaFuncion(fu8.id,fu8.horario,fu8.idPeli)
    Negocio.insertarNuevaFuncion(fu9.id,fu9.horario,fu9.idPeli)






    terminado = False;
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            for i in Negocio.verCines():
                print(i[1] +'\n')
            print('********************')


        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            for i in Negocio.verCines():
                print(str(i[0]) +': '+ str(i[1]) +'\n')
            print('********************')
            cine = input('Primero elija un cine:')
            cineCreado=Cine(int(cine), Negocio.buscarElementoPorId(int(cine)))

            print('********************')
            for i in Negocio.verPeliculasPorCine(cineCreado.id):
                print (str(i[0]) +'. '+ str(i[1]) +'\n')
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            for i in Negocio.verCines():
                print(str(i[0]) +': '+ str(i[1]) +'\n')
            print('********************')
            cine = input('Primero elija un cine:')
            cineCreado=Cine(int(cine), Negocio.buscarElementoPorId(int(cine)))
            for i in Negocio.verPeliculasPorCine(cineCreado.id):
                print (str(i[0]) +'. '+ str(i[1]) +'\n')
            pelicula_elegida = input('Elija pelicula:')
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funci in Negocio.verFuncionesPorPelicula(int(pelicula_elegida)):
                print (str(funci[0]) +'. '+ str(funci[1]) +'\n')
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            l=[]
            for i in range(1,int(cantidad_entradas)+1):
                l.append(Entrada(i,int(funcion_elegida)))
            print('Se realizó la compra de la entrada. Código es {}'.format(len(l)))

        elif opcion == '0':
            Negocio.finalizar()
            terminado = True
        else:
            Negocio.finalizar()
            print(opcion)


if __name__=='__main__':
    main()
