from .controllers import time_controller, formated_date_controller


actionmapping = [
    {'action': 'time:time', 'controller': time_controller}, 
    {'action': 'time:formatted', 'controller': formated_date_controller}, 
]