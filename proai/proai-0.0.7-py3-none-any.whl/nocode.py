import copy
import logging
import sys
import time

import pandas as pd
import requests
from tqdm import tqdm


log = logging.getLogger(__name__)


def load_env(filepath='.env'):
    with open(filepath) as fin:
        lines = fin.readlines()
    var_values = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            name, value = line.split('=')
            name, value = name.strip().upper(), value.strip()
            value = value[1:-1] if value[0] in '"\'' and value[-1] == value[0] else value
        except ValueError:
            name, value = None, None
        if name and value:
            var_values[name.upper().strip()] = value
    return var_values


def load_manychat_answers(filepath='data/answers_613364286.csv'):
    # globals.update(read_env())
    df = pd.read_csv(filepath, parse_dates=True)
    df['finished'] = pd.to_datetime(df['finished'])
    df['timestamp'] = (df['finished'].view('int64') / 1e9).astype('int64')
    return df


def load_augmented_manychat_answers(filepath='data/answers_613364286_with_manychat_data.csv'):
    # globals.update(read_env())
    df = pd.read_csv(filepath, parse_dates=True)
    df['finished'] = pd.to_datetime(df['finished'])
    df['timestamp'] = (df['finished'].view('int64') / 1e9).astype('int64')
    return df


def find_manychat_user(row, config=None):
    if config is None:
        config = globals()
    log.info(f'Retrieving information for user named {row["full_name"]}')
    url = "https://api.manychat.com/fb/subscriber/findByName"
    params = dict(name=row['full_name'])
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer Bearer {MANYCHAT_API_KEY}".format(**config)
    }
    resp = requests.get(url=url, params=params, headers=headers)
    if resp.status_code == 200:
        log.error(resp.json())
    else:
        log.error(str(resp))
    return resp


class RateLimit():
    def __init__(self, rate=13, sleep=time.sleep, sleep_seconds=1.27):
        """ rate in requests per minute """
        self.t0 = time.time()
        self.rate = rate
        self.dt = 60 / self.rate
        self.sleep = sleep
        self.sleep_seconds = sleep_seconds

    def __call__(self, sleep_seconds=None):
        self.sleep_seconds = sleep_seconds or self.sleep_seconds
        slept = 0
        while time.time() < self.t0 + self.dt:
            self.sleep(self.sleep_seconds)
            slept += 1
        self.t0 = time.time()
        return slept * self.sleep_seconds


def get_manychat_data(config=None):
    """ GET request API:
    https://api.manychat.com/swagger#/Subscriber/Manychat%5CController%5CApi%5CSubscriberController%3A%3AactionFindByName"""
    if config is None:
        config = load_env()
    df = load_manychat_answers()

    rows = []
    rate = 29  # per minute

    delta_t = 60 / rate
    t0 = time.time()
    for i, row in df.iterrows():
        row = copy.deepcopy(row.to_dict())
        row['full_name'] = copy.copy(row['user'])
        resp = find_manychat_user(row=row, config=config)
        datas = resp.json()['data']
        if len(datas) > 1:
            log.warning(f"Found {len(datas)} users with the name {row['full_name']}..")
        for data in datas:
            row = copy.deepcopy(row)
            row['user_id'] = data['id']
            for k in (
                    'status gender last_name first_name profile_pic '
                    'last_input_text phone optin_phone email optin_email subscribed '
                    'last_interaction last_seen ig_last_seen is_followup_enabled').split():
                row[k] = data[k]
            for d in data['custom_fields']:
                row[d['name']] = d['value']
            # row.update(dict(data))
            rows.append(row)

        if time.time() - t0 < delta_t:
            time.sleep(2.13)
        t0 = time.time()

    newdf = pd.DataFrame(rows)
    filepath = 'data/answers_613364286_with_manychat_data.csv'
    newdf.to_csv(filepath)
    return newdf


def upload_amplitude_record(row, config):
    url = 'https://api2.amplitude.com/2/httpapi'
    data = {
        "api_key": config['AMPLITUDE_API_KEY'],
        "events": [{
            "user_id": row['user_id'],
            "event_type": "Reported Age Group",
            "time": row['timestamp'],
            "event_properties": {
                "age_group": row['age_group']
            },
            "user_properties": {
                "age_group": row['age_group'],
            }
        }
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }
    resp = requests.post(url, json=data, params={}, headers=headers)
    if resp.status_code == 200:
        log.error(resp.json())
    else:
        log.error(str(resp))
    return resp.json()


def upload_amplitude_batch(batch, config):
    if isinstance(batch, (dict, pd.Series)):
        batch = [batch]
        log.warning(
            f'Uploading only a single event or record for {batch[0]["full_name"]} to amplitude.')
    url = 'https://api2.amplitude.com/2/httpapi'
    data = {
        "api_key": config['AMPLITUDE_API_KEY'],
        "events": [{
            "user_id": row['user_id'],
            "event_type": "Reported Age Group",
            "time": row['timestamp'],
            "event_properties": {
                "age_group": row['age_group']
            },
            "user_properties": {
                "age_group": row['age_group'],
            }
        } for row in batch]
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }
    resp = requests.post(url, json=data, params={}, headers=headers)
    print(resp)
    # TODO requests wrapper for vebosity
    if resp.status_code == 200:
        log.error(resp.json())
    else:
        log.error(str(resp))
    return resp.json()


def upload_all_amplitude_records(
        df='data/answers_613364286_with_manychat_data.csv',
        config=None,
        numevents=1,
        rate=13,
        batch_size=40,
):
    """ HTTP2 API: https://developers.amplitude.com/docs/http-api-v2#uploadrequestbody """
    if config is None:
        config = load_env()
    records = []
    if isinstance(df, str):
        df = load_augmented_manychat_answers(df)
    limit_rate = RateLimit(rate=rate)
    num_records_uploaded = 0
    total_records = len(df)
    batch = []
    numevents = min(total_records, numevents)
    for i, row in tqdm(df.iterrows(), total=int(total_records / batch_size) + 1):
        limit_rate()
        batch.append(row.to_dict())
        if len(batch) >= batch_size or num_records_uploaded == total_records - len(batch):
            print(upload_amplitude_batch(batch=batch, config=config))
            num_records_uploaded += len(batch)
            if num_records_uploaded >= total_records:
                log.error(f'All done uploading {total_records}!!!')
            batch = []
            if num_records_uploaded >= numevents:
                break
    if num_records_uploaded < total_records:
        print(f'Only uploaded {num_records_uploaded} out of {total_records} total records.')
    return pd.DataFrame(records)


if __name__ == '__main__':
    rate = 13.13
    config = load_env()
    command = config.get('DEFAULT_COMMAND', 'a')
    command_names = dict(a='amplitude-upload', m='manychat-download', b='both-manychat-and-amplitude')
    numevents = int(config.get('NUM_EVENTS', 1))
    if len(sys.argv) > 1:
        command = sys.argv[1].strip().lstrip('-').lower()[0]
    if len(sys.argv) > 2:
        numevents = int(sys.argv[2].strip().lstrip('-').lower())
    log.warning(f'Running: {command_names[command]} for {numevents} users at {rate} per min.')
    if command in 'mb':
        dfmanychat = get_manychat_data(config=config, rate=rate)
    if command in 'ab':
        dfuploaded = upload_all_amplitude_records(config=config, rate=rate, numevents=numevents)
