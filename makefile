all:
	clear
		cd /home/pi/Downloads
			wget https://github.com/pu8asr/svxlink-automake/raw/master/start.c
				gcc -g -o start start.c
					./start
					
clean: installer
	sudo rm -f -r *
