import pychromecast
import os

while True:
    menu = """
1. Scan For Chromecasts
2. Kill Current Running App
3. Reboot Chromecast
4. Play Video
5. Get Rick Rolled ;)
6. Info about chromecast
    """
    print menu

    choose = raw_input(">")

    if choose == "1":
	print "[*] Scanning..."
        chromecasts = pychromecast.get_chromecasts()
        myDevices = []
	for device in chromecasts:
  	    device.wait()
    	    print(str(device))
    elif choose == "2":
        ip = raw_input("IP of Chrome Cast> ")
        os.system('curl -H "Content-Type: application/json" http://%s:8008/apps/YouTube -X DELETE' % (ip))

    elif choose == "3":
        ip = raw_input("IP of Chrome Cast> ")
        os.system('curl -H "Content-Type: application/json" http://%s:8008/setup/reboot -d "{"params":"now"}" -X POST' % (ip))

    elif choose == "4":
        ip = raw_input("IP of Chrome Cast> ")
	print "eg. v=dQw4w9WgXcQ"
        video = raw_input("Link> ")
        os.system('curl -H "Content-Type: application/json" http://%s:8008/apps/YouTube -X POST -d "%s"' % (ip, video))
        
    elif choose == "5":
        ip = raw_input("IP of Chrome Cast> ")
        os.system('curl -H "Content-Type: application/json" http://%s:8008/apps/YouTube -X POST -d "v=dQw4w9WgXcQ"' % (ip))

    elif choose == "6":
        ip = raw_input("IP of Chrome Cast> ")
        os.system('curl http://%s:8008/setup/eureka_info?options=detail | json_pp' % (ip))

    else:
        print "Error!"
