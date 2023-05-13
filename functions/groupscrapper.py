import os
import requests
from threading import Thread, active_count
import colorama
import webbrowser
import requests
import json
import time
import threading
import concurrent.futures
import random
import string
from startdisplay import display_menu

def groupscrapper():
        threadc = 5
        groupid_input = int(
            input(
                f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter group Id: "
            )
        )
        groupids = [groupid_input]

        def scrape(gid):
            try:
                r = requests.get(f"https://groups.roblox.com/v1/groups/{gid}").json()
                fname = (
                    "".join(
                        x
                        for x in r["name"]
                        if x.lower() in "abcdefghijklmnopqrstuvwxyz1234567890 "
                    )
                    + f" ({gid})"
                )
                members = r["memberCount"]
            except:
                fname = gid
                members = "?"
            print(
                f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Started scraping {fname} ({members} members)"
            )
            fname = f"output/{fname}"
            cursor = ""
            while 1:
                try:
                    r = requests.get(
                        f"https://groups.roblox.com/v1/groups/{gid}/users?sortOrder=Asc&limit=100&cursor={cursor}"
                    )
                    users = [f'{x["user"]["username"]}\n' for x in r.json()["data"]]
                    with open(f"{fname}.txt", "a") as f:
                        f.writelines(users)
                    cursor = r.json()["nextPageCursor"]
                    if not cursor:
                        break
                except Exception as e:
                    print(
                        f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error... {e}"
                    )

        while 1:
            if groupids and (active_count() < threadc + 1):
                groupid = groupids.pop()
                Thread(target=scrape, args=(groupid,)).start()
            if active_count() == 1:
                break

        input(
            f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Finished! press enter to go to menu"
        )
        display_menu()