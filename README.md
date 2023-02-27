# LIDAR_Bot
* **Author** : _Sukarna Jana_
* **Date** : _26/Feb/2023_
* **Version** : _V0.1.0_
* **Title** : _YDLidar based navigation and mapping and moving the BOT over WiFi_
* **Credits** : [Team Vikasana](https://github.com/Vikasana-PU)

## Material Used :
> this project was maid in **India** So, all the following reference link are in **INR** and from **[Amazon.in](https://www.amazon.in/)** 

| **SNo.** | **Item Name** | **Referal link** |
| :---: | :---: | :---: |
| 1 | ESP32 | [LINK]() |
| 2 | YDLidar | [LINK]() |
| 3 | L2938 | [LINK]() |
| 4 | Motors x 4 | [LINK]() |
| 5 | Battery | [LINK]() |
| 6 | Step Down Convater | [LINK]() |
| 7 | USB Cable | [LINK]() |
| 8 | Chassis | [LINK]() |

| **Sno** | **Hardware/Software** | **Referal link** |
| :---: | :---: | :---: |
| 1 | PC | --- |
| 2 | Python3.x.x | [LINK]() |
| 3 | Arduino IDE | [LINK]() |

## Setup Guilde :
### 1. Setup ESP32 on your Arduino IDE
> **NOTE:** if you are from india you may face issue during installing ESP32 because ```raw.githubusercontent.com``` in banned by ISP of India. \
So, use **VPN**
1. In your Arduino IDE, go to **File > Preferences**
2. Enter the following into the “Additional Board Manager URLs” field:
```https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json``` Then, click the “OK” button
3. Open the Boards Manager. Go to **Tools > Board > Boards Manager…**
4. Search for **ESP32** and press install button for the **“ESP32 by Espressif Systems“**
5. That’s it. It should be installed after a few seconds...

### 2. Install few requied libraries
1. Python Libraries:
    * ```sudo python3 -m pip install requirements.txt```

## Reference :
* [ChatGPT](#) Helped a lot for understanding the concept. 
* [Youtube](https://www.youtube.com/watch?v=xSrjtJ2AZqw)
* [Github Repo](https://github.com/NikodemBartnik/LIDAR-Robot)
* [YDLidar Repo](https://github.com/YDLIDAR/ydlidar_arduino)