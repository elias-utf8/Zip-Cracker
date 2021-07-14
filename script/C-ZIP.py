import zipfile
from tqdm import tqdm
import time
from colorama import Fore, Back, Style
import sys  
import random 

print(" ,-----.       ,-------.,--.,------.")                   
time.sleep(0.2)                                   
print("'  .--./,-----.`--.   / |  ||  .--. '")
time.sleep(0.2)
print("|  |    '-----'  /   /  |  ||  '--' | ")
time.sleep(0.2)
print("'  '--'\        /   `--.|  ||  | --' ")
time.sleep(0.2)
print(" `-----'       `-------'`--'`--' ")


for i in range(10): 
    sys.stdout.write("|{0}|   \r".format('█' * (i+1) + ' ' * (6 - i))) 
    sys.stdout.flush() 
    time.sleep(random.random()) 
                           

print(Fore.GREEN + "\n [+] load ")
print(Style.RESET_ALL)
time.sleep(1)


zip_file = input("Please enter directory of zip file :")
wordlist = input( "Please enter directory of dictionary file :")

choix = input(f'\n Do you want to start the process on the zip file  O/n    ' )      
if choix == 'O':                               
    #zip file
    zip_file = zipfile.ZipFile(zip_file)
    # count the number of words in this wordlist
    n_words = len(list(open(wordlist, "rb")))
    # print the total number of passwords
    print("Total passwords to test:", n_words)


    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print(Fore.GREEN + ' [+] Password found: ', word.decode().strip())
                print(Style.RESET_ALL)
                exit(0)
    print(Fore.RED + '[!] Password not found, try other wordlist.')
    print(Style.RESET_ALL)
    
if choix == 'n' :
    print('\033[32m' + '[-] Process canceled')
   
    