import datetime


class ImageRandomResult:

    def __init__(self, data):
        self.id = data['id']
        self.url = data['url']


class ImageIdResult:

    def __init__(self, data):
        self.id = data['id']
        self.tag = data['name']
        self.fileType = data['filetype']
        self.code = data['code']
        self.nsfw = data['nsfw']
        self.authorId = data['author']
        self.createdAt = datetime.datetime.strptime(data['createdAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')
        self.updatedAt = datetime.datetime.strptime(data['updatedAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')


class BanCheckResult:

    def __init__(self, data):
        self.isBanned = data['banned']
        self.createdAt = datetime.datetime.strptime(data['createdAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')
        self.updatedAt = datetime.datetime.strptime(data['updatedAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')



class BanInfoResult:

    def __init__(self, data):
        self.creator = data['creator']
        self.id = data['id']
        self.discordId = data['discord_id']
        self.isBlacklisted = data['is_bl']
        self.isBlacklistedWeb = data['is_bl_web']
        self.isWarned = data['is_warn']
        self.reason = data['reason']
        self.createdAt = datetime.datetime.strptime(data['createdAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')
        self.updatedAt = datetime.datetime.strptime(data['updatedAt'].split('.')[0], '%Y-%m-%dT%H:%M:%f')
