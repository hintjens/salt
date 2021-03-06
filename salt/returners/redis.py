'''
Return data to a redis server
This is a VERY simple example for pushing data to a redis server and is not
nessisarily intended as a usable interface.
'''

import redis as redispy

__opts__ = {
            'redis.host': 'mcp',
            'redis.port': 6379,
            'redis.db': '0',
           }

def returner(ret):
    '''
    Return data to a redis data store
    '''
    serv = redispy.Redis(
            host=__opts__['redis.host'],
            port=__opts__['redis.port'],
            db=__opts__['redis.db'])
    serv.set(ret['id'] + ':' + red['jid'], str(ret['return']))
