import app
import schedule_tools
import command_system


def rtoday_schedule(request):

    user_id = request['message']['from']['id']
    group = app.db['users'].find_one({'name': user_id})['group']

    cur_day = app.db['info'].find_one({'name': 'current_day'})['day']
    cur_week = app.db['info'].find_one({'name': 'current_week'})['week']

    return schedule_tools.get_schedule(group, cur_day, cur_week)


rtoday_schedule_command = command_system.Command()

rtoday_schedule_command.keys = [r'/today\t*']
rtoday_schedule_command.description = '/today - getting today schedule by your group'
rtoday_schedule_command.process = rtoday_schedule
