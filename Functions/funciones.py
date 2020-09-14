import pandas as pd
import numpy as np
import requests
import regex as re
import matplotlib.pyplot as plt
import seaborn as sns
import argparse



def clean():
    """
    In this function we clean up our database
    """
    import pandas as pd
    test = pd.read_csv("Input/dato.csv")
    test["NA_Sales"]= test["NA_Sales"].apply(lambda x: x.replace(",","."))
    test["EU_Sales"]=test["EU_Sales"].apply(lambda x: x.replace(",","."))
    test["JP_Sales"]=test["JP_Sales"].apply(lambda x: x.replace(",","."))
    test["Other_Sales"]=test["Other_Sales"].apply(lambda x: x.replace(",","."))
    test["Global_Sales"]=test["Global_Sales"].apply(lambda x: x.replace(",","."))
    test["NA_Sales"]=[float(x) for x in test["NA_Sales"]]
    test["EU_Sales"]=[float(x) for x in test["EU_Sales"]]
    test["JP_Sales"]=[float(x) for x in test["JP_Sales"]]
    test["Other_Sales"]=[float(x) for x in test["Other_Sales"]]
    test["Global_Sales"]=[float(x) for x in test["Global_Sales"]]
    return test

test = clean()

def releasedate(x=3498):
    """
    We obtain the release date of any game
    Some ID number examples: 3498,4200,3328,5286,5679,12020,802,4062,13536,3439,4291
    """
    url= f"https://api.rawg.io/api/games/{x}"
    res = requests.get(url)
    result = res.json()
    print(result["name"])
    return result["released"]

def apis(x):
    """
    This function is to automatize the request to the API
    """
    url=f"https://api.rawg.io/api/games/{x}"
    response = requests.get(url)
    results= response.json()
    return results

def gamestatistics(x):
    """
    This function returns the statistics of a certain game.
    You have to insert the ID number of this game
    Some ID number examples: 3498,4200,3328,5286,5679,12020,802,4062,13536,3439,4291
    """
    result = apis(x)
    rating = result["rating"]
    name = result["name"]
    print(f"{name} has a rating of {rating}")
    website=result["website"]
    print(f"In order to visit the website, enter the following link {website}")

def platforms(idnumber):
    """
    This function returns specifications for each console, the id number can be found in the list below:
    [PS2 = 15; X360 = 14; PS3 = 16; X= 180; Wii = 11; DS = 9; PSP = 17; PS4 = 18; GBA = 24; XONE= 1; 3DS= 8;
    PS = 27; PSV= 19; WiiU= 10]
    """
    res = requests.get(f"https://api.rawg.io/api/platforms/{idnumber}")
    results = res.json()
    name = results["name"]
    print(f"The name of the platform is {name}")
    games = results["games_count"]
    print(f"The total games on this platform is {games}")
    desc = results["description"]
    a = input("Do you want a description of this platform? (Y/N)")
    if a == "Y":
        print(f"{desc}")
    else:
        print("Okay MR.I HAVE NO TIME!")

def regionsales(x):
    """
    This functios gives us the total sales of the three major gaming regions.
    Please enter the region inside a string, e.g regionsales("EU")
    Regions = "EU", "JP", "NA"
    """
    a =  test[f"{x}_Sales"].sum()
    print(f"{x} has a total of {a} sales (In Millions)")

def parse():
    '''
    We define the arguments to parse
    '''
    parser = argparse.ArgumentParser(description='Programa para la inmersión en los videojuegos')
    parser.add_argument('-s', dest='nombre',
                        default='jugador desconocido',
                        required=True,
                        help="Añade tu nombre aqui")
    group = parser.add_mutually_exclusive_group()                   
    group.add_argument('-p', dest='Plataforma',
                        default=None,
                        required=False, 
                        help='La plataforma de la cual queremos info, e.g 18')
    group.add_argument('-j', dest='Juego',
                        default=None,
                        required=False, 
                        help='El juego del cual queremos saber más, e.g 3498')
    group.add_argument('-r', dest='Region',
                        default="EU",
                        required=False,
                        help="Región de la cual queremos saber sus ventas totales, eg EU ")
                        
    args = parser.parse_args()
    return args