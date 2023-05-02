#Conexion
import pyscopg2 as bd
class conexion:
    DATABASE = 'test_db'
    USERNAME = 'postgres'
    PASSWORD = 'Nube'
    DB_PORT = '5432'
    HOST = '127.0.0.1'
    conexion = bd.connect()
    cursor = bd.cursor()

    @classmethod
    def obtenerConexion(cls):
        conexion = bd.connect(user='postgres', password='Nube', host='127.0.0.1', port='5432', database='test_db')

    @classmethod
    def obtenerCursor(cls):
        return

    @classmethod
    def cerrar(cls):
        return







conexion = psycopg2.connect(
    user = 'postgres',
    password = 'Nube',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por comas): ')
            #tupla de tuplas
            valores = (tuple(entrada.split(',')),)
            #ejecutamos
            cursor.executemany(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
#si hay excepción la reporta
except Exception as e:
    #imprimo excepción
    print(f'Ocurrió un error {e}')
finally:
    #cerramos conexión
    conexion.close()





conexion = bd.connect(user='postgres', password='Nube', host='127.0.0.1', port='5432', database='test_db')

try:
    #autocommit en false es que no se guarden los cambios de manera automática
    #para hacerlo tenemos que hacer commit al terminar la sentencia
    #conexion.autocommit = False #este es el valor por defecto
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            #ejecutamos sentencia
            cursor.execute(sentencia, valores)
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona =%s'
            valores = ('Juan', 'Perez', 'jperez@mail.com',1 )
            #recordar que el cursor siempre es necesario para ejecutar la sentencia
            cursor.execute(sentencia, valores)
            #grabamos los datos en la BBDD, lo ideal es usar o with o este modo sin autocommit
            conexion.commit()
            print('Termina la transacción, se hizo commit')
except Exception as e:
    #imprimo excepción
    #si hay excepción, hacemos rollback, volvemos al principio del proceso
    #para que no haya rollback tienen que ejecutarse toda slas sentencias
    #conexion.rollback()
    #with hace el rollback de manera automática
    print(f'Ocurrió un error, se hizo rollback {e}')
finally:
    #cerramos conexión
    conexion.close()
