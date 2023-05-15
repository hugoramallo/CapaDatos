from logger_base import log
import psycopg2 as bd
import sys
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Nube'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    #CREAMOS LA CONEXIÓN A LA BBDD
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE
                                           )
                log.debug(f'Conexión exitosa!!!: {cls._conexion}')
                # devolvemos la conexión
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                # terminamos la conexión
                sys.exit()
        else:
            return cls._conexion
    #CREAMOS EL CURSOR PARA PODER HACER CONSULTAS EN LA BBDD
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor



if __name__ == "__main__":
    #conectamos a la BBDD
    Conexion.obtenerConexion()
    #obtenemos el cursor
    Conexion.obtenerCursor()
    #ya podemos comenzar a enviar consultas SQL
