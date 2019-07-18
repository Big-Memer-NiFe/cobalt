import os, time

os.system('clear')
user = input("Enter Username: ")
os.system('clear')
os.system('toilet -F metal Cobalt')
print("!cmds.help to see all cmds.")
print("")
def lmao() -> object:
    lol = input('[' + user + '@cobalt ~]# ')

    if lol == "!other.help":
        print("\n!connect.ssh - Connect To An IP Via SSH")
        print("!connect.telnet - Connect To An IP Via Telnet")
        print("!system.free - See Memory/Swap Info")
        print("!tools.install - Install Everything")
        print("!other.calc - Calculator")
        print("!console.clear - Clear The Screen")
        print("!console.exit - Do I Really Need To Explain This One?\n")
        return lmao()

    elif lol == "!other.calc":
     calc()
     return lmao()

    elif lol == "!cmds.help":
         print("\n!tools.help - Tools Menu")
         print("!other.help - Other Cmds\n")
         return lmao()

    elif lol == "!cmds.nmap":
        print("\n!start.nmap1 - Quick Scan")
        print("!start.nmap2 - Quick Scan With OS Detection")
        print("!start.nmap3 - Intense Scan")
        print("!start.nmap4 - Intense Scan With OS Detection")
        print("!start.nmap5 - Intense Scan, All TCP Ports (1-65535)")
        print("!start.nmap6 - Scan A Specific Port\n")
        return lmao()

    elif lol == "!tools.help":
                print("\n!cmds.nmap - See Nmap Commands")
                print("!cmds.ytdl - See Youtube-dl Commands")
                print("!start.nikto - Start Nikto")
                print("!start.golismero - Start Golismero")
                print("!start.nikto - Start Nikto")
                print("!start.wpscan - Start WPScan")
                print("!start.sslscan - Start SSLScan")
                print("!start.beef - Start Beef-XSS")
                print("!start.sqlmap - Start Sqlmap")
                print("!start.msfconsole - Start Metasploit")
                print("!start.ophcrack - Start Ophcrack")
                print("!start.commix - Start Commix")
                print("!start.reconng - Start Recon-ng")
                print("!start.wireshark - Start Wireshark")
                print("!start.setoolkit - Start Setoolkit")
                print("!start.hexchat - Start Hexchat IRC Client")
                print("!start.xsser - Start XSSer")
                print("!start.tcpdump - Start TCPDump\n")
                return lmao()

    elif lol == "!start.tcpdump":
        os.system('clear')
        int = input("Interface: ")
        os.system('sudo tcpdump -i ' + int)
        return lmao()

    elif lol == "!system.free":
        print("")
        os.system('free')
        print("")
        return lmao()

    elif lol == "!start.xsser":
        xss = input("Enter URL (INCLUDING HTTP/HTTPS) ")
        os.system('xsser --all=' + xss)
        return lmao()

    elif lol == "!start.hexchat":
        os.system('clear')
        os.system('hexchat')
        return lmao()

    elif lol == "!tools.install":
        os.system('sudo apt-get install nmap -y')
        os.system('sudo apt-get install nikto -y')
        os.system('sudo apt-get install golismero -y')
        os.system('sudo apt-get install youtube-dl -y')
        os.system('sudo apt-get install wpscan -y')
        os.system('sudo apt-get install beef-xss -y')
        os.system('sudo apt-get install sslscan -y')
        os.system('sudo apt-get install sqlmap -y')
        os.system('sudo apt-get install ophcrack -y')
        os.system('sudo apt-get install commix -y')
        os.system('sudo apt-get install recon-ng -y')
        os.system('sudo apt-get install telnet -y')
        os.system('sudo apt-get install setoolkit -y')
        os.system('sudo apt-get install wireshark -y')
        os.system('sudo apt-get install hexchat -y')
        os.system('sudo apt-get install figlet -y')
        os.system('sudo apt-get install toilet -y')
        os.system('sudo apt-get install tcpdump -y')
        insts = input("Would you like to update? (y/n) ")

        if insts == "y" or insts == "Y":
           os.system('sudo apt-get update && upgrade')
           os.system('clear')
           print("Please restart the script.")
           exit()

        elif insts == "n" or insts == "N":
            os.system('clear')
            print("Please restart the script.")
            exit()

    elif lol == "!start.setoolkit":
        os.system('setoolkit')
        return lmao()

    elif lol == "!start.wireshark":
        os.system('wireshark')
        return lmao()

    elif lol == "!connect.ssh":
        sship = input("Enter IP: ")
        os.system('ssh ' + sship)
        return lmao()

    elif lol == "!connect.telnet":
        telip = input("Enter IP: ")
        telport = input("Enter Port: ")
        os.system('telnet ' + telip +' ' + telport)
        return lmao()

    elif lol == "!start.reconng":
        os.system('recon-ng')
        return lmao()

    elif lol == "!start.msfconsole":
        os.system('clear')
        os.system('msfconsole')
        return lmao()

    elif lol == "!start.commix":
        comurl = input("Enter URL(Including HTTP/HTTPS/WWW): ")
        os.system('commix --all --url=' + comurl)
        return lmao()

    elif lol == "!start.ophcrack":
        os.system('clear')
        os.system('ophcrack')
        return lmao()

    elif lol == "!start.sqlmap":
        sql1 = input("Enter URL: ")
        sqltor = input("Would you like to use tor?")
        if sqltor == "y" or sqltor == "Y" or sqltor == "yes" or sqltor == "YES":
            os.system('sqlmap -u ' + sql1 + ' --tor --time-sec 3 --random-agent --dump')
            return lmao()
        else:
            os.system('sqlmap -u ' + sql1 + ' --random-agent --dump')
            return lmao()

    elif lol == "!start.nikto":
        nikurl = input("Enter URL: ")
        os.system('nikto -h ' + nikurl)
        return lmao()

    elif lol == "!start.beef":
        os.system('clear')
        os.system('beef-xss')
        return lmao()

    elif lol == "!start.sslscan":
        ssl = input("Enter IP/URL: ")
        os.system('sslscan ' + ssl)
        return lmao()

    elif lol == "!start.wpscan":
        wpurl = input("Enter URL: ")
        os.system('wpscan --url ' + wpurl)
        return lmao()

    elif lol == "!start.golismero":
        golisurl = input("Enter URL: ")
        os.system('golismero ' + golisurl)
        return lmao()

    elif lol == "!cmds.ytdl":
        print("\n[!start.ytdl-mp4] Download Video As mp4")
        print("[!start.ytdl-mp3] Download Video As mp3\n")
        return lmao()

    elif lol == "!start.ytdl-mp4":
        ytmp4 = input("Enter URL: ")
        os.system('youtube-dl --recode-video mp4 ' + ytmp4)
        return lmao()

    elif lol == "!start.ytdl-mp3":
        ytmp3 = input("Enter URL: ")
        os.system('youtube-dl --extract-audio --audio-format mp3 ' + ytmp3)
        return lmao()

    elif lol == "!start.nmap1":
        quick = input("Enter IP/Website URL: ")
        os.system('nmap -F -Pn ' + quick)
        return lmao()

    elif lol == "!start.nmap2":
        quickos = input("Enter IP/Website URL: ")
        os.system('sudo nmap -O -F -Pn ' + quickos)
        return lmao()

    elif lol == "!start.nmap3":
        intense = input("Enter IP/Website URL: ")
        print("This is gonna take a while...")
        os.system('nmap -sV -Pn -T4 -A ' + intense)
        return lmao()

    elif lol == "!start.nmap4":
        intenseos = input("Enter IP/Website URL: ")
        print("This is gonna take a while...")
        os.system('sudo nmap -sV -Pn -T4 -A -O ' + intenseos)
        return lmao()

    elif lol == "!start.nmap5":
        intenseall = input("Enter IP/Website URL: ")
        print("This is gonna take forever...")
        os.system('sudo nmap -p 1-65535 -sV -Pn -T4 -A -O ' + intenseall)
        return lmao()

    elif lol == "!start.nmap6":
        specific = input("Enter IP/Website URL: ")
        specport = input("Enter Port Number: ")
        os.system('nmap -p ' + specport + ' -Pn ' + specific)
        return lmao()

    #if you looked at the code for this, fuck you. prick.
    elif (lol == "!lol.secret"):
           os.system('firefox https://www.youtube.com/watch?v=-zHm77FkW3U')
           os.system('firefox https://hentaihaven.org')
           os.system('start https://www.youtube.com/watch?v=-zHm77FkW3U')
           os.system('start https://hentaihaven.org')
           return lmao()

    elif lol == "!console.clear" or lol == "!console.cls":
        os.system('clear')
        os.system('toilet -F metal Cobalt')
        return lmao()

    elif lol == "!console.exit" or lol == "!console.quit":
       print("Cya!")
       time.sleep(2)
       exit()

    else:
        print("Error: " + lol + " Not Found.")
        return lmao()

def calc():

    print('1. add()\n2. sub()\n3. mul()\n4. div()')
    choice = input('[' + user + '@cobalt_calc ~]# ')
    if choice == '1':
               plus = int(input ("Enter A Value: "))
               plus1 = int(input ("Enter B Value: "))
               print(plus + plus1)
               return lmao()
    elif choice == '2':
               sub = int(input ("Enter A Value: "))
               sub1 = int(input ("Enter B Value: "))
               print(sub - sub1)
               return lmao()
    elif choice == '3':
               mult = int(input ("Enter A Value: "))
               mult1 = int(input ("Enter B Value: "))
               print(mult * mult1)
               return lmao()
    elif choice == '4':
              try:
                 div1 = int(input ("Enter A Value: "))
                 div2 = int(input ("Enter B Value: "))
                 print(div1 / div2)
              except:
                  print('zeros are not accepted')
    elif choice not in ['1', '2', '3', '4']:
              print('Not a Valid choice')
              return lmao()
try:
    lmao()
except:
     print("\nCya!")
     time.sleep(1)
     exit()

#made by NiFe#0666
