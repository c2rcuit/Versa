#!/usr/bin/env python3
import subprocess
import time
import os
import platform

start_stop = True
current_os = platform.system()

def openapps():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/Discord.app"])
        time.sleep(2)
        subprocess.run(["open", "/Applications/Brave.app"])
    elif current_os == "Windows":
        subprocess.run(["start", "discord"], shell=True)
        time.sleep(2)
        subprocess.run(["start", "brave"], shell=True)
    elif current_os == "Linux":
        subprocess.run(["discord"], shell=True)
        time.sleep(2)
        subprocess.run(["brave-browser"], shell=True)

def openroblox():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/Roblox.app"])
    elif current_os == "Windows":
        subprocess.run(["start", "RobloxPlayerLauncher.exe"], shell=True)
    elif current_os == "Linux":
        print("Roblox is not supported on Linux by default.")

def timetodev():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/PyCharm.app"])
    elif current_os == "Windows":
        subprocess.run(["start", "pycharm64.exe"], shell=True)
    elif current_os == "Linux":
        subprocess.run(["pycharm.sh"], shell=True)

def runnetworkdiagnostic():
    if current_os == "Darwin":
        os.system('osascript -e \'tell application "Terminal" to do script "ping -c 4 google.com"\'')
    elif current_os == "Windows":
        os.system('start cmd /k "ping -n 4 google.com"')
    elif current_os == "Linux":
        os.system('gnome-terminal -- bash -c "ping -c 4 google.com; exec bash"')

def opengoogle():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/Google Chrome.app"])
    elif current_os == "Windows":
        subprocess.run(["start", "chrome"], shell=True)
    elif current_os == "Linux":
        subprocess.run(["google-chrome"], shell=True)

def privacy():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/ProtonVPN.app"])
        subprocess.run(["open", "/Applications/Tor Browser.app"])
    elif current_os == "Windows":
        subprocess.run(["start", "ProtonVPN.exe"], shell=True)
        subprocess.run(["start", "TorBrowser.exe"], shell=True)
    elif current_os == "Linux":
        subprocess.run(["protonvpn"], shell=True)
        subprocess.run(["tor-browser"], shell=True)

def school():
    if current_os == "Darwin":
        subprocess.run(["open", "/Applications/Google Chrome.app"])
        subprocess.run(["open", "/Applications/Notes.app"])
        subprocess.run(["shortcuts", "run", "Enable DND"])
    elif current_os == "Windows":
        subprocess.run(["start", "chrome"], shell=True)
        subprocess.run(["start", "notepad"], shell=True)
    elif current_os == "Linux":
        subprocess.run(["google-chrome"], shell=True)
        subprocess.run(["gedit"], shell=True)

def close_all_apps():
    if current_os == "Darwin":
        os.system('osascript -e \'tell application "System Events" to set quitapps to (name of every process where background only is false and name is not "Finder")\' -e \'repeat with closeall in quitapps\' -e \'tell application closeall to quit\' -e \'end repeat\'')
    elif current_os == "Windows":
        subprocess.run('powershell "Get-Process | Where-Object { $_.MainWindowTitle } | ForEach-Object { Stop-Process -Id $_.Id -Force }"', shell=True)
    elif current_os == "Linux":
        subprocess.run("pkill -u $USER", shell=True)

def exit_program():
    print("Bye!")

# ASCII Art and Title
print("        /\\")
print("       /  \\")
print("      /    \\")
print("     /      \\")
print("    /        \\")
print("   /          \\")
print("  /            \\")
print(" /              \\")
print("/________________\\")
print("       ||")
print("       ||")
print("       ||")
print("       ||")
print("       ||")
print("       ||")
print("       ..")

print("VERSA V1.2")
print("Welcome to Versa V1.5")
print("POSSIBLE COMBINATIONS")
print("---------------------------------------------------------")
print(" Name                |   Action")
print("---------------------------------------------------------")
print(" OpenApps            |   Opens Discord and Brave")
print(" OpenRoblox          |   Opens Roblox")
print(" Timetodev           |   Opens PyCharm")
print(" NetworkDiagnostic   |   Opens Terminal and runs ping")
print(" OpenGoogle          |   Opens Google Chrome")
print(" Privacy             |   Opens ProtonVPN and Tor Browser")
print(" School              |   Opens browser and notes app")
print(" CloseApps           |   Closes All Apps")
print(" Exit                |   Exits the program")
print("---------------------------------------------------------")

while start_stop:
    inpit = input("What would you like to do? (OpenApps, OpenRoblox, Timetodev, NetworkDiagnostic, OpenGoogle, Privacy, School, Exit): ")
    if inpit == "OpenApps":
        openapps()
    elif inpit == "OpenRoblox":
        openroblox()
    elif inpit == "Timetodev":
        timetodev()
    elif inpit == "NetworkDiagnostic":
        runnetworkdiagnostic()
    elif inpit == "OpenGoogle":
        opengoogle()
    elif inpit == "Privacy":
        privacy()
    elif inpit == "School":
        school()
    elif inpit == "CloseApps":
        close_all_apps
    elif inpit == "Exit":
        exit_program()
        break
    else:
        print("Invalid input, please try again.")
