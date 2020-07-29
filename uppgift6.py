import codecs
import os

from uppgift1_4 import *
from uppgift5 import *


def hämta_data(antal_kolumner, kolumnnamn_stickprov):
    """ Hämtar data från en CSV-fil som funktionen frågar efter. Tillämpar simpel validering genom att
    räkna antalet kolumner och göra stickprov på ett kolumnnanamn.
    """
    filnamn = input("Ange filnamn: ").strip()
    if os.path.isfile(filnamn):
        with open(filnamn) as fil:
            csv_reader = csv.reader(fil, delimiter=';')
            titelrad = next(csv_reader)
            # Enkel felhantering: kollar antal kolumner och tar ett stickprov på ett kolumnnamn
            if len(titelrad) != antal_kolumner or kolumnnamn_stickprov not in titelrad:
                raise ValueError("Indatafilen verkar ha fel format!")

            inläst_data = [r for r in csv_reader]

            # Användaren får nåt slags feedback
            print(f"Läste in {len(inläst_data)} datarader från filen {filnamn}.")
            return inläst_data
    else:
        raise ValueError(f"{filnamn} är antingen inte en läsbar fil, eller så existerar den inte!")


def spara_analyserad_data(analyserad_data):
    if not analyserad_data:
        raise ValueError("Ingen data att spara. Läs in och analysera först!")

    filnamn = input("Ange filnamn: ").strip()
    # I/O-relaterade fel kommer att kastas uppåt, så ingen felhantering här
    with codecs.open(filnamn, "w", "utf-8") as fil:
        csv_writer = csv.writer(fil, delimiter=';')
        # Header för att göra Excel glad och för att möjliggöra validering av filformat
        csv_writer.writerow(["År", "Total försening", "Samtliga medel", "Samtliga min", "Samtliga max",
                             "Försenade medel", "Försenade min", "Försenade max",
                             "Riktigt försenade medel", "Riktigt försenade min", "Riktigt försenade max"])
        csv_writer.writerows(analyserad_data)


def presentera_data(analyserad_data):
    print(resultat_tabell(analyserad_data))
    plotta_data(analyserad_data)


def skriv_ut_meny():
    print("""
    1. Hämta icke analyserad data
    2. Analysera data
    3. Spara analyserad data
    4. Hämta och presentera analyserad data
    5. Avsluta
""")


sluta = False
trafik_data = []
analyserad_data = []
while not sluta:
    skriv_ut_meny()
    alternativ = input("Välj menyalterantiv (1-5): ").strip()
    try:
        if alternativ == '1':
            trafik_data = hämta_data(antal_kolumner=6, kolumnnamn_stickprov="Kvartal")
        elif alternativ == '2':
            analyserad_data = analysera_data(trafik_data)
            presentera_data(analyserad_data)
        elif alternativ == '3':
            spara_analyserad_data(analyserad_data)
        elif alternativ == '4':
            analyserad_data = hämta_data(antal_kolumner=11, kolumnnamn_stickprov="Samtliga medel")
            # Konvertera allt förutom årtalet till flyttal vid återläsning så att plottningen inte ballar ur
            analyserad_data = [[årsrad[0]] + list(map(float, årsrad[1:])) for årsrad in analyserad_data]
            presentera_data(analyserad_data)
        elif alternativ == '5':
            sluta = True
        else:
            print("Felaktigt menyalternativ!")
    except Exception as e:
        print(f"Ett fel har inträffat: {str(e)}")
