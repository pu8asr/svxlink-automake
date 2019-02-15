#coding:utf-8
######################################################
#
# Assistente de Configuração do SVXLINK no Pi
#
######################################################
# Autor: Airam Saile
# Indicativo: PU8ASR / PX8C1730 / PP8004SWL
# E-Mail: airamcosta@gmail.com
# Site: http://conferenciaamazonica.wordpress.com
######################################################
 
######################################################
# /etc/svxlink/svxlink.conf
# /etc/svxlink/svxlink.d/ModuleEchoLink.conf
# /etc/rc.local
######################################################

svxlink = "/etc/svxlink/svxlink.conf"
ModuleEchoLink = "/etc/svxlink/svxlink.d/ModuleEchoLink.conf"
start = "/etc/rc.local"

print("Você está configurando um LINK ou um REPETIDOR?")
type = raw_input("Informe L para Link ou R para Repetidor: ")
type = type.upper()
qra = raw_input("Qual seu nome? ")
qra = qra.upper()
callsign = raw_input("Qual seu indicativo? ")
callsign = callsign.upper()
password = raw_input("Informe sua senha do EchoLink: ")
qth = raw_input("Informe sua cidade e sigla do estado. Ex: Manaus - AM ")
qth = qth.upper()
print("Para a próxima pergunta, observe o exemplo")
qrg = raw_input("Informe a QRG de operação. Ex: 145.015 ")
print("Para a próxima pergunta, observe o exemplo")
ctcss = raw_input("Informe o Subtom ou deixe em branco se não houver. Ex: 67.0 ")
transceiver = raw_input("Informe o fabricante/modelo do seu transceptor: ")
transceiver = transceiver.upper()
antenna = raw_input("Informe o fabricante/modelo da sua antena: ")
antenna = antenna.upper()

# Realiza as alterações nos arquivos
if (type == "L"):
	# svxlink.conf
		with open(svxlink, 'U') as f:
			newText=f.read()
			
			while 'LOGICS=RepeaterLogic' in newText:
				newText=newText.replace('LOGICS=RepeaterLogic', 'LOGICS=SimplexLogic')
 
			while 'MYCALL' in newText:
				newText=newText.replace('MYCALL', callsign)
 
			while 'alsa:plughw:0' in newText:
				newText=newText.replace('alsa:plughw:0', 'alsa:plughw:1')
		
			while 'PTT_PORT=/dev/ttyS0' in newText:
				newText=newText.replace('PTT_PORT=/dev/ttyS0', 'PTT_PORT=GPIO')
			
			while 'PTT_PIN=DTRRTS' in newText:
				newText=newText.replace('PTT_PIN=DTRRTS', 'PTT_PIN=gpio17')
 
		with open(svxlink, "w") as f:
			f.write(newText)
		# ModuleEchoLink.conf
		with open(ModuleEchoLink, 'U') as f:
			newText=f.read()
 
			while 'MYCALL' in newText:
				newText=newText.replace('MYCALL', callsign)
			
			while '-R' in newText:
				newText=newText.replace('-R', '-L')
 
			while 'MyPass' in newText:
				newText=newText.replace('MyPass', password)
		
			while 'MyName' in newText:
				newText=newText.replace('MyName', qra)
		
			while '[Svx] Fq, MyTown' in newText:
				newText=newText.replace('[Svx] Fq, MyTown', qth)
			
			while 'You have connected to a SvxLink node' in newText:
				newText=newText.replace('You have connected to a SvxLink node', 'Você está conectado a um dispositivo Pi com SVXLINK')
				
			while 'a voice services system for Linux with EchoLink' in newText:
				newText=newText.replace('a voice services system for Linux with EchoLink', 'um sistema de suporte a voz sobre IP para')
			
			while 'support.' in newText:
				newText=newText.replace('support.', 'Linux com EchoLink')
			
			while 'Check out http://svxlink.sf.net/ for more info' in newText:
				newText=newText.replace('Check out http://svxlink.sf.net/ for more info', 'Acesse https://goo.gl/MGqJ5t para mais informações')
			
			while 'My_QTH' in newText:
				newText=newText.replace('My_QTH', qth)
			
			while 'Simplex link on ???.???' in newText:
				newText=newText.replace('Simplex link on ???.???', qrg)
			
			while 'My_CTCSS_fq_if_any' in newText:
				newText=newText.replace('My_CTCSS_fq_if_any', ctcss)
			
			while 'My_transceiver_type' in newText:
				newText=newText.replace('My_transceiver_type', transceiver)
			
			while 'My_antenna_brand/type/model' in newText:
				newText=newText.replace('My_antenna_brand/type/model', antenna)
 
		with open(ModuleEchoLink, "w") as f:
			f.write(newText)
		
		# rc.local
		with open(start, 'U') as f:
			newText=f.read()
 
			while 'exit 0' in newText:
				newText=newText.replace('exit 0', '')
 
		with open(start, "w") as f:
			f.write(newText)
		
		# Acrescenta ostras configurações
		initial = open(start, 'r+')
		initial.readlines()
		# Imprime o conteudo

		# Texto a ser inserido no arquivo
		startconfig = """# Configurações GPIO paraacionamento do PTT
# PTT GPIO17 (pino 11) -- Éselecionado o pino 11
# porque o pino 9 é GND (e fica ao lado do 11)
echo 17 > /sys/class/gpio/export
echo 'out' > /sys/class/gpio/gpio17/direction
echo 0 > /sys/class/gpio/gpio17/value

#Substitui /var/spool/svxlink que é temporário.
cd /var/spool
tar zxvf svxlink.tgz
		
svxlink
		
exit 0"""                     # Termina o texto

		initial.writelines(startconfig)
		initial.close() # Fecha o arquivo

		print("Seu link está configurado para acionar o PTT utilizando a porta\nGPIO 17 (pinos 11 e 9). Seu Raspberry se conectará no sistema EchoLink quando\nvocê ligá-lo.")
