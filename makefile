all:
	clear
		cd /home/pi/Downloads
			wget https://github.com/pu8asr/svxlink-automake/raw/master/svxlink-install-pt_BR.c
				wget https://github.com/pu8asr/svxlink-automake/raw/master/optimization-partitions.py
					wget https://github.com/pu8asr/svxlink-automake/raw/master/optimization-usb.py
						gcc -g -o setup svxlink-install-pt_BR.c
							./setup
clean: setup
	rm -f setup
		rm -f svxlink-install-pt_BR.c
