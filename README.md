# AntiCheatPS
Short Python script that detects alerts from Minecraft Anti-Cheats and plays a sound on your computer.
I made this script with the intention of moderating minecraft servers 24/7 while being able to do other things during the day without having to check the Minecraft chat every time. Most Anti-Cheat services don't play sounds when alerts are given in chat so this helps :3.

# Installation

# Dependencies
 -watchdog (for monitoring file changes)
 -playsound (for playing sound alerts)
To install both run:
 ```pip install watchdog playsound```
or
 ```py pip install watchdog playsound```

#Usage

1.- Clone repository
 ```git clone https://github.com/yourusername/AntiCheatPS.git```
 ```cd AntiCheatPS```

2.- Open script in VSC and update:
  LOGS_FOLDER = " "  -> Paste the path to your own Logs Folder (Default Minecraft logs are found in 'C:\Users\"yourname"\AppData\Roaming\.minecraft\logs')
  SOUND_FILE = "MGS.mp3"  -> Paste path to your desired sound file if you want a different sound than the one I use.

3.- Run the script ^^
 ```python anticheatps.py```
or
 ```py anticheatps.py```

#Contribute pls :3!
Feel free to open issues or submit pull requests if you have improvements!


