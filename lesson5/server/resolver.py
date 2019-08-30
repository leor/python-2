from functools import reduce
from decorators import log


@log('%(name)s%(args)s - %(result)s')
def get_server_actions(installed):
    apps = list(map(
        lambda item: __import__(f'{item}.routes'),
        installed
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

@log('%(name)s%(args)s - %(result)s')
def resolve(action, installed):
    sa = get_server_actions(installed)
    print(sa)

    actionmapping = {
        item.get('action'): item.get('controller')
        for item in sa
        if item
    }

    return actionmapping.get(action)