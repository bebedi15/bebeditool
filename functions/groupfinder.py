import os
import requests
from threading import Thread, active_count
import colorama
import requests
import json
import time
import concurrent.futures
import random


def groupfinder():
    current_time = time.localtime()
    formatted_time = "{0}-{1}-{2}-{3}-{4}-{5}".format(
            current_time.tm_mday,
            current_time.tm_mon,
            current_time.tm_year % 100,
            current_time.tm_hour,
            current_time.tm_min,
            current_time.tm_sec,
    )
    start_id = 1
    end_id = 17000000

    proxy_ask = input(
        f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to use the Proxy Pool? (y/n): "
    )
    if proxy_ask.lower() == "y":
        webhook_url = input(
            f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter webhook URL (leave empty if you dont want to use webhook): "
        )
        response = requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=100&country=all&ssl=all&anonymity=all"
        )
        proxies = [
            line.strip()
            for line in response.text.split("\r\n")
            if line.strip().endswith(":8080")
        ]
        proxy_index = 0
        if webhook_url:
            send_test_message = input(
                f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to send a test message to the webhook? (y/n): "
            )
            if send_test_message.lower() == "y":
                payload = {"content": "Test message"}
                headers = {"Content-Type": "application/json"}
                response = requests.post(
                    webhook_url, data=json.dumps(payload), headers=headers
                )
                response.raise_for_status()
                print(
                    f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Test message sent successfully"
                )

                input(
                    f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start..."
                )
        else:
            input(
                f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start..."
            )

        def process_group(group_id, proxy):
            group_id = random.randint(start_id, end_id)
            try:
                response = requests.get(
                    f"https://groups.roblox.com/v1/groups/{group_id}",
                    proxies={"http": proxy, "https": proxy},
                )
                print(
                    f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Request for Group ID {group_id} Status Code: {response.status_code}"
                )
                response.raise_for_status()
                data = json.loads(response.text)
                if (
                    data
                    and data.get("owner") is None
                    and data.get("publicEntryAllowed") is True
                ):
                    if (
                        not data.get("isLocked")
                        or data.get("isLocked")
                        and data.get("isLocked") is False
                    ):
                        group_name = data.get("name")
                        group_description = data.get("description")
                        payload = {
                            "embeds": [
                                {
                                    "title": "Group Found",
                                    "url": f"https://www.roblox.com/groups/{group_id}",
                                    "description": "Group without Owner found!",
                                    "color": 15258703,
                                    "fields": [
                                        {
                                            "name": "Id",
                                            "value": f"{group_id}",
                                        },
                                        {
                                            "name": "Name",
                                            "value": f"{group_name}",
                                        },
                                        {
                                            "name": "Description",
                                            "value": f"{group_description}",
                                        },
                                    ],
                                    "footer": {
                                        "text": "Group Finder",
                                    },
                                }
                            ]
                        }
                        headers = {"Content-Type": "application/json"}
                        if webhook_url:
                            response = requests.post(
                                webhook_url,
                                data=json.dumps(payload),
                                headers=headers,
                            )
                        with open(
                            f"output/ownerless_group{formatted_time}.txt", "a+"
                        ) as file:  # make a file v2 babe
                            file.writelines(f"{group_id}\n")
                        print(
                            f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} found ownerless group for Group ID {group_id}"
                        )
                    else:
                        with open(
                            f"output/Closed_group{formatted_time}.txt", "a+"
                        ) as file:  # make a file v2 babe
                            file.writelines(f"{group_id}\n")

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 400:
                    print(
                        f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group does not exist"
                    )
                else:
                    if e.response.status_code == 429:
                        print(
                            f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Too many requests, trying again..."
                        )
                    else:
                        if e.response.status_code == 500:
                            print(
                                f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Internal Server Error"
                            )
                        else:
                            print(
                                f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error..."
                            )
            except KeyboardInterrupt:
                print(
                    f"{colorama.Fore.RED}[exit]{colorama.Style.RESET_ALL} Keyboard interrupt detected, exiting..."
                )
            except:
                print(
                    f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error..."
                )

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            while True:
                group_id = random.randint(start_id, end_id)
                proxy = proxies[proxy_index]
                proxy_index = (proxy_index + 1) % len(proxies)
                executor.submit(process_group, group_id, proxy)

    else:
        if proxy_ask.lower() == "n":
            webhook_url = input(
                f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter webhook URL: "
            )

            if webhook_url:
                send_test_message = input(
                    f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to send a test message to the webhook? (y/n): "
                )
                if send_test_message.lower() == "y":
                    payload = {"content": "Test message"}
                    headers = {"Content-Type": "application/json"}
                    response = requests.post(
                        webhook_url, data=json.dumps(payload), headers=headers
                    )
                    response.raise_for_status()
                    print(
                        f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Test message sent successfully"
                    )

            input(
                f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start..."
            )

            while True:
                group_id = random.randint(start_id, end_id)

                try:
                    response = requests.get(
                        f"https://groups.roblox.com/v1/groups/{group_id}"
                    )
                    print(
                        f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Request for Group ID {group_id} Status Code: {response.status_code}"
                    )

                    response.raise_for_status()

                    data = json.loads(response.text)

                    if (
                        data
                        and data.get("owner") is None
                        and data.get("publicEntryAllowed") is True
                    ):
                        if (
                            not data.get("isLocked")
                            or data.get("isLocked")
                            and data.get("isLocked") is False
                        ):
                            group_name = data.get("name")
                            group_description = data.get("description")
                            payload = {
                                "embeds": [
                                    {
                                        "title": "Group Found",
                                        "url": f"https://www.roblox.com/groups/{group_id}",
                                        "description": "Group without Owner found!",
                                        "color": 15258703,
                                        "fields": [
                                            {
                                                "name": "Id",
                                                "value": f"{group_id}",
                                            },
                                            {
                                                "name": "Name",
                                                "value": f"{group_name}",
                                            },
                                            {
                                                "name": "Description",
                                                "value": f"{group_description}",
                                            },
                                        ],
                                        "footer": {
                                            "text": "Group Finder",
                                        },
                                    }
                                ]
                            }
                            headers = {"Content-Type": "application/json"}
                            if webhook_url:
                                response = requests.post(
                                    webhook_url,
                                    data=json.dumps(payload),
                                    headers=headers,
                                )
                            with open(
                                f"output/ownerless_group{formatted_time}.txt", "a+"
                            ) as file:  # make a file v2 babe
                                file.writelines(f"{group_id}\n")
                            print(
                                f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} ownerless group found for Group ID {group_id}"
                            )
                        else:
                            with open(
                                f"output/Closed_group{formatted_time}.txt", "a+"
                            ) as file:  # make a file v2 babe
                                file.writelines(f"{group_id}\n")

                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        print(
                            f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Too many requests, waiting for 15 seconds..."
                        )
                        time.sleep(15)
                    else:
                        if e.response.status_code == 400:
                            print(
                                f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group does not exist"
                            )
                        else:
                            if e.response.status_code == 500:
                                print(
                                    f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error..."
                                )
                            else:
                                print(
                                    f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error..."
                                )
                except KeyboardInterrupt:
                    print(
                        f"{colorama.Fore.RED}[exit]{colorama.Style.RESET_ALL} Keyboard interrupt detected, exiting..."
                    )
                    break
                except:
                    print(
                        f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error..."
                    )