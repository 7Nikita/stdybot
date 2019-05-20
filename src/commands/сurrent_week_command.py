import app
import command_system


def get_week(request):
    return app.db['info'].find_one({'name': 'current_week'})['week']


get_week_command = command_system.Command()

get_week_command.keys = [r'/week']
get_week_command.description = '/week - get current week'
get_week_command.process = get_week
