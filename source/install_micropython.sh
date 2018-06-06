esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 write_flash 0x1000 esp32-20180511-v1.9.4-2-g9630376d.bin
