class MiExcepcion(Exception):
    def __init__(self, error):
        print(f'Cometiste el siguiente error: {error}')

try:
    raise MiExcepcion('Excepción personalizada')
except:
    print('Me ejecuto porque he lanzado una excepción')