import re
import app
import utility
import command_system


def reload_module(request):
    user_id = request['message']['from']['id']

    module_name = re.findall(r'\w+', request['message']['text'][8:])[-1]

    if user_id == app.db['info'].find_one({'name': 'admin'})['user_id']:
        return utility.reload_module(module_name)

    return 'Invalid command'


reload_module_command = command_system.Command()

reload_module_command.keys = [r'/reload \w+\t*']
reload_module_command.description = '/reload - reload module'
reload_module_command.process = reload_module
