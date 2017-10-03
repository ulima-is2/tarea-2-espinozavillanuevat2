import sys

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

#composite

class CineComposite:
    def listar_toda_pelicula(self):
        pass
    
class CineMaestro(CineComposite):
    def __init__(self):
        self.hijos = []
        
    def add_hijos(self, hijo):
        self.hijos.append(hijo)
        
    def listar_toda_pelicula(self):
        
        cad = ""
        star=[]
        for hijo in self.hijos:
            peli = hijo.listar_peliculas()
            for p in peli:
                star.append(p.nombre)

        set(star)
        for x in star:
            print(x)

        return cad
                
    

class CinePlaneta(CineComposite):
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)



class CineStark(CineComposite):
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

#factory
class cineFactory:
    def obtener_cine(self, tipo_cine):
        if tipo_cine == 'CineStark':
            return CineStark()
        elif tipo_cine == 'CinePlaneta':
            return CinePlaneta()
        else:
            return None
#fachada

def lista_cina():
    
    listita = ["Lista de cines",  "1: CinePlaneta" , "2: CineStark"]
    for l in listita:
        print(l)
   
 

def main():
    terminado = False;
#factory

    tarea2 = ['CinePlaneta','CineStark']
    cinefac = cineFactory()
    
    
#composite
    cinemaestro=CineMaestro()
    cinestark=CineStark()
    cineplaneta=CinePlaneta()

    cinemaestro.add_hijos(cinestark)
    cinemaestro.add_hijos(cineplaneta)
    
    
    
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(4) Ver todas las peliculas que hay') 
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            #fachada
            listi = lista_cina()
            print('********************')

        elif opcion == '2':
            print('********************')
            #fachada
            listi = lista_cina()
            print('********************')

            cine = input('Primero elija un cine:')
            #factory
            xd = int(cine)-1
            escine= cinefac.obtener_cine(tarea2[xd])
            peliculas = escine.listar_peliculas()

            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            #fachada
            listi = lista_cina()
            print('********************')
            cine = input('Primero elija un cine:')
            #factory
            xd = int(cine)-1
            escine= cinefac.obtener_cine(tarea2[xd])
            peliculas = escine.listar_peliculas()
            cine =cinefac.obtener_cine(tarea2[xd])


            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        #composite
        elif opcion == '4':
            tpeliculas= cinemaestro.listar_toda_pelicula()
            

        elif opcion == '0':
            terminado = True
            composite
        
        else:
            print(opcion)



if __name__ == '__main__':
    main()
