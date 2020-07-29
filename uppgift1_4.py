# Deluppgift1:
# ------------
# Egendefinierade funktioner för medelvärde, största- och minsta värde i en numerisk lista (num_lista)

# Medelvärde:
def mean_value(num_lista):
    if num_lista:
        return sum(num_lista) / len(num_lista)
    raise ValueError('Kan ej beräkna medeltal för en tom lista')


# Största värde:
def max_value(num_lista):
    # Återimplementerar Pythons inbyggda funktion max()
    if num_lista:
        max_varde = num_lista[0]
        for v in num_lista:
            if v > max_varde:
                max_varde = v
        return max_varde
    raise ValueError('Kan ej hitta största värde för en tom lista')

    # Minsta värde:


def min_value(num_lista):
    # Återimplementerar Pythons inbyggda funktion min()
    if num_lista:
        min_varde = num_lista[0]
        for v in num_lista:
            if v < min_varde:
                min_varde = v
        return min_varde
    raise ValueError('Kan ej hitta minsta värde för en tom lista')


# Deluppgift 2:
# -------------
# Läs innehållet i CSV-filen trafikdata.csv och spara dess innehåll i listan trafik_data.
import csv

with open('trafikdata.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')
    # Kastar bort header-raden här. Bättre felhantering i uppgift 6.
    next(csv_reader)
    trafik_data = [r for r in csv_reader]

# Deluppgift 3:
# -------------

# Utför dataanlys på listan trafik_data enligt beskrivning ovan.

# Skriv koden här:
import re

KVARTAL_PER_ÅR = 4

# Kolumner i filen
OFFSET_ÅR = 0
OFFSET_KVARTAL = 1
OFFSET_TOTAL = 2
OFFSET_GENOMSNITTLIG_FÖRSENING = 3
OFFSET_FÖRSENADE = 4
OFFSET_FÖRSENADE_MINST_5 = 5

ANTAL_DATAKOLUMNER = 6


class Årsgruppering:
    """
    Håller ihop data för ett år och möjliggör aggregering.
    """

    def __init__(self, år):
        # Enkel sanity check för årtal som placerar oss kring relevant tidsperiod
        if not re.match(r"^(19\d{2}|2\d{3})$", år):
            raise ValueError(f"Ogiltigt år: {år}")
        self.år = år
        self.total_försening = 0
        self.förseningar_samtliga = []
        self.förseningar_försenade = []
        self.förseningar_minst_fem_plus = []

    def lägg_till_kvartalsrad(self, rad):
        """Lägger till en rad innehållande data för ett kvartal. Gör grundläggande, men ej uttömmande,
        sanity checks på raden, eftersom den inte är typad på något sätt. Emedan kursen inte ställer krav på
        avancerad felhantering, så görs här simplistisk felhantering.
        """

        if len(rad) != ANTAL_DATAKOLUMNER:
            raise ValueError(f"En kvartalsrad förväntas ha {ANTAL_DATAKOLUMNER} kolumner; hade {len(rad)}")
        if rad[OFFSET_ÅR] != self.år:
            raise ValueError(f"Försök att lägga till data för år {rad[OFFSET_ÅR]} i årsgruppering för år {self.år}")
        if not re.match(r"^kvartal [1-4]$", rad[OFFSET_KVARTAL]):
            raise ValueError(f"Andra kolumnen förväntas inneålla ett kvartal; innehöll {rad[OFFSET_KVARTAL]}")
        for kolumn in range(2, ANTAL_DATAKOLUMNER):
            if not rad[kolumn].isnumeric():
                raise ValueError(f"Värdet i kolumn {kolumn} förväntas vara numeriskt; var {rad[kolumn]}")

        # Här vet man de facto inte om minuterna alltid är heltal, men de är det i den fil vi använder.
        self.total_försening += int(rad[OFFSET_TOTAL])
        self.förseningar_samtliga.append(int(rad[OFFSET_GENOMSNITTLIG_FÖRSENING]))
        self.förseningar_försenade.append(int(rad[OFFSET_FÖRSENADE]))
        self.förseningar_minst_fem_plus.append(int(rad[OFFSET_FÖRSENADE_MINST_5]))

    def aggregera(self):
        """ Aggregerar årsdatat till en lista innehållande medel, min och max för de olika förseningstyperna. """

        # Ja, den här kollen är lite trivial, men enkel fehnatering var det...
        if len(self.förseningar_samtliga) != KVARTAL_PER_ÅR:
            raise RuntimeError("Kan inte aggregera, eftersom grupperingen inte innehåller fyra kvartal")

        # Gör allt till floats redan här för att passa det angivna utskriftsformatet
        return [
            self.år,
            float(self.total_försening),
            float(mean_value(self.förseningar_samtliga)),
            float(min_value(self.förseningar_samtliga)),
            float(max_value(self.förseningar_samtliga)),
            float(mean_value(self.förseningar_försenade)),
            float(min_value(self.förseningar_försenade)),
            float(max_value(self.förseningar_försenade)),
            float(mean_value(self.förseningar_minst_fem_plus)),
            float(min_value(self.förseningar_minst_fem_plus)),
            float(max_value(self.förseningar_minst_fem_plus))
        ]

def analysera_data(trafik_data):
    if not trafik_data:
        raise ValueError("Ingen data att analysera!")

    analyserad_data = []
    nuvarande_år = trafik_data[0][0]
    årsgruppering = Årsgruppering(nuvarande_år)
    for rad in trafik_data:
        if rad[0] != nuvarande_år:
            analyserad_data.append(årsgruppering.aggregera())
            nuvarande_år = rad[0]
            årsgruppering = Årsgruppering(nuvarande_år)
        årsgruppering.lägg_till_kvartalsrad(rad)
    analyserad_data.append(årsgruppering.aggregera())

    return analyserad_data

analyserad_data = analysera_data(trafik_data)

# Deluppgift 4:
# -------------

# Skapa resultattabellen.
def formatera_förseningssektion(rubrik, data, startkolumn):
    sektionsrubrik = f"Genomsnittlig försening {rubrik} [min] (baserat på kvartalsvärden)"
    sektion = f"""\n\n{sektionsrubrik}
{'=' * len(sektionsrubrik)}

År      Försening medel         Försening min           Försening max
---------------------------------------------------------------------
"""
    for årsdata in data:
        sektion += f"{årsdata[0]:8}{årsdata[startkolumn]:<24}{årsdata[startkolumn + 1]:<24}{årsdata[startkolumn + 2]:<24}\n"
    return sektion


def resultat_tabell(analyserad_data):
    tabell = """
************************************** R E S U L T A T **************************************
    
Total försening alla tåg [h]
============================
    
År      Försening [h]
----------------------------------\n"""
    for årsdata in analyserad_data:
        tabell += f"{årsdata[0]}\t{årsdata[1]}\n"

    tabell += formatera_förseningssektion("för samtliga tåg", analyserad_data, startkolumn=2)
    tabell += formatera_förseningssektion("av försenade tåg", analyserad_data, startkolumn=5)
    tabell += formatera_förseningssektion("av tåg försenade mer än 5 minuter", analyserad_data, startkolumn=8)
    tabell += "\n" + ("*" * 92)
    return tabell


print(resultat_tabell(analyserad_data))
