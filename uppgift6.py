from trafikdataanalys import ANTAL_DATAKOLUMNER
import csv
import os
def hämta_data():
    filnamn = input("Ange filnamn: ").strip()
    if os.path.isfile(filnamn):
        with open(filnamn) as fil:
            csv_reader = csv.reader(fil, delimiter=';')
            titelrad = next(csv_reader)
            if len(titelrad) != ANTAL_DATAKOLUMNER or "minuter" not in titelrad:
                raise ValueError("Indatafilen verkar ha fel format!")
        return [r for r in csv_reader]
    else:
        raise ValueError(f"{filnamn} är antingen inte en läsbar fil, eller så existerar den inte!")

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
while not sluta:
    skriv_ut_meny()
    alternativ = input("Välj menyalterantiv (1-5): ").strip()
    try:
        if alternativ == '1':
            trafik_data = hämta_data()
        elif alternativ == '2':
            pass
        elif alternativ == '3':
            pass
        elif alternativ == '4':
            pass
        elif alternativ == '5':
            sluta = True
        else:
            print("Falaktigt menyalternativ")
    except Exception as e:
        print(f"Ett fel har inträffat: {str(e)}")




