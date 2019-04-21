import re
import app
import utility
import command_system


def unload_module(request):
    user_id = request['message']['from']['id']

    module_name = re.findall(r'\w+', request['message']['text'])[-1][8:]

    if user_id == app.db['info'].find_one({'name': 'admin'})['user_id']:
        return utility.unload_module(module_name)

    return 'Invalid command'


unload_module_command = command_system.Command()

unload_module_command.keys = [r'/unload \w+\t*']
unload_module_command.description = 'unload module'
unload_module_command.process = unload_module
