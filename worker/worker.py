import redis
import json
from time import sleep
from random import randint


if __name__ == '__main__':
    print('Aguardando mensagens...')
    r = redis.Redis(host='queue', port=6379, db=0)

    while True:
        print('Ouvindo mensagem')
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulando envio de email...
        print('Mandando a mensagem: ', mensagem['assunto'])
        sleep(randint(5, 20))
        print('Mensagem', mensagem['assunto'], 'enviada')
