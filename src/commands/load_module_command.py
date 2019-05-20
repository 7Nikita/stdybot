import re
import app
import utility
import command_system


def load_module(request):
    user_id = request['message']['from']['id']

    module_name = re.findall(r'\w+', request['message']['text'][6:])[-1]

    if user_id == app.db['info'].find_one({'name': 'admin'})['user_id']:
        return utility.load_module(module_name)

    return 'Invalid command'


load_module_command = command_system.Command()

load_module_command.keys = [r'/load \w+\t*']
load_module_command.description = '/load - load module'
load_module_command.process = load_module
