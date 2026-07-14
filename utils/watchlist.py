"""
====================================================
Trade Decision Engine (TDE)

Universe Loader
====================================================
"""

import json
from pathlib import Path


# --------------------------------------------------
# Folder containing all universes
# --------------------------------------------------

UNIVERSE_FOLDER = Path("universes")


def load_universe(universe: str = "nifty50"):

    """
    Load a stock universe.

    Example
    -------
    load_universe("nifty50")

    Reads:

    universes/nifty50.json
    """

    universe_file = UNIVERSE_FOLDER / f"{universe}.json"

    with open(universe_file, "r") as file:

        data = json.load(file)

    return data["watchlist"]
