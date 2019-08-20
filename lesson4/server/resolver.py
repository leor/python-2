from functools import reduce
from settings import INSTALLED_APPS


def get_server_actions():
    apps = list(map(
        lambda item: __import__(f'{item}.routes'),
        INSTALLED_APPS
    ))

    routes = list(map(
        lambda item: getattr(item, 'routes', None),
        apps    
    ))
    
    return reduce(
        lambda value, item: value + getattr(item, 'actionmapping', None), 
        routes,
        []
    )

def resolve(action):
    actionmapping = {
        item.get('action'): item.get('controller')
        for item in get_server_actions()
        if item
    }

    return actionmapping.get(action)