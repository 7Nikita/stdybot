import app
import time
import requests
import datetime


def update_information():

    while True:
        current_day = datetime.datetime.now().weekday()
        app.db['info'].replace_one({'name': 'current_day'}, {'name': 'current_day', 'day': current_day}, upsert=True)

        current_week = requests.get('http://journal.bsuir.by/api/v1/week').json()
        app.db['info'].replace_one({'name': 'current_week'}, {'name': 'current_week', 'week': current_week}, upsert=True)

        # update_groups()
        update_schedules()

        time.sleep(60 * 60)


def update_groups():
    current_groups = [group['name'] for group in requests.get('https://journal.bsuir.by/api/v1/groups').json()]
    return current_groups


def update_schedules():
    update_request = 'https://journal.bsuir.by/api/v1/studentGroup/lastUpdateDate?studentGroup='
    group_schedule_request = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup='

    for group in app.db['groups'].find({}):
        group_number = group['name']

        try:
            group_last_update = requests.get(update_request + group_number).json()['lastUpdateDate']
        except:
            continue

        if not (app.db['schedules'].count_documents({'name': group_number})
                and app.db['schedules'].find_one({'name': group_number})['last_update'] == group_last_update):
            try:
                sch = requests.get(group_schedule_request + group_number).json()
                upd = requests.get(update_request + group_number).json()
                app.db['schedules'].replace_one({'name': group_number},
                                            {'name': group_number,
                                             'schedule': sch['schedules'],
                                             'last_update': upd['lastUpdateDate']},
                                            upsert=True)
            except:
                continue
