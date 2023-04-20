""" 
Autor: Francisco Moya 
Fecha: 
Descripción: 
"""

TOKEN = 'YOUR_TOKEN_HERE'
# General constants 
OPENALPR_CLOUD_API_URL = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=eu'
OPENALPR_RESULTS = 'results'
OPENALPR_CANDIDATES = 'candidates'
OPENALPR_VEHICLE = 'vehicle'
OPENALPR_MAKE = 'make'
OPENALPR_MAKE_MODEL = 'make_model'
OPENALPR_COLOR = 'color'

# Function to get the image results
def analyse_results(results):
    plate = results[OPENALPR_RESULTS][0][OPENALPR_CANDIDATES][0]['plate']
    brand = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE][0]['name']
    model = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE_MODEL][0]['name']
    color = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_COLOR][0]['name']
    return plate, brand, model, color
