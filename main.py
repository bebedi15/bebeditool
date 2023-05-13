import os
from threading import Thread, active_count
import colorama
import requests


colorama.init()

output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
from startdisplay import display_menu
display_menu()
