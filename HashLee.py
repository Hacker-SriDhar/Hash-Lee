from time import sleep
from HashLee import hashlib as h
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    NO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




print("""
 /$$   /$$                  /$$             /$$                        
| $$  | $$                 | $$            | $$                        
| $$  | $$ /$$$$$$  /$$$$$$| $$$$$$$       | $$       /$$$$$$  /$$$$$$ 
| $$$$$$$$|____  $$/$$_____| $$__  $$/$$$$$| $$      /$$__  $$/$$__  $$
| $$__  $$ /$$$$$$|  $$$$$$| $$  \ $|______| $$     | $$$$$$$| $$$$$$$$
| $$  | $$/$$__  $$\____  $| $$  | $$      | $$     | $$_____| $$_____/
| $$  | $|  $$$$$$$/$$$$$$$| $$  | $$      | $$$$$$$|  $$$$$$|  $$$$$$$
|__/  |__/\_______|_______/|__/  |__/      |________/\_______/\_______/
                     Created by H@ck3r-SriDh@r                v1.01""")






file=sys.argv[1]
id=sys.argv[2]
status=bcolors.NO + "Not Match" + bcolors.ENDC
#print(bcolors.NO + "Warning:" + bcolors.ENDC)
Found=False

algo={1:'sha3_224', 2:'sha512',3: 'sha224', 4:'sha3_256', 5:'blake2s',6:'shake_256',7:'sha3_512',8:'shake_128',9:'sha384',10:'blake2b',11:'sha3_384',12:'sha1',13:'sha256',14:'md5'}
print(bcolors.OKGREEN + "Hashing Algorithms" + bcolors.ENDC)
for i in algo.keys():
    print(str(i)+"|"+algo[i],end="\n")
#print(algo)
choice=int(input("Enter Your Choice (eg:14):"))
if(choice<=14):
    pass
else:
    print("INVALID HASH OPTION")
    exit()
name=choice
print("______________________________________________")
print(bcolors.HEADER+"[*] Algorithm:"+bcolors.ENDC+algo[name])
print(bcolors.HEADER+"[*] Wordlist :"+bcolors.ENDC+file)
print(bcolors.HEADER+"[*] TaRGET Hash:"+bcolors.ENDC,id)
print("______________________________________________")

d=open("Non-Match.txt","w+")   #creating the rainbow table
f=open(file,'r')

#chioce Assigning
if name == 1:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha3_224(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 2:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha512(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 3:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha224(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 4:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha3_256(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC) 
    d.close()
elif name == 5:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.blake2s(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 6:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.shake_256(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 7:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha3_512(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 8:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.shake_128(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 9:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha384(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 10:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.blake2b(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 11:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha3_384(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 12:
    for data in f:
        print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
        result = h.sha1(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
elif name == 13:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.sha256(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()

elif name == 14:
    print(bcolors.OKGREEN+"started Cracking.."+bcolors.ENDC)
    for data in f:
        result = h.md5(data.encode())
        Final = result.hexdigest()
        print(Final,status)
        sleep(0.01)
        if Final == id:
            print(bcolors.OKBLUE+"Hash Found"+bcolors.ENDC)
            print(bcolors.OKGREEN+"Cracked:"+bcolors.ENDC, data)
            Found = True
            break
        d.write(Final + "\n")
    else:
        print(bcolors.NO+"[*] TaRget Hash Not Found"+bcolors.ENDC)
    d.close()
else:
    print("INVALID HASH OPTION")

if(KeyboardInterrupt):
    exit()


    








