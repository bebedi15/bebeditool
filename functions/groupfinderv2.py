import os
import requests
from threading import Thread, active_count
import colorama
import requests
import json
import time
import concurrent.futures
import random
import threading


def groupfinderv2():
    current_time = time.localtime()

    formatted_time = "{0}-{1}-{2}-{3}-{4}-{5}".format(
        current_time.tm_mday,
        current_time.tm_mon,
        current_time.tm_year % 100,
        current_time.tm_hour,
        current_time.tm_min,
        current_time.tm_sec,
    )
    input(
        f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Make sure to put the Proxies in the 'proxies.txt' file. This group finder may slow down your Network Speed. press enter to continue..."
    )
    input(
        f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start..."
    )

    class stat:
        i = 1

    def check():
        num = random.randint(
            1000000, 17500000
        )  # you can change but its pretty good range
        proxy = random.choice(open("proxies.txt", "r").read().splitlines())
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        headers = {
            "authority": "groups.roblox.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "origin": "https://www.roblox.com",
            "referer": "https://www.roblox.com/",
            "sec-ch-ua": '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
        }
        try:
            response = requests.get(
                f"https://groups.roblox.com/v1/groups/{num}",
                headers=headers,
                proxies=proxies,
            )
            if "Too many requests" in response.text:
                print(
                    f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Proxy Limited: {proxy}"
                )
                return
            try:
                owner = response.json()["owner"]["username"]
                print(
                    f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Group with owner  Id:{response.json()['id']} | Owner: {owner} | {stat.i}"
                )
            except:
                if "Group is invalid or does not exist." in response.text:
                    print(
                        f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group invalid {num}"
                    )
                    return
                if "isLocked" in response.text:
                    if response.json()["isLocked"] == True:
                        print(
                            f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Locked Group: {response.json()['id']} | {stat.i}"
                        )
                        return
                else:
                    if response.json()["publicEntryAllowed"] == True:
                        with open(
                            f"output/Open_group{formatted_time}.txt", "a+"
                        ) as file:  # make a file
                            file.write(f"{response.json()['id']}\n")
                            print(
                                f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} No owner found: {response.json()['id']} | Open {response.json()['publicEntryAllowed']} | {stat.i}"
                            )
                            return
                    else:
                        if response.json()["publicEntryAllowed"] == False:
                            with open(
                                f"output/Closed_group{formatted_time}.txt", "a+"
                            ) as file:  # make a file v2 babe
                                file.write(f"{response.json()['id']}\n")
                        print(
                            f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} No owner found: {response.json()['id']} | Open {response.json()['publicEntryAllowed']} | {stat.i}"
                        )
                        return
        except:
            pass
        stat.i += 1

    while True:
        threading.Thread(target=check).start()