""" 
Autor: Francisco Moya 
Fecha: 
Descripción: 
"""

TOKEN = 'sk_b3d97bf38c2eb0081d6666eb'
# GENERAL CONSTANTS THAT MAY BE UPDATED IN THE FUTURE BY OPENALPR
OPENALPR_CLOUD_API_URL = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=eu'
OPENALPR_RESULTS = 'results'
OPENALPR_CANDIDATES = 'candidates'
OPENALPR_VEHICLE = 'vehicle'
OPENALPR_MAKE = 'make'
OPENALPR_MAKE_MODEL = 'make_model'
OPENALPR_COLOR = 'color'


def analyse_results(results):
    plate = results[OPENALPR_RESULTS][0][OPENALPR_CANDIDATES][0]['plate']
    brand = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE][0]['name']
    model = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE_MODEL][0]['name']
    color = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_COLOR][0]['name']
    return plate, brand, model, color
