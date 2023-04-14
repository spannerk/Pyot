import asyncio
import sys

from module.tasks import get_matches


if __name__ == "__main__":
    print("Summoner name:", sys.argv[1])
    matches = asyncio.run(get_matches(sys.argv[1]))
    print(
        "Found {} matches:".format(len(matches)),
        matches
    )
