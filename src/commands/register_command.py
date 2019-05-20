import re
import app
import command_system


def register(request):

    user_id = request['message']['from']['id']
    group = re.findall(r'\d+', request['message']['text'])[-1]

    if not app.db['groups'].count_documents({'name': group}):
        return 'Invalid group number'

    app.db['users'].replace_one({'name': user_id}, {'name': user_id, 'group': group}, upsert=True)

    return 'registered'


register_command = command_system.Command()

register_command.keys = [r'/reg \d+\t*']
register_command.description = '/reg group - register your university group'
register_command.process = register
