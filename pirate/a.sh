#python i2c-write.py -i a -p /dev/ttyUSB0 -s 11072 -b 128
python i2c-write.py -i a -p /dev/ttyUSB0 -s 512 -b 128
python i2c-dump.py  -o b -p /dev/ttyUSB0 -s 512 -b 128
hexdump -C b

