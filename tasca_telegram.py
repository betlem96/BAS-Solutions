#!/usr/bin/env python3
import requests

idBot = '6631454984:AAHaYHskd0-2_AKQQMkwaV7JvkF8gNoiWHs'
idGrupo = '5409603849'
idGrupo2 = '-4071937789'

def enviar_missatge(missatge):
    print('\nEnviant missatge: ' + str(missatge[:4096]))
    
    url = 'https://api.telegram.org/bot' + idBot + '/sendMessage'
    # print('\nURL: ' + url)

    return requests.post(url, data={'chat_id': idGrupo, 'text': missatge, 'parse_mode': 'HTML'})
    # print(response.text)  # Imprime la respuesta del servidor


def enviar_document(ruta):
    print('\n\nEnviant document: ' + ruta)
    url = 'https://api.telegram.org/bot' + idBot + '/sendDocument'

    # print('\nURL: ' + url)
    return requests.post(url, files={'document': (ruta, open(ruta, 'rb'))},
              data={'chat_id': idGrupo, 'caption': 'imagen caption'})
    # print(response.text)  # Imprime la respuesta del servidor

# enviarMensaje("Prova")
# enviarDocumento("/home/alumne/Documents/py/BAS-Solutions/tasca1_shodan.py")