from Conexion import Conexion
from Persona import Persona
from logger_base import log
class PersonaDAO:
    '''
    DAO (DATA ACCESS OBJECT)
    CRUD (CREATE-READ-UPDATE-DELETE)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'


    #SELECCIONAR
    @classmethod
    def seleccionar(cls):
        #conecta bbdd usando with (no hace falta cerrar la BBDD)
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                #realiza consulta
                cursor.execute(cls._SELECCIONAR)
                #recuperamos los registros
                registros = cursor.fetchall()
                #lista de personas (las listas pueden contener objetos de diferentes tipos)
                personas = []
                for registro in registros: #registros devueltos a recorrer
                    #recorremos los registros
                    #recuperamos el id[0], nombre[1], apellido[2], email[3]
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    #agrega personas a la lista
                    personas.append(persona)
                return personas

    #INSERTAR
    @classmethod
    def insertar(cls, persona):
        #creamos nuestra conexión
        with Conexion.obtenerConexion() as conexion:
            #creamos el cursor
            with Conexion.obtenerCursor() as cursor:
                #tupla de valores (campos fijos, inmutable)
                valores = (persona.nombre, persona.apellido, persona.email)
                #insertamos los valores
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                #devolvemos cantidad de registros insertados
                return cursor.rowcount

    #ACTUALIZAR
    @classmethod
    def actualizar(cls, persona):
        #obtenemos nuestra conexión
        with Conexion.obtenerConexion() as conexion:
            #obtenemos el cursor
            with Conexion.obtenerCursor() as cursor:
                #tupla de valores (campos fijos, inmutable)
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                #actualizamos los valores
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                #devolvemos cantidad de registros actualizado
                return cursor.rowcount

    #ELIMINAR
    @classmethod
    def eliminar(cls, persona):
        #obtenemos nuestra conexión
        with Conexion.obtenerConexion() as conexion:
            #obtenemos el cursor
            with Conexion.obtenerCursor() as cursor:
                #solo obtenemos el valor id en la tupla para poder eliminar el registro
                valores = (persona.id_persona,)
                #actualizamos los valores
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona eliminado: {persona}')
                #devolvemos cantidad de registros eliminados
                return cursor.rowcount


if __name__ == '__main__':
    #Insertar un registro
    #persona1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertadas: {personas_insertadas}')

    #Actualizar un registro
    persona1 = Persona(1,'Juan Carlos','Juarez','cjjuarez@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    #eliminar un registro
    #especificamos el valor del campo ya que solo hay un campo
    persona1 = Persona(id_persona=20)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)