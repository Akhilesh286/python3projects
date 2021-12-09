import os 
url1 = str ( input ('url>>>'))
url = 'view-source:'+url1
os.system (f'termux-open-url {url}')