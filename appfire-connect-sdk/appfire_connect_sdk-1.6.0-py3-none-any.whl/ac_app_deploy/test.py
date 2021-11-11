import yaml

env = "dts"
stage = "stage"
try:
    with open("./env.yml", 'r') as stream:
        dts_env_settings = yaml.safe_load(stream)
except yaml.YAMLError as exc:
        logger.info(exc)
except IOError:
        logger.info("env.yml not found!")
aws_profile =  dts_env_settings['environment'][env][stage].get('profile')

print(aws_profile)

if aws_profile:
    print("yes")
else:
    print("no")