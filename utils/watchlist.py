"""
Trade Decision Engine

Watchlist Loader
"""

import json


WATCHLIST_FILE = "watchlist.json"


def load_watchlist():

    with open(WATCHLIST_FILE, "r") as file:

        data = json.load(file)

    return data["watchlist"]
