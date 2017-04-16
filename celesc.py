from __future__ import print_function

import os
import urllib2
from datetime import datetime

URL = 'http://site.celesc.com.br/aplicativos/aviso_desligamento/'
RUA = os.environ['rua']  # O site recebe os todos parametros em maiusculas
CIDADE = os.environ['cidade'] # O site recebe os parametros todos em maiusculas


def validate(res):
    if 'Munic&iacute;pio' not in res:
        raise Exception('Pagina de manutencao invalida')
    return RUA not in res


def lambda_handler(event, context):
    print('Verificando {} em {}...'.format(URL, event['time']))
    try:
        request = urllib2.Request(URL, 'munic='+CIDADE)
        if not validate(urllib2.urlopen(request).read()):
            raise Exception('Rua com manutencao programada')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
