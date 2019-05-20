import re
import app
import schedule_tools
import command_system


def today_schedule(request):

    group = re.findall(r'\d+', request['message']['text'])[-1]

    if not app.db['groups'].count_documents({'name': group}):
        return 'Invalid group number'

    cur_day = app.db['info'].find_one({'name': 'current_day'})['day']
    cur_week = app.db['info'].find_one({'name': 'current_week'})['week']

    return schedule_tools.get_schedule(group, cur_day, cur_week)


today_schedule_command = command_system.Command()

today_schedule_command.keys = [r'/today \d+\t*']
today_schedule_command.description = '/today group - getting today schedule by group'
today_schedule_command.process = today_schedule
