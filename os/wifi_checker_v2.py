import tkinter as tk
import os 
import subprocess
import re

def Showwifi():
    try:
        result = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        label_pass = tk.Label(root, text=result)
        label_pass.pack(pady=5)
    except:
        label_pass.config(text="Błąd podczas pobierania WiFi")


def password():
    ssid = area.get()
    try:
        result = subprocess.run(
            f'netsh wlan show profile "{ssid}" key=clear',
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        password_match = re.search(r'Key Content\s*:\s*(.*)', result.stdout)
        if password_match:
            password = password_match.group(1).strip()
            label_pass = tk.Label(root, text=f"Password: {password}")
            label_pass.pack(pady=5)
        else:
            label_pass = tk.Label(root, text="No password found")
            label_pass.pack(pady=5)
    except subprocess.CalledProcessError:
        label_pass = tk.Label(root, text=f"Could not find Wi-Fi: '{ssid}'")
        label_pass.pack(pady=5)


root = tk.Tk()
root.title("Wifi checker_v2")
root.geometry("300x500")

#Label
label =tk.Label(root, text="To show actual password please type Wi-Fi name")
label.pack(pady=5)
#Area to type wifi
area = tk.Entry(root,width=30)
area.pack(pady=5)

#button to confirm typing
confirm = tk.Button(root, text="Search", command=password)
confirm.pack(pady=5)

#button to show all avablive wifi names
show = tk.Button(root, text="Show available networks", command=Showwifi)
show.pack(pady=5)



root.mainloop()

# ssid = input(f"Input your Wifi name to get pasword: ")
# password(ssid)
