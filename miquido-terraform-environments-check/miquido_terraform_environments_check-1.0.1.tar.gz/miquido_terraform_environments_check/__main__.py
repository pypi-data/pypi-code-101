# yamllint disable rule:line-length
#     - |
#       IFS=' ' #setting space as delimiter
#       read -ra ENVIRONMENTS <<<"$ENVIRONMENTS"
#       for ENVIRONMENT in "${ENVIRONMENTS[@]}"
#       do
#         cd "$ENVIRONMENT"
#         git config --global \url."https://${GITLAB_TERRAFORM_DEPLOY_TOKEN_USERNAME}:${GITLAB_TERRAFORM_DEPLOY_TOKEN_SECRET}@gitlab.com/miquido/terraform".insteadOf "ssh://git@gitlab.com/miquido/terraform"
#         git config --global url."https://github.com".insteadOf "ssh://git@github.com"
#         terraform init -backend=false
#         terraform validate
#         cd -
#       done
import os


environments = os.getenv('ENVIRONMENTS').split(' ')
username = os.getenv('GITLAB_TERRAFORM_DEPLOY_TOKEN_USERNAME').split(' ')
secret = os.getenv('GITLAB_TERRAFORM_DEPLOY_TOKEN_SECRET').split(' ')

os.system(f'git config --global url."https://{username}:{secret}@gitlab.com/miquido/terraform".insteadOf "ssh://git@gitlab.com/miquido/terraform"')
os.system('git config --global url."https://github.com".insteadOf "ssh://git@github.com"')

for environment in environments:
    os.chdir(environment)
    os.system('terraform init -backend=false')
    os.system('terraform validate')
    os.chdir('../')
