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
from functions.groupfinder import groupfinder
from functions.groupscrapper import groupscrapper
from functions.groupfinderv2 import groupfinderv2
from functions.usernamegen import usernamegen


def handlechoices(choice):
    if choice == "1":
        groupfinder()
    elif choice == "3":
        groupscrapper()
    elif choice == "2":
        groupfinderv2()
    elif choice == "4":
        usernamegen()
    elif choice == "d":
        webbrowser.open("https://linksta.cc/@Bebedi")
    elif choice == "0":
        exit()
    else:
        print(
            f"{colorama.Fore.RED}[error]{colorama.Style.RESET_ALL} Invalid choice. Please try again."
        )
        time.sleep(2)
        from startdisplay import display_menu
        display_menu()