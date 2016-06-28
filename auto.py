import os
import sys
import json
import time


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_PATH = os.path.join(PROJECT_PATH, 'auto.log')
DATA_PATH = os.path.join(PROJECT_PATH, 'data.json')
try:
    DATA_DICT = json.loads(open(DATA_PATH, "r").read())
except:
    DATA_DICT = {}


def save_data():
    with open(DATA_PATH, 'w') as data_file:
        data_file.write(json.dumps(DATA_DICT))


def _log(msg):
    with open(LOG_PATH, 'a') as log_file:
        log_file.write(msg + '\n')


def auto(to_sn, msg):
    _log('sn: {}'.format(to_sn))
    _log('sn: {}'.format(to_sn))
    now = int(time.time())
    last_time = DATA_DICT.get(to_sn)
    send_auto_response = False
    if (not last_time) or ((now - last_time) > (60*60*12)):
        send_auto_response = True
        DATA_DICT[to_sn] = now
        save_data()
    if send_auto_response:
        print 1
    else:
        print 0
    return send_auto_response


if __name__ == '__main__':
    _log('++ running auto.py')
    auto(to_sn=sys.argv[1], msg='')