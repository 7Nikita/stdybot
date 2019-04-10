import re
import requests
import command_system


days = {
    '1': 'Понедельник',
    '2': 'Вторник',
    '3': 'Среда',
    '4': 'Четверг',
    '5': 'Пятница',
    '6': 'Суббота',
    '7': 'Воскресенье'
}


def get_group_schedule(request):

    group, day = re.findall(r'\d+', request['message']['text'])

    groups = requests.get('https://journal.bsuir.by/api/v1/groups').json()
    flag = any([group == i['name'] for i in groups])

    if not flag:
        return 'Invalid group number'

    cur_day = days[day]
    cur_week = requests.get('http://journal.bsuir.by/api/v1/week').json()

    url = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup={}'.format(group)
    r = requests.get(url).json()

    ans = ''

    for day in r['schedules']:
        if day['weekDay'] == cur_day:
            for subject in day['schedule']:
                if cur_week in subject['weekNumber']:
                    ans += '{} ({}) {} {} {}\n'.format(
                        subject['subject'],
                        subject['lessonType'],
                        subject['auditory'],
                        subject['numSubgroup'],
                        subject['lessonTime']
                    )

    return ans if ans else 'There are no subjects on this day'


group_schedule_command = command_system.Command()

group_schedule_command.keys = [r'/group_schedule \d+ \d+']
group_schedule_command.description = 'getting schedule by group and day number'
group_schedule_command.process = get_group_schedule
