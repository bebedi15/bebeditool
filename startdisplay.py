import os
import colorama
import sys

colorama.init()


def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"                               {colorama.Fore.MAGENTA} ______        _               _ _    _______          _  {colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.MAGENTA}(____  \      | |             | (_)  (_______)        | | {colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.MAGENTA} ____)  )_____| |__  _____  __| |_       _  ___   ___ | | {colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.MAGENTA}|  __  (| ___ |  _ \| ___ |/ _  | |     | |/ _ \ / _ \| | {colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.MAGENTA}| |__)  ) ____| |_) ) ____( (_| | |     | | |_| | |_| | | {colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.MAGENTA}|______/|_____)____/|_____)\____|_|     |_|\___/ \___/ \_){colorama.Style.RESET_ALL}"
    )
    print(f"                                                                         ")
    print(
        f"                                                      {colorama.Fore.BLUE}Version 1.1{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}╔═════════════════════════════╦═══════════════════════════╦══════════════════════════════════╗{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > Tools & Features          {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > Made by Bebedi          {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} > discord.gg                     {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}╠══╦══════════════════════════╬══╦════════════════════════╬══╦═══════════════════════════════╣{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}01{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Finder             {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}02{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Finder V2        {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}03{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Group Username Scraper        {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}04{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Username Generator       {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}05{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Coming soon            {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}06{colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} Coming soon                   {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}"
    )
    print(
        f"              {colorama.Fore.BLUE}╚══╩══════════════════════════╩══╩════════════════════════╩══╩═══════════════════════════════╝{colorama.Style.RESET_ALL}"
    )
    print("")
    print(
        f"                               {colorama.Fore.BLUE}╔═════════════════════════════╦═══════════════════════════════╗{colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} [ 0 ] Exit                  {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL} [ d ] Support Me              {colorama.Fore.BLUE}║{colorama.Style.RESET_ALL}"
    )
    print(
        f"                               {colorama.Fore.BLUE}╚═════════════════════════════╩═══════════════════════════════╝{colorama.Style.RESET_ALL}"
    )
    print(
        f"                                                                                               "
    )
    print(
        f"                                                                                               "
    )
    choice = input(
        f"                                              {colorama.Fore.BLUE}[Input]{colorama.Style.RESET_ALL} Enter your choice: "
    )
    from handler.choices import handlechoices
    handlechoices(choice)