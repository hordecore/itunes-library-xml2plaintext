__author__ = 'oleg'
# coding:utf-8

import plistlib
from lastfm import scrobble_them


def diff_itunes(old, new):
    diff = {}
    count = "Play Count"
    for track in new:
        if count not in new[track]:
            continue
        if track in old:
            if old[track][count] == new[track][count]:
                continue
            diff[track] = new[track]
            diff[track][count] = new[track][count] - old[track][count]
        else:
            diff[track] = new[track]
    return diff


def main():
    track_dict_old = plistlib.readPlist('itunes_old.xml')['Tracks']
    track_dict_new = plistlib.readPlist('itunes_new.xml')['Tracks']
    track_dict_diff = diff_itunes(track_dict_old, track_dict_new)
    scrobble_them(track_dict_diff)


main()
