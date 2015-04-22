__author__ = 'oleg'

from config import api_key, api_secret, username, password_hash
from time import time
import pylast

def scrobble(track, scrobbler):
    scrobbler.scrobble(artist=track['Artist'], title=track['Name'], timestamp=str(int(time())))

def scrobble_them(diff):
    for track in diff:
        for listen in range(0, diff[track]['Play Count']):
            try:
                scrobble(diff[track], get_scrobbler())
            except pylast.MalformedResponseError as e:
                continue
    return None


def get_scrobbler():
    network = pylast.LastFMNetwork(api_key = api_key,
                                   api_secret = api_secret,
                                   username = username,
                                   password_hash = password_hash)
    return network
