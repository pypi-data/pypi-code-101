from notetool.log import logger
from notetool.secret import read_secret

from github import Github


def upload_data_to_github(content, git_path, repo_str):
    access_tokens = read_secret(cate1='github', cate2='access_tokens', cate3='pygithub')
    g = Github(access_tokens)
    repo = g.get_repo(repo_str)
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    if git_path in all_files:
        contents = repo.get_contents(git_path)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        logger.info(f'{git_path} UPDATED')
    else:
        repo.create_file(git_path, "committing files", content, branch="master")
        logger.info(f'{git_path} CREATED')
    

def upload_file_to_github(file_path, *args, **kwargs):
    with open(file_path, 'r') as file:
        content = file.read()
        upload_data_to_github(content=content, *args, **kwargs)
