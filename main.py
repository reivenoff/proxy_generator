# Lousy proxy generator(no)
import requests  # pip install requests
import colorama  # pip install colorama

from colorama import Fore, Style

# Settings
ip = '1.1.1.1'
ports = [80, 999, 3128, 8080, 8123, 8888, 55443, 57844]
timeout = 1.5

# Function for changing the digits in the ip address
def change_ip():
    ip_split = [int(ip.split('.')[0]),
                int(ip.split('.')[1]),
                int(ip.split('.')[2]),
                int(ip.split('.')[3])]

    if ip_split[3] == 999 and ip_split[2] == 999 and ip_split[1] == 999 and ip_split[0] == 999:
        print('['+Fore.YELLOW+'FINAL'+Fore.LIGHTCYAN_EX+f'] The final! The result in the file "http_proxy.txt"!')
        raise NameError('HiThere')
    elif ip_split[3] != 999:
        ip_split[3] = ip_split[3] + 1
    else:
        ip_split[3] = 0
        if ip_split[2] != 999:
            ip_split[2] = ip_split[2] + 1
        else:
            ip_split[2] = 0
            if ip_split[1] != 999:
                ip_split[1] = ip_split[1] + 1
            else:
                ip_split[1] = 0
                ip_split[0] = ip_split[0] + 1

    return f'{ip_split[0]}.{ip_split[1]}.{ip_split[2]}.{ip_split[3]}'

# Getting http proxy
# Creating txt file with http proxy
http_file = open('http_proxy.txt', 'a')

while True:
    ip = change_ip()
    answer = False
    for port in ports:
        try:
            r = requests.get(f'http://{ip}:{port}/', timeout=timeout)
            if r.status_code == requests.codes.ok:
                http_file.write(str(ip)+'\n')
                print(Fore.LIGHTCYAN_EX+'['+Fore.WHITE+'Answer'+Fore.LIGHTCYAN_EX+f']'+Fore.GREEN+f'{ip} == {r.status_code}')
                # answer = True
                # break
        except: pass
    # if answer is False:
    #     print(Fore.LIGHTCYAN_EX+'['+Fore.WHITE+'Answer'+Fore.LIGHTCYAN_EX+f']'+Fore.RED+f'{ip} no connection')
