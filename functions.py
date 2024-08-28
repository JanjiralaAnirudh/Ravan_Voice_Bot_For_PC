import pyautogui
import keyboard
import subprocess
import ctypes
import os
import pyttsx3
import wmi
import psutil
import winreg
import requests
import pywhatkit
from pywhatkit.core.exceptions import InternetException
import datetime
import speedtest
import getpass
import csv
import time
import pygetwindow as gw

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def time():
      time = "curruct time is " + datetime.datetime.now().strftime("%H:%M %p")
      talk(time)

def date():
      currentdate = datetime.date.today()
      talk(str(currentdate))

def check_internet():
    try:
        response = requests.get("http://www.google.com", timeout=3)
        if response.status_code == 200:
            net = "yes"
        else :      net = "no"
    except requests.ConnectionError:
        pass
    return net

def play_song(query):
      song = query.replace("play", "")
      try:
            talk("playing" + song)
            pywhatkit.playonyt(song)
      except InternetException:
            pass

def allow_bluetooth():
        pyautogui.click(x=1697, y=1048)
        pyautogui.sleep(1)
        pyautogui.click(x=1660, y=440)

def check_application(query):
    apps = []

    # Check registry keys
    registry_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for key_path in registry_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    subkey_name = winreg.EnumKey(key, i)
                    subkey_path = os.path.join(key_path, subkey_name)
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                            app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            apps.append(app_name)
                    except FileNotFoundError:
                        continue
        except FileNotFoundError:
            continue

    # Check common app directories
    app_directories = [
        r"C:\Program Files",
        r"C:\Program Files (x86)"
    ]

    for directory in app_directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".exe"):
                    app_name = os.path.splitext(file)[0]
                    apps.append(app_name.lower())


    apps = sorted(apps)
    for i in apps:
        if i in query :
            talk("opening "+i)
            open_application(i)
            break

def is_bluetooth_on():
    try:
        wmi_service = wmi.WMI()
        bt_adapter = wmi_service.Win32_PnPEntity(Description='Bluetooth Device (Personal Area Network)')
        return bool(bt_adapter)
    except Exception:
        return False

def bluetooth_access(query):
        if is_bluetooth_on() == True:     bluetooth = "on"
        else :  bluetooth = "off"

        if ("on" in query) and (bluetooth == "on"):
                talk("your bluetooth is already in ON")
        
        if ("on" in query) and (bluetooth == "off"):
                talk("oning bluetooth")
                allow_bluetooth()

        if ("off" in query) and (bluetooth == "off"):
                talk("your bluetooth is already in OFF")

        if ("half" in query) and (bluetooth == "off"):
                talk("your bluetooth is already in OFF")

        if ("off" in query) and (bluetooth == "on"):
                talk("OFFING bluetooth")
                allow_bluetooth()

        if ("half" in query) and (bluetooth == "on"):
                talk("OFFING bluetooth")
                allow_bluetooth()
        
        if ("check" in query) or ("status" in query) or ("state" in query):
                talk("your bluetooth is in "+bluetooth+" state")

def settings_access():
        keyboard.press("windows+u")

def increse_sound():
        pyautogui.press("volumeup",10)

def decrese_sound():
        pyautogui.press("volumedown",10)

def mute_sound():
        pyautogui.press("volumedown",100)

def unmute_sound():
        pyautogui.press("volumeup",35)

def open_application(application_name):
        keyboard.press_and_release("windows")
        pyautogui.sleep(1)
        keyboard.write(application_name)
        pyautogui.sleep(1)
        keyboard.press_and_release("enter")


def lock_system():
        LockWorkStation = ctypes.windll.user32.LockWorkStation
        LockWorkStation()

def shut_down():
    talk("bye bye !!!!!")
    os.system("taskkill /F /IM chrome.exe")
    os.system("shutdown /s /t 0")

def restart_sys():
        os.system("shutdown /r /t 1")

def wifi_status():
        wifi_on_or_off = ''
        connections = psutil.net_if_stats()
        for interface, status in connections.items():
                if "Wi-Fi" in interface or "wlan" in interface:
                        if status.isup:         wifi_on_or_off = "on"
                        else :      wifi_on_or_off = 'off'
        
        talk("your wifi is in "+wifi_on_or_off)

def get_connected_wifi_network():
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    output = result.stdout.lower()
    ssid_index = output.find("ssid")
    if ssid_index != -1:
        ssid_start_index = output.find(":", ssid_index) + 1
        ssid_end_index = output.find("\n", ssid_start_index)
        return output[ssid_start_index:ssid_end_index].strip()
    return None

def wifi_net_con():
        connected_wifi = get_connected_wifi_network()
        if connected_wifi:
                connection_name = "Connected WiFi network is "+str(connected_wifi)
                talk(connection_name)
        else:
                talk("No WiFi network connected.")

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', ctypes.c_byte),
        ('BatteryFlag', ctypes.c_byte),
        ('BatteryLifePercent', ctypes.c_byte),
        ('Reserved1', ctypes.c_byte),
        ('BatteryLifeTime', ctypes.c_ulong),
        ('BatteryFullLifeTime', ctypes.c_ulong),
    ]

def get_battery_percentage():
    status = SYSTEM_POWER_STATUS()
    ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status))
    return status.BatteryLifePercent

def BatteryPercentage():
      percentage = get_battery_percentage()
      talk("your battery percentage is "+str(percentage))

def in_charge_or_not():
    battery = psutil.sensors_battery()
    if battery.power_plugged:
          talk("your pc is charging")
          BatteryPercentage()
    else :  
          talk("your pc is not in charging &")
          BatteryPercentage()

def open_whatsapp():
      pywhatkit.open_web()

def check_internet_speed():
    talk("just wait few seconds !!!")
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    talk(f"Download Speed: {download_speed:.2f} Mbps")
    talk(f"Upload Speed: {upload_speed:.2f} Mbps")

def get_username():
    username = getpass.getuser()
    talk("username is "+username.lower())

def save_query_to_csv(query):
    filename = 'aa_bot_queries.csv'
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([query])

def get_queries():
    filename = 'aa_bot_queries.csv'
    # Open the file and read the queries from CSV
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        queries = [row[0] for row in reader]

    commands = list(queries)
    last = len(commands)
    previous_query = commands[last-1]
    talk("your last query is ")
    talk(previous_query)

def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    
def countdown_timer(minutes):
    seconds = minutes * 60
    talk("timer as been started")
    time.sleep(seconds)
    talk("Time's up!")

def tab_closing():
    talk("closing !!!")
    active_window = gw.getActiveWindow()
    if active_window is None:
        talk("No active window found.")
        return
    
    active_window.close()
