all:
	clear
		cd /home/pi/Downloads
			wget http://pu8asr.talkaboutfrs.com.br/download/Pi/svxlink/svxlink-install-pt_BR.c
				wget http://pu8asr.talkaboutfrs.com.br/download/Pi/svxlink/optimization-partitions.py
					wget http://pu8asr.talkaboutfrs.com.br/download/Pi/svxlink/optimization-usb.py
						wget http://pu8asr.talkaboutfrs.com.br/download/Pi/svxlink/svxlink-install-pt_BR.c
							gcc -g -o setup svxlink-install-pt_BR.c
								./setup
clean: setup
	rm -f setup
		rm -f svxlink-install-pt_BR.c
