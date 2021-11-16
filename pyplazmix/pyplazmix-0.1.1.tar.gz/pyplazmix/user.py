from .enums import Permissions, Badges


# user
class User:
    """[pyplazmix.User] - Plazmix User
    
    :param data: User object
    :type data: dict
    """
    def __init__(self, data: dict):
        # general info
        self.id = data['id']
        self.uuid = data['uuid']
        self.nickname = data['nickname']
        self.level = data['level']
        
        # online info
        try:
            self.is_online = data["online"]["status"] == "ONLINE"
            self.online_comment = data['online']['comment']
        except: pass

        # groups
        self.__groups = data['groups']
        self.main_group = Permissions.__members__[self.__groups['main_group']['technical_name']]
        self.groups = [Permissions.__members__[x['technical_name']] for x in self.__groups['groups']]

        # friends
        self.friends_count = data['friends_count']

        # badges
        self.badges = [Badges.__members__[x['technical_name']] for x in data['badges']]

        # image
        try: self.image = Image(data['image'])
        except: pass

    def __repr__(self):
        return f'<User id={self.id} nickname="{self.nickname}" level={self.level}>'

# image
class Image:
    """[pyplazmix.Image] - Plazmix Image
    
    :param data: Image object
    :type data: dict
    """
    def __init__(self, data: dict):
        # general info
        self.identifier = data['identifier']
        self.skin_raw = data['skin_raw']

        # variants
        self.__variants = data['variants']

        self.avatar = self.__variants['avatar']
        self.head = self.__variants['head']
        self.bust = self.__variants['bust']
        self.body = self.__variants['body']