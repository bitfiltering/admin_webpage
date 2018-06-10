#This script parses a network device's admin webpage. It locates the model and firmware version.
#Usage-
#$>python get.device.admin.info.py
#
#
#
#
import urllib2
import ssl
import re



##########Bypass invalid SSL certs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





##########URL of admin web page. Uncomment appropriate url for your setup.
#ABC
#url = 'https://192.168.1.1'


#DEF
#url = 'http://192.168.1.1'


#GHI
#url = 'http://192.168.1.2'






#Connect to URL and read page.
response = urllib2.urlopen(url, context=ctx)
content = response.read()








###########Parse firmware version.
#Needs a regex format.
getVerRaw = (re.findall(r'ver=.*\d', content, re.IGNORECASE))

#Convert results to a string.
getVerString = str(getVerRaw)

#Strip out extra characters.
getVer = re.sub('[\[\]]','',getVerString)
getVerA = re.sub('ver=','',getVer)
OsVer = getVerA.strip('\'')





#import pdb;pdb.set_trace()





###########Locate device model.
models = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'PPP', 'QQQ']



#Temporary list to handle non-standard HTML.
modelsTemp = []

#Character prepended to each model value.
gt = ">"


for i in models:
    i = gt + i
    modelsTemp.append(i)




for m in modelsTemp:
    modelSearch = m
    modelSearchResults = re.findall(modelSearch, content, re.IGNORECASE)
    for n in modelSearchResults:
        modelSearchResultsPretty = n.strip('[>]')
        print ("Model is " + modelSearchResultsPretty)




############If model not found, then try search_strings[].
if modelSearchResultsPretty:
    print "Firmware version is",osVer
    exit
else:
    search_strings = ["AAAA","BBBB","CCCC","DDDD"]    
    if s in content:
        print ("[" + s + "]")
        print "Firmware version is",osVer


quit()


