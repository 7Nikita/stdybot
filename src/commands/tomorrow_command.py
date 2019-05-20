import re
import app
import schedule_tools
import command_system


def tomorrow_schedule(request):

    group = re.findall(r'\d+', request['message']['text'])[-1]

    if not app.db['groups'].count_documents({'name': group}):
        return 'Invalid group number'

    cur_day = (app.db['info'].find_one({'name': 'current_day'})['day'] + 1) % 7
    cur_week = (app.db['info'].find_one({'name': 'current_week'})['week'] + (cur_day == 0)) % 4 + (cur_day == 0)

    return schedule_tools.get_schedule(group, cur_day, cur_week)


tomorrow_schedule_command = command_system.Command()

tomorrow_schedule_command.keys = [r'/tomorrow \d+\t*']
tomorrow_schedule_command.description = '/tomorrow group - getting tomorrow schedule by group'
tomorrow_schedule_command.process = tomorrow_schedule
