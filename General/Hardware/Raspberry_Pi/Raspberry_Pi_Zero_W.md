# Raspberry Pi - Zero W

## Imaging
* Start the imaging tool (Raspberry Pi Imager)
* Plug in micro SD card (USB or SD Adapter)
* Choose OS (Raspian OS lite command line only)
* Click Write (Wait for writing and verification to complete)
* Insert micro SD into Raspberry Pi Zero W and plugin power to boot

## Setting up keyboard

```
raspi-config
```

Run raspi-config then choose **Localisation Options** > **Change Locale** (en_US.UTF-8) (Optional)

Run raspi-config then choose **Localisation Options** > **Change Keyboard Layout** 
* Choose Generic 101-key PC > English (US)
* Choose The default for the keyboard layout
* No compose key

## Setting up wifi

```
wpa_passphrase <SSID> >> /etc/wpa_supplicant/wpa_supplicant.conf
```

Type the password into the blank prompt. Open the wpa_supplicant.conf and delete the plaintext password

```
wpa_cli -i wlan0 reconfigure
```

Connects to the network specified in wpa_supplicant.conf if configured correctly

## Setting up SSH

```
sudo systemctl enable ssh
sudo systemctl start ssh
```

## Updating

```
sudo apt update && apt full-upgrade -y
```


## References
* https://www.raspberrypi.org/documentation/installation/installing-images/
* https://www.raspberrypi.org/documentation/configuration/raspi-config.md
* https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
* https://www.raspberrypi.org/documentation/remote-access/ssh/README.md
* https://www.raspberrypi.com/documentation/computers/os.html#using-apt
