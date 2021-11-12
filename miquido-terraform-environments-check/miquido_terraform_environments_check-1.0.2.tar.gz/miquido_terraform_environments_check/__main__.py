import os


environments = os.getenv('ENVIRONMENTS').split(' ')

exit_code = 0
for environment in environments:
    exit_code += os.chdir(environment)
    exit_code += os.system('terraform init -backend=false')
    exit_code += os.system('terraform validate')
    exit_code += os.chdir('../')
