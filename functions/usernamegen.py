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



def usernamegen():
    names = int(
        input(
            f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How many Usernames do you want to create: "
        )
    )  # Amount of usernames

    length = int(
        input(
            f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How long should be the usernames (letters): "
        )
    )  # Length of usernames
    if length < 3:
        print(
            f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} The length has to be 3 Letters or more"
        )
        length = int(
            input(
                f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How long should be the usernames (letters): "
            )
        )  # Length of usernames

    def randomword(length):
        letters = string.ascii_lowercase + string.digits
        return "".join(random.choice(letters) for i in range(length))

    current_time = time.localtime()

    formatted_time = "{0}-{1}-{2}-{3}-{4}-{5}".format(
        current_time.tm_mday,
        current_time.tm_mon,
        current_time.tm_year % 100,
        current_time.tm_hour,
        current_time.tm_min,
        current_time.tm_sec,
    )

    i = 0
    while i < names:
        try:
            user = randomword(length)

            print(
                f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} {user} not avaible"
            )

            Data = requests.get(
                f"https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20"
            )

            if int(Data.json()["code"]) == 0:
                i += 1
                print(
                    f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Found Username: {user} | Generated {i}/{names}"
                )

                with open(f"output/valid{formatted_time}.txt", "a") as f:
                    f.write(f"{user}\n")

        except Exception as e:
            print("Error:", e)

        time.sleep(50 / 1000)

    input(
        f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Finished! press enter to go to menu"
    )
    from startdisplay import display_menu
    display_menu()
