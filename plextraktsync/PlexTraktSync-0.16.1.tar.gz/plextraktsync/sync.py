from plextraktsync.config import Config
from plextraktsync.decorators.measure_time import measure_time
from plextraktsync.decorators.memoize import memoize
from plextraktsync.logging import logger
from plextraktsync.media import Media
from plextraktsync.trakt_list_util import TraktListUtil
from plextraktsync.walker import Walker


class SyncConfig:
    def __init__(self, config: Config):
        self.config = dict(config["sync"])

    def __getitem__(self, key):
        return self.config[key]

    def __contains__(self, key):
        return key in self.config

    @property
    @memoize
    def trakt_to_plex(self):
        if "trakt_to_plex" not in self:
            return {
                "watched_status": self["watched_status"],
                "ratings": self["ratings"],
                "liked_lists": self["liked_lists"],
                "watchlist": self["watchlist"],
            }

        return self["trakt_to_plex"]

    @property
    @memoize
    def plex_to_trakt(self):
        if "plex_to_trakt" not in self:
            return {
                "watched_status": self["watched_status"],
                "ratings": self["ratings"],
                "collection": self["collection"]
            }

        return self["plex_to_trakt"]

    @property
    @memoize
    def sync_ratings(self):
        return self.trakt_to_plex["ratings"] or self.plex_to_trakt["ratings"]

    @property
    @memoize
    def sync_watched_status(self):
        return self.trakt_to_plex["watched_status"] or self.plex_to_trakt["watched_status"]


class Sync:
    def __init__(self, config: Config):
        self.config = SyncConfig(config)

    def sync(self, walker: Walker, dry_run=False):
        listutil = TraktListUtil()
        trakt = walker.trakt

        if self.config.trakt_to_plex["watchlist"] and trakt.watchlist_movies:
            listutil.addList(None, "Trakt Watchlist", trakt_list=trakt.watchlist_movies)

        if self.config.trakt_to_plex["liked_lists"]:
            for lst in trakt.liked_lists:
                listutil.addList(lst['username'], lst['listname'])

        for movie in walker.find_movies():
            self.sync_collection(movie, dry_run=dry_run)
            self.sync_ratings(movie, dry_run=dry_run)
            self.sync_watched(movie, dry_run=dry_run)
            listutil.addPlexItemToLists(movie)

        for episode in walker.find_episodes():
            self.sync_collection(episode, dry_run=dry_run)
            self.sync_ratings(episode, dry_run=dry_run)
            self.sync_watched(episode, dry_run=dry_run)
            listutil.addPlexItemToLists(episode)

        if not dry_run:
            with measure_time("Updated plex watchlist"):
                listutil.updatePlexLists(walker.plex)

        if not dry_run:
            trakt.flush()

    def sync_collection(self, m: Media, dry_run=False):
        if not self.config.plex_to_trakt["collection"]:
            return

        if m.is_collected:
            return

        logger.info(f"To be added to collection: {m}")
        if not dry_run:
            m.add_to_collection()

    def sync_ratings(self, m: Media, dry_run=False):
        if not self.config.sync_ratings:
            return

        if m.plex_rating is m.trakt_rating:
            return

        # Plex rating takes precedence over Trakt rating
        if m.plex_rating is not None:
            if not self.config.plex_to_trakt["ratings"]:
                return
            logger.info(f"Rating {m} with {m.plex_rating} on Trakt")
            if not dry_run:
                m.trakt_rate()
        elif m.trakt_rating is not None:
            if not self.config.trakt_to_plex["ratings"]:
                return
            logger.info(f"Rating {m} with {m.trakt_rating} on Plex")
            if not dry_run:
                m.plex_rate()

    def sync_watched(self, m: Media, dry_run=False):
        if not self.config.sync_watched_status:
            return

        if m.watched_on_plex is m.watched_on_trakt:
            return

        if m.watched_on_plex:
            if not self.config.plex_to_trakt["watched_status"]:
                return
            logger.info(f"Marking as watched in Trakt: {m}")
            if not dry_run:
                m.mark_watched_trakt()
        elif m.watched_on_trakt:
            if not self.config.trakt_to_plex["watched_status"]:
                return
            logger.info(f"Marking as watched in Plex: {m}")
            if not dry_run:
                m.mark_watched_plex()
