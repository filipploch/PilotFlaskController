import requests
from config import HOST_ADRESS


def start_timer():
    requests.get(f'{HOST_ADRESS}/control-timer/1')


def stop_timer():
    requests.get(f'{HOST_ADRESS}/control-timer/0')


def reset_timer():
    requests.get(f'{HOST_ADRESS}/control-timer/2')


def get_time(countdown: bool = True):

    response = requests.get(f'{HOST_ADRESS}/matchdata')
    overall_seconds = int(response.json()['match']['seconds'])
    match_length = int(response.json()['match']['match_length'])
    hours, remainder = divmod(overall_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if countdown:
        remaining_seconds = match_length * 60 - overall_seconds
        overall_minutes = f'{int(remaining_seconds/60):02d}'
        seconds = f'{(60 - seconds):02d}'.replace("60", "00")
    else:
        overall_minutes = f'{(hours * 60 + minutes):02d}'
        seconds = f'{(seconds):02d}'
    return f'{overall_minutes}:{seconds}'


def increment_seconds(value, countdown):
    if countdown:
        requests.post(f'{HOST_ADRESS}/increment-seconds'
                      , json={'value': value * -1})
    else:
        requests.post(f'{HOST_ADRESS}/increment-seconds'
                      , json={'value': value})