else:
	if (type == "R"):
		# svxlink.conf
		with open(svxlink, 'U') as f:
			newText=f.read()
			
			while 'LOGICS=SimplexLogic' in newText:
				newText=newText.replace('LOGICS=SimplexLogic', 'LOGICS=RepeaterLogic')
 
			while 'MYCALL' in newText:
				newText=newText.replace('MYCALL', callsign)
 
			while 'alsa:plughw:0' in newText:
				newText=newText.replace('alsa:plughw:0', 'alsa:plughw:1')
		
			while 'PTT_PORT=/dev/ttyS0' in newText:
				newText=newText.replace('PTT_PORT=/dev/ttyS0', 'PTT_PORT=GPIO')
			
			while 'PTT_PIN=DTRRTS' in newText:
				newText=newText.replace('PTT_PIN=DTRRTS', 'PTT_PIN=gpio17')
 
		with open(svxlink, "w") as f:
			f.write(newText)
		# ModuleEchoLink.conf
		with open(ModuleEchoLink, 'U') as f:
			newText=f.read()
 
			while 'MYCALL' in newText:
				newText=newText.replace('MYCALL', callsign)
			
			while '-L' in newText:
				newText=newText.replace('-L', '-R')
 
			while 'MyPass' in newText:
				newText=newText.replace('MyPass', password)
		
			while 'MyName' in newText:
				newText=newText.replace('MyName', qra)
		
			while '[Svx] Fq, MyTown' in newText:
				newText=newText.replace('[Svx] Fq, MyTown', qth)
			
			while 'You have connected to a SvxLink node' in newText:
				newText=newText.replace('You have connected to a SvxLink node', 'Você está conectado a um dispositivo Pi com SVXLINK')
				
			while 'a voice services system for Linux with EchoLink' in newText:
				newText=newText.replace('a voice services system for Linux with EchoLink', 'um sistema de suporte a voz sobre IP para')
			
			while 'support.' in newText:
				newText=newText.replace('support.', 'Linux com EchoLink')
			
			while 'Check out http://svxlink.sf.net/ for more info' in newText:
				newText=newText.replace('Check out http://svxlink.sf.net/ for more info', 'Acesse https://goo.gl/MGqJ5t para mais informações')
			
			while 'My_QTH' in newText:
				newText=newText.replace('My_QTH', qth)
			
			while 'Simplex link on ???.???' in newText:
				newText=newText.replace('Simplex link on ???.???', qrg)
			
			while 'My_CTCSS_fq_if_any' in newText:
				newText=newText.replace('My_CTCSS_fq_if_any', ctcss)
			
			while 'My_transceiver_type' in newText:
				newText=newText.replace('My_transceiver_type', transceiver)
			
			while 'My_antenna_brand/type/model' in newText:
				newText=newText.replace('My_antenna_brand/type/model', antenna)
 
		with open(ModuleEchoLink, "w") as f:
			f.write(newText)
		
		# rc.local
		with open(start, 'U') as f:
			newText=f.read()
 
			while 'exit 0' in newText:
				newText=newText.replace('exit 0', '')
 
		with open(start, "w") as f:
			f.write(newText)
		
		# Acrescenta ostras configurações
		initial = open(start, 'r+')
		initial.readlines()
		# Imprime o conteudo

		# Texto a ser inserido no arquivo
		startconfig = """# Configurações GPIO paraacionamento do PTT
# PTT GPIO17 (pino 11) -- Éselecionado o pino 11
# porque o pino 9 é GND (e fica ao lado do 11)
echo 17 > /sys/class/gpio/export
echo 'out' > /sys/class/gpio/gpio17/direction
echo 0 > /sys/class/gpio/gpio17/value

#Substitui /var/spool/svxlink que é temporário.
cd /var/spool
tar zxvf svxlink.tgz
		
svxlink
		
exit 0"""                     # Termina o texto

		initial.writelines(startconfig)
		initial.close() # Fecha o arquivo
		
		print("Seu repetidor está configurado para acionar o PTT utilizando a porta\nGPIO 17 (pinos 11 e 9). Seu Raspberry se conectará no sistema EchoLink quando\nvocê ligá-lo.")
		
	else:
		print("Você não informou um formato válido!\nTodo o esforço para desenvolver um sistema e você ainda consegue fazer errado?!\nPresta atenção pelo amor de Deus...")

