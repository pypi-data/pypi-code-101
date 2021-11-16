import enum


# permissions
class Permissions(enum.Enum):
    """[pyplazmix.ext.enums.Permissions] - Permissions enum"""
    DEFAULT = "DEFAULT"
    STAR = "STAR"
    COSMO = "COSMO"
    GALAXY = "GALAXY"
    UNIVERSE = "UNIVERSE"
    YOUTUBE = "YOUTUBE"
    YOUTUBE_PLUS = "YOUTUBE_PLUS"
    TESTER = "TESTER"
    ART = "ART"
    BUILDER = "BUILDER"
    BUILDER_PLUS = "BUILDER_PLUS"
    JUNIOUR = "JUNIOUR"
    MODERATOR = "MODERATOR"
    MODERATOR_PLUS = "MODERATOR_PLUS"
    DEVELOPER = "DEVELOPER"
    ADMINISTRATOR = "ADMINISTRATOR"
    OWNER = "OWNER"

# badges
class Badges(enum.Enum):
    """[pyplazmix.ext.enums.Badges] - Badges enum"""
    verification = "verification"
    legend = "legend"
    top_worker = "top_worker"
    worker = "worker"
    partner_developer = "partner_developer"
    plus_sub = "plus_sub"

# identifications
class Identifications(enum.Enum):    
    """[pyplazmix.ext.enums.Identifications] - Identifications enum"""
    AUTH = "auth"
    HUB = "hub"
    BEDWARS_LOBBY = "bwlobby"
    SKYWARS_LOBBY = "swlobby"
    SKYWARS_SOLO = "sws"
    SKYWARS_DOUBLE = "swd"
    BEDWARS_DOUBLE = "bws"
    BEDWARS_THREE = "bwd"
    BEDWARS_QUAD = "bwq"
    BEDWARS_POINTS_DOUBLE = "bwsp"
    BEDWARS_POINTS_THREE = "bwdp"
    BEDWARS_POINTS_QUAD = "bwqp"

# for developing
# metrics period
class MetricsPeriod(enum.Enum):    
    """[pyplazmix.ext.enums.MetricsPeriod] - Metrics Period enum"""
    LAST_HOUR = "last_hour"
    TODAY = "today"
    YESTERDAY = "yesterday"
    BEFORE_YESTERDAY = "before_yesterday"
    DAY = "24hours"
    WEEK = "week"
    PAST_WEEK = "past_week"