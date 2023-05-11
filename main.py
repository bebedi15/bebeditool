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
colorama.init()

output_dir = 'output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(f"                               {colorama.Fore.MAGENTA} ______        _               _ _    _______          _  {colorama.Style.RESET_ALL}")
    print(f"                               {colorama.Fore.MAGENTA}(____  \      | |             | (_)  (_______)        | | {colorama.Style.RESET_ALL}")
    print(f"                               {colorama.Fore.MAGENTA} ____)  )_____| |__  _____  __| |_       _  ___   ___ | | {colorama.Style.RESET_ALL}")
    print(f"                               {colorama.Fore.MAGENTA}|  __  (| ___ |  _ \| ___ |/ _  | |     | |/ _ \ / _ \| | {colorama.Style.RESET_ALL}")
    print(f"                               {colorama.Fore.MAGENTA}| |__)  ) ____| |_) ) ____( (_| | |     | | |_| | |_| | | {colorama.Style.RESET_ALL}")
    print(f"                               {colorama.Fore.MAGENTA}|______/|_____)____/|_____)\____|_|     |_|\___/ \___/ \_){colorama.Style.RESET_ALL}")
    print(f'                                                                         ')
    print(f'                                                      {colorama.Fore.BLUE}Version 1.0{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}╔═════════════════════════════╦═══════════════════════════╦══════════════════════════════════╗{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > Tools & Features          {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > Made by Bebedi          {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > discord.gg                     {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}╠══╦══════════════════════════╬══╦════════════════════════╬══╦═══════════════════════════════╣{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}01{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Finder             {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}02{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Finder V2        {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}03{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Username Scraper        {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}04{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Username Generator       {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}05{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Coming soon            {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}06{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Coming soon                   {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}')
    print(f'              {colorama.Fore.BLUE}╚══╩══════════════════════════╩══╩════════════════════════╩══╩═══════════════════════════════╝{colorama.Style.RESET_ALL}')
    print('')
    print(f'                               {colorama.Fore.BLUE}╔═════════════════════════════╦═══════════════════════════════╗{colorama.Style.RESET_ALL}')
    print(f'                               {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} [ 0 ] Exit                  {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} [ d ] Support Me              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}')
    print(f'                               {colorama.Fore.BLUE}╚═════════════════════════════╩═══════════════════════════════╝{colorama.Style.RESET_ALL}')
    print(f'                                                                                               ')
    print(f'                                                                                               ')
    choice = input(f"                                              {colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter your choice: ")


    if choice == "1":
        start_id = 1
        end_id = 17000000


        proxy_ask = input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to use the Proxy Pool? (y/n): ")
        if proxy_ask.lower() == "y":

            webhook_url = input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter webhook URL (leave empty if you dont want to use webhook): ")
            response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=50&country=all&ssl=all&anonymity=all")
            proxies = [line.strip() for line in response.text.split("\r\n") if line.strip().endswith(":8080")]
            proxy_index = 0
            if webhook_url:
                send_test_message = input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to send a test message to the webhook? (y/n): ")
                if send_test_message.lower() == "y":
                    payload = {
                    "content": "Test message"
                    }
                    headers = {
                    "Content-Type": "application/json"
                    }
                    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
                    response.raise_for_status()
                    print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Test message sent successfully")

                    input(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start...")
            else:
                input(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start...")

            def process_group(group_id, proxy):
                group_id = random.randint(start_id, end_id)
                try:
                    response = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}", proxies={"http": proxy, "https": proxy})
                    print(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Request for Group ID {group_id} Status Code: {response.status_code}")
                    response.raise_for_status()
                    data = json.loads(response.text)
                    if data and data.get("owner") is None and data.get("publicEntryAllowed") is True:
                        if not data.get("isLocked") or data.get("isLocked") and data.get("isLocked") is False:
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
                                        "value": f"{group_description}"
                                        },
                                    ],
                                    "footer": {
                                        "text": "Group Finder",
                                    }
                                    }
                                ]
                            }
                            headers = {
                                "Content-Type": "application/json"
                            }
                            if webhook_url:
                                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
                            with open(f"output/ownerless_group{formatted_time}.txt", "a+") as file: # make a file v2 babe
                                file.writelines(f"{group_id}\n")
                            print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} found ownerless group for Group ID {group_id}")
                        else:
                            with open(f"output/Closed_group{formatted_time}.txt", "a+") as file: # make a file v2 babe
                                file.writelines(f"{group_id}\n")

                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 400:
                        print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group does not exist")
                    else:
                        if e.response.status_code == 429:
                            print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Too many requests, trying again...")
                        else:
                            if e.response.status_code == 500:
                                print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Internal Server Error")
                            else:
                                print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")
                except KeyboardInterrupt:
                    print(f"{colorama.Fore.RED}[exit]{colorama.Style.RESET_ALL} Keyboard interrupt detected, exiting...")
                except:
                    print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")

            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                while True:
                    group_id = random.randint(start_id, end_id)
                    proxy = proxies[proxy_index]
                    proxy_index = (proxy_index + 1) % len(proxies)
                    executor.submit(process_group, group_id, proxy)

        else:
            if proxy_ask.lower() == "n":

                webhook_url = input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter webhook URL: ")
                

                if webhook_url:
                    send_test_message = input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Do you want to send a test message to the webhook? (y/n): ")
                    if send_test_message.lower() == "y":
                        payload = {
                            "content": "Test message"
                        }
                        headers = {
                            "Content-Type": "application/json"
                        }
                        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
                        response.raise_for_status()
                        print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Test message sent successfully")



                input(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start...")

                while True:

                    group_id = random.randint(start_id, end_id)

                    try:


                        response = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}")
                        print(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Request for Group ID {group_id} Status Code: {response.status_code}")


                        response.raise_for_status()


                        data = json.loads(response.text)

                        
                        if data and data.get("owner") is None and data.get("publicEntryAllowed") is True:
                            if not data.get("isLocked") or data.get("isLocked") and data.get("isLocked") is False:
                                
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
                                            "value": f"{group_description}"
                                            },
                                        ],
                                        "footer": {
                                            "text": "Group Finder",
                                        }
                                        }
                                    ]
                                }
                                headers = {
                                    "Content-Type": "application/json"
                                }
                                if webhook_url:
                                    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
                                with open(f"output/ownerless_group{formatted_time}.txt", "a+") as file: # make a file v2 babe
                                    file.writelines(f"{group_id}\n")
                                print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} ownerless group found for Group ID {group_id}")
                            else:
                                with open(f"output/Closed_group{formatted_time}.txt", "a+") as file: # make a file v2 babe
                                    file.writelines(f"{group_id}\n")


                    except requests.exceptions.HTTPError as e:
                        
                        if e.response.status_code == 429:
                            print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Too many requests, waiting for 15 seconds...")
                            time.sleep(15)
                        else:
                            if e.response.status_code == 400:

                                print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group does not exist")
                            else:
                                if e.response.status_code == 500:
                                    print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")
                                else:
                                    print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")
                    except KeyboardInterrupt:
                        
                        print(f"{colorama.Fore.RED}[exit]{colorama.Style.RESET_ALL} Keyboard interrupt detected, exiting...")
                        break
                    except:
                        print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")
        
    elif choice == "3":
       
        threadc = 5
        groupid_input = int(input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter group Id: "))
        groupids = [groupid_input]

        def scrape(gid):
            try:
                r = requests.get(f'https://groups.roblox.com/v1/groups/{gid}').json()
                fname = ''.join(x for x in r['name'] if x.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890 ') + f' ({gid})'
                members = r['memberCount']
            except:
                fname = gid
                members = '?'
            print(f'{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Started scraping {fname} ({members} members)')
            fname = f'output/{fname}'
            cursor = ''
            while 1:
                try:
                    r = requests.get(f'https://groups.roblox.com/v1/groups/{gid}/users?sortOrder=Asc&limit=100&cursor={cursor}')
                    users = [f'{x["user"]["username"]}\n' for x in r.json()['data']]
                    with open(f'{fname}.txt', 'a') as f:
                        f.writelines(users)
                    cursor = r.json()['nextPageCursor']
                    if not cursor: break
                except Exception as e:
                    print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Unknown Error...")

        while 1:
            if groupids and (active_count() < threadc+1):
                groupid = groupids.pop()
                Thread(target=scrape, args=(groupid,)).start()
            if active_count() == 1: break

        input(f'{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Finished! press enter to go to menu')
        display_menu()
    elif choice == "2":
        current_time = time.localtime()

        formatted_time = "{0}-{1}-{2}-{3}-{4}-{5}".format(current_time.tm_mday, current_time.tm_mon, current_time.tm_year%100, current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
        input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Make sure to put the Proxies in the 'proxies.txt' file. This group finder may slow down your Network Speed. press enter to continue...")
        input(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Setup done! Press enter to start...")

        class stat():
            i = 1
        def check():
            num = random.randint(1000000, 17500000) # you can change but its pretty good range
            proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            headers = {
                'authority': 'groups.roblox.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'origin': 'https://www.roblox.com',
                'referer': 'https://www.roblox.com/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
            }
            try:
                response = requests.get(f'https://groups.roblox.com/v1/groups/{num}', headers=headers, proxies=proxies)
                if "Too many requests" in response.text:
                    print(f"{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Proxy Limited: {proxy}")
                    return
                try:
                    owner = response.json()['owner']['username']
                    print(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Group with owner  Id:{response.json()['id']} | Owner: {owner} | {stat.i}")
                except:
                    if "Group is invalid or does not exist." in response.text:
                        print(f'{colorama.Fore.YELLOW}[warn]{colorama.Style.RESET_ALL} Group invalid {num}')
                        return
                    if "isLocked" in response.text:
                        if response.json()['isLocked'] == True:
                            print(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Locked Group: {response.json()['id']} | {stat.i}")
                            return
                    else:
                        if response.json()['publicEntryAllowed'] == True:
                            with open(f"output/Open_group{formatted_time}.txt", "a+") as file: # make a file
                                file.write(f"{response.json()['id']}\n")
                                print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} No owner found: {response.json()['id']} | Open {response.json()['publicEntryAllowed']} | {stat.i}")
                                return
                        else:
                            if response.json()['publicEntryAllowed'] == False:
                                with open(f"output/Closed_group{formatted_time}.txt", "a+") as file: # make a file v2 babe
                                    file.write(f"{response.json()['id']}\n")
                            print(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} No owner found: {response.json()['id']} | Open {response.json()['publicEntryAllowed']} | {stat.i}")
                            return
            except:
                pass
            stat.i += 1
        while True:
            threading.Thread(target=check).start()
    elif choice == "4":



        names =  int(input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How many Usernames do you want to create: ")) # Amount of usernames

        length =  int(input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How long should be the usernames (letters): ")) # Length of usernames
        if length < 3:
            print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} The length has to be 3 Letters or more")
            length =  int(input(f"{colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} How long should be the usernames (letters): ")) # Length of usernames



        def randomword(length):
            letters = string.ascii_lowercase + string.digits
            return ''.join(random.choice(letters) for i in range(length))


        current_time = time.localtime()

        formatted_time = "{0}-{1}-{2}-{3}-{4}-{5}".format(current_time.tm_mday, current_time.tm_mon, current_time.tm_year%100, current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

        i = 0
        while i < names:
            try:
                user = randomword(length)
                
                print(f'{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} {user} not avaible')
                
                Data = requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20')
                
                if int(Data.json()['code']) == 0:
                    
                    i += 1
                    print(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Found Username: {user} | Generated {i}/{names}")
                    
                    with open(f'output/valid{formatted_time}.txt','a') as f:
                        f.write(f"{user}\n")
                        
            except Exception as e:
                print('Error:', e)

            time.sleep(50/1000)

        input(f'{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Finished! press enter to go to menu')
        display_menu()

    elif choice == "d":
        webbrowser.open('https://linksta.cc/@Bebedi')
    elif choice == "0":
        exit()
    else:
        print(f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Invalid choice. Please try again.")
        time.sleep(2)
        display_menu()


display_menu()
