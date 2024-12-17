#%%

from flask import Flask
from flask import  request
from flask_restful import Api, Resource
from flask_cors import CORS
from pygoogletranslation import Translator

#%%
app = Flask(__name__)
CORS(app)
# creating an API object
api = Api(app)
class Language_Translator(Resource):
    def post (self):
        pass
        encoded = request.get_json()  # Get base64 data from API
        #Convert receive data in string 
        translate_into=encoded["translate_into"]
        input_value=encoded["input_value"]
        input_value=str(input_value)
        input_value=input_value.replace("['",'' ) 
        input_value=input_value.replace("']",'' ) 
        translator = Translator()
        translate_into=translate_into
        translations = translator.translate(input_value, dest=translate_into)
        text=translations.text
        return(text)

api.add_resource(Language_Translator,'/Language_Translator')
if __name__ == "__main__":
    app.run(port=5000, debug=True)
    


#%%

