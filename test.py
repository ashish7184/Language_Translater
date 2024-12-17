
from flask import Flask
from flask import  request
from flask_restful import Api, Resource
from flask_cors import CORS
from googletrans import Translator
import httpx,pandas as pd

#https://pypi.org/project/googletrans/#history   #Use library

timeout = httpx.Timeout(35)



import time
start_time = time.time()



df=pd.read_excel(r'D:\Python Projects\Language_Translator\engasp_23062022.xlsx')
df_data=df['Transaction contents']


#input_value='承認後売上'

#input_value='承認後売上'

#input_value='承認後売上'

#input_value='承認後売上'

#input_value='承認後売上'

# =============================================================================
# input_value='ウェスティンホテル 東京 承認後売上'
# 
# translate_into='en'
# translator = Translator(timeout=timeout)  # initalize the Translator object
# translations = translator.translate(input_value, dest=translate_into)
# text=translations.text
# print(text)
# 
# =============================================================================


count=0
for x in df_data:
    count=count+1
    translate_into='en'
    input_value=x
    #input_value=str(input_value)
    #input_value=input_value.replace("['",'' ) 
    #input_value=input_value.replace("']",'' ) 
    translator = Translator()
    #translator = Translator()
    #translate_into=translate_into
    translations = translator.translate(input_value, dest=translate_into)
    
    
    print(count,":", translations.text)
    
    
print("--- %s seconds ---" % (time.time() - start_time))