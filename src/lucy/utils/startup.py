import requests
from lucy.core.console import  ConsoleManager
def turn_on_flash_light():
    # gpio.setmode(gpio.BOARD)
    # gpio.setup(FLASHLIGHT, gpio.OUT)
    return

def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    """
    Checks for internet connection availability based on google page.
    """
    console_manager = ConsoleManager()
    try:
        console_manager.console_output(info_log='Checking internet connection..')
        _ = requests.get(url, timeout=timeout)
        console_manager.console_output(info_log='Internet connection passed!')
        return True
    except requests.ConnectionError:
        console_manager.console_output(warn_log="No internet connection.")
        return False

