import json


def exchange(user, borrower, amount):
    try:
        owes = user['owes'][borrower]
    except:
        owes = 0
    try:
        owed_by = user['owed_by'][borrower]
    except:
        owed_by = 0
    new_owes = owes - owed_by - amount
    if new_owes > 0:
        user['owes'][borrower] = new_owes
        try:
            user['owed_by'].pop(borrower)
        except:
            pass
    elif new_owes < 0:
        try:
            user['owes'].pop(borrower)
        except:
            pass
        user['owed_by'][borrower] = -new_owes
    else:
        try:
            user['owes'].pop(borrower)
        except:
            pass
        try:
            user['owed_by'].pop(borrower)
        except:
            pass
    user['balance'] = (sum(v for v in user['owed_by'].values()) -
                       sum(v for v in user['owes'].values()))
    return user


class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        database = self.database
        if payload:
            load = json.loads(payload)
            database['users'] = list(filter(lambda user: user['name']
                                     in load['users'], database['users']))
        return json.dumps(database)

    def post(self, url, payload=None):
        load = json.loads(payload)
        if url == '/add':
            new_user = {'name': load['user'],
                        'owes': {},
                        'owed_by': {},
                        'balance': 0}
            return json.dumps(new_user)
        elif url == '/iou':
            users = self.database['users']
            lender = list(filter(lambda x: x['name'] == load['lender'],
                                 users))[0]
            borrower = list(filter(lambda x: x['name'] == load['borrower'],
                                   users))[0]
            iou_users = [exchange(lender,
                                  load['borrower'],
                                  load['amount']),
                         exchange(borrower,
                                  load['lender'],
                                  -load['amount'])]
            return json.dumps({'users': sorted(iou_users,
                                               key=lambda d: d['name'])})
