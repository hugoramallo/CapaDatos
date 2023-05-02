import logging as log

#niveles de logging, usamos parametros posicionales y en el medio llamamos a la función
log.basicConfig(level = log.DEBUG,
                format = '%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)s] %(message)s',
                datefmt = '%i:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])


#si se ejecuta desde esta clase...
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mesanje a nivel de error')
    log.critical('Mesanje a nivel crítico')

