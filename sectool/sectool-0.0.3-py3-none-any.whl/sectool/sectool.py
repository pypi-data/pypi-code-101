import configparser
import os
import subprocess
import sys


def decrypt(secret_file, password):
    if secret_file.startswith("~"):
        secret_file = os.path.expanduser(secret_file)
    child = subprocess.Popen(
        f'openssl enc -aes-256-cbc -k {password} -d -in {secret_file}',
        stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output = child.communicate()[0]
    output = output.decode('utf-8')
    if child.returncode != 0:
        print(output)
        sys.exit(child.returncode)
    return output


def read_vars(str_data):
    config = configparser.ConfigParser()
    config.read_string(str_data)
    vars = dict(config.items('secrets'))
    return vars


def merge_values(vars, template_file):
    with open(template_file, 'r') as f:
        lines = f.readlines()

    merged = []
    for line in lines:
        for var in vars.keys():
            if '{{' + var + '}}' in line:
                line = line.replace('{{' + var + '}}', vars[var])
                break

        merged.append(line)

    return merged


def main(argv):
    if len(argv) == 3:
        secret_file = argv[0]
        password = argv[1]
        template_file = argv[2]
    elif len(argv) == 2:
        secret_file = argv[0]
        template_file = argv[1]
        password = input("Enter your password: ")
    else:
        print("Usage: python sectool.py <secret_file> [password] <path_to_template_file>")
        sys.exit(2)

    output = decrypt(secret_file, password)
    values = read_vars(output)
    merged_content = merge_values(values, template_file)
    for line in merged_content:
        print(line, end='')


if __name__ == "__main__":
    main(sys.argv[1:])
