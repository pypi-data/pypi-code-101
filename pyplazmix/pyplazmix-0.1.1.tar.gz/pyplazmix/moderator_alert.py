from datetime import datetime


class ModeratorAlert:
    """[pyplazmix.ModeratorAlerts] - Plazmix ModeratorAlerts
    
    :param data: ModeratorAlerts object
    :type data: dict
    """
    def __init__(self, data: dict):
        self.id = data['id']
        self.author = data['author']
        self.type = data['type']
        self.reason = data['reason']
        self.create_date = datetime.fromtimestamp(int(data['create_date_timestamp']))
        self.active = data['active']

    def __repr__(self):
        return f'<ModeratorAlert id={self.id} author="{self.author}">'