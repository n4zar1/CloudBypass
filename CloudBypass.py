import os

# Requirements Checking

try:
    import requests
except Exception:
    print('requests library not found please install it by : pip3 install requests')
    install = input('Do you want to install this library? (Y/N) >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install requests')
    else:
        quit()
try:
    import subprocess
except Exception:
    print('subprocess library not found please install it by : pip3 install subprocess')
    install = input('Do you want to install this library? (Y/N) >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install subprocess')
    else:
        quit()
try:
    import re
except Exception:
    print('re library not found please install it by : pip3 install re')
    install = input('Do you want to install this library? (Y/N) >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install re')
    else:
        quit()
try:
    import multiprocessing
except Exception:
    print('multiprocessing library not found please install it by : pip3 install multiprocessing')
    install = input('Do you want to install this library? (Y/N) >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install multiprocessing')
    else:
        quit()

# Start of Script

print('\x1b[1;32;40m'+'''
   #####                              ######                                    
 #     # #       ####  #    # #####  #     # #   # #####    ##    ####   ####  
 #       #      #    # #    # #    # #     #  # #  #    #  #  #  #      #      
 #       #      #    # #    # #    # ######    #   #    # #    #  ####   ####  
 #       #      #    # #    # #    # #     #   #   #####  ######      #      # 
 #     # #      #    # #    # #    # #     #   #   #      #    # #    # #    # 
  #####  ######  ####   ####  #####  ######    #   #      #    #  ####   #### '''+ '\033[0m')
print('''
 ==================================================
                github.com/n4zar1
              Bypass Cloud Protection
 ===================================================
''')
try:

    domain = input('[+] enter Target domain >> ')
except KeyboardInterrupt:
    print('\n[-] Stopping CloudBypass')
    quit()
def checker(domain):

    try:

        link=requests.get('http://'+domain)
        if link.status_code ==200 or link.status_code==403:


            ping_command = subprocess.check_output('ping -c 1 '+domain,shell=True)
            filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ping_command.decode('utf-8'))
            print('\x1b[1;32;40m'+'[+] the domain : '+domain+' has Ip address by : '+filtered_re[0]+ '\033[0m')

        else:

            print('\x1b[0;31;40m'+'[-] the domain : '+domain+' has Ip address by : N/A '+ '\033[0m')
    except Exception:
        print('\x1b[0;31;40m'+'[-] the domain : '+domain+' has Ip address by : N/A '+ '\033[0m')
        pass




try:

    with open('subl.txt','r')as wordlist:
        for word in wordlist:
            word = word.strip()

            try:

                subwdom= word+'.'+domain
                #checker(subwdom)
                p= multiprocessing.Process(target=checker,args=(subwdom,))
                p.start()
                p.join()
            except Exception:
                quit()
except KeyboardInterrupt:

    print('\n[-] Stopping CloudBypass')
    quit()
print('\n[-] Stopping CloudBypass')