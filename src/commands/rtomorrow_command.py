import app
import schedule_tools
import command_system


def rtomorrow_schedule(request):

    user_id = request['message']['from']['id']
    group = app.db['users'].find_one({'name': user_id})['group']

    cur_day = (app.db['info'].find_one({'name': 'current_day'})['day'] + 1) % 7
    cur_week = (app.db['info'].find_one({'name': 'current_week'})['week'] + (cur_day == 0)) % 4 + (cur_day == 0)

    return schedule_tools.get_schedule(group, cur_day, cur_week)


rtomorrow_schedule_command = command_system.Command()

rtomorrow_schedule_command.keys = [r'/tomorrow\t*']
rtomorrow_schedule_command.description = '/tomorrow - getting tomorrow schedule by your group'
rtomorrow_schedule_command.process = rtomorrow_schedule
