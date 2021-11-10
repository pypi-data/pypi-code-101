#!/usr/bin/env python
import argparse
import os
from os.path import expanduser
import configparser
from InquirerPy import prompt
import pandas as pd
import pystache
from twilio.rest import Client

config_file = os.path.join(expanduser("~"), '.twilio-sendsms.config')


def config_twilio():
    questions = [
        {
            'type': 'input',
            'name': 'sender',
            'message': 'Sender name',
        },
        {
            'type': 'input',
            'name': 'account_sid',
            'message': 'Twillio Account SID',
        },
        {
            'type': 'input',
            'name': 'token',
            'message': 'Twillio Auth Token',
        }
    ]

    print("== Twillio Client Configuration ==")
    return prompt(questions)


def read_config(force_update=False):
    config = configparser.ConfigParser()

    if not force_update and os.path.isfile(config_file):
        config.read(config_file)
    else:
        config['twilio'] = config_twilio()

        print("Writing config to " + config_file)
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    return config


def send_sms(client, from_mobile, to_mobile, body):
    try:
        message = client.messages \
                        .create(
                            body=body,
                            from_=from_mobile,
                            to=to_mobile
                        )

        print(to_mobile + ',' + message.sid + ',' + body)
    except:
        print('Error sending SMS to : ' + to_mobile + ',' + message.sid)


def run(conf, file, template, sample=None, sendto=None):
    df = pd.read_csv(file, dtype={'mobile_number': 'str'})
    parsed_template = None

    renderer = pystache.Renderer()
    with open(template, 'r', encoding='utf-8') as template_file:
        parsed_template = pystache.parse(template_file.read())

    # Extract keys from the template for validation against input file
    template_keys = []
    for node in parsed_template._parse_tree:
        if isinstance(node, pystache.parser._EscapeNode):
            template_keys.append(node.key)

    for key in template_keys:
        if key not in df.columns:
            raise NameError('Missing column in input file ' + key)

    twilio_client = Client(conf["account_sid"], conf["token"])

    if sample is not None:
        df = df.sample(int(sample))

    for index, row in df.iterrows():
        template_params = {}
        for key in template_keys:
            template_params[key] = row[key]

        message = renderer.render(parsed_template, template_params)
        mobile_number = row["mobile_number"] if sendto is None else sendto

        if mobile_number.startswith('+'):
            send_sms(twilio_client, conf['sender'], mobile_number, message)
        else:
            print('ERROR - Mobile number ' + mobile_number +
                  ' was not in international format e.g. +614XXXXXXXX')


def main():
    parser = argparse.ArgumentParser(prog='twilio-sendsms')

    parser.add_argument(
        '--template', help='Mustache template to use.')
    parser.add_argument(
        '--sample', help='Randomly sample n lines from the input file')
    parser.add_argument(
        '--sendto', help='Ignore the mobile number in the input file and sent to this.')
    parser.add_argument(
        'file', help='Input file with fields matching the template.')
    args = parser.parse_args()

    run(read_config()['twilio'], args.file,
        args.template, args.sample, args.sendto)


if __name__ == '__main__':
    main()
