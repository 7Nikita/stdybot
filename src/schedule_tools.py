import app


days = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье'
}


def get_schedule(group, cur_day, week):

    if not app.db['groups'].count_documents({'name': group}):
        return 'Invalid group number'

    ans = ''

    cur_day = days[cur_day]

    for day in app.db['schedules'].find_one({'name': group})['schedule']:
        if day['weekDay'] == cur_day:
            for subject in day['schedule']:
                if week in subject['weekNumber']:
                    ans += '{} ({}) {} {} {}\n'.format(
                        subject['subject'],
                        subject['lessonType'],
                        subject['auditory'],
                        subject['numSubgroup'],
                        subject['lessonTime']
                    )

    return ans if ans else 'There are no subjects on this day'
