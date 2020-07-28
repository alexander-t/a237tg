import matplotlib.pyplot as plt

from uppgift1_4 import analyserad_data


def plotta_total_försening_per_år(år, minuter):
    plt.title(f"Total försening per år för alla tåg under åren {år[0]}-{år[-1]}.")
    plt.grid()
    plt.xlabel("År")
    plt.ylabel("Timmar [h]")
    plt.plot(år, minuter)
    plt.show()


def plotta_medel_min_max_med_rubrik_per_år(delrubrik, år, medel, min, max):
    """
    Plottar tre serier: medeltal samt min- och max-värde. Stoppar in den specificerade delrubriken i grafens
    huvudrubrik, som säger att det rör sig om en försening.
    """
    plt.title(f"Genomsnittlig försening per år för {delrubrik} under åren {år[0]}-{år[-1]}.")
    plt.grid()
    plt.xlabel("År")
    plt.ylabel("Minuter [min]")
    plt.plot(år, medel, color='blue', linestyle='dashed', label='Medel')
    plt.plot(år, min, color='green', label='Min')
    plt.plot(år, max, color='red', label='Max')
    plt.legend()
    plt.show()


def plotta_genomsnittlig_försening_för_alla_tåg(analyserad_data):
    plotta_medel_min_max_med_rubrik_per_år("alla tåg",
                                           [ad[0] for ad in analyserad_data],
                                           [ad[2] for ad in analyserad_data],
                                           [ad[3] for ad in analyserad_data],
                                           [ad[4] for ad in analyserad_data])


def plotta_genomsnittlig_försening_för_försenade_tåg(analyserad_data):
    plotta_medel_min_max_med_rubrik_per_år("försenade tåg",
                                           [ad[0] for ad in analyserad_data],
                                           [ad[5] for ad in analyserad_data],
                                           [ad[6] for ad in analyserad_data],
                                           [ad[7] for ad in analyserad_data])


def plotta_genomsnittlig_försening_för_riktigt_försenade_tåg(analyserad_data):
    plotta_medel_min_max_med_rubrik_per_år("tåg försenade mer än 5 minuter",
                                           [ad[0] for ad in analyserad_data],
                                           [ad[8] for ad in analyserad_data],
                                           [ad[9] for ad in analyserad_data],
                                           [ad[10] for ad in analyserad_data])


def plotta_data(analyserad_data):
    """
    Skapar fyra grafer baserade på parametern analyserad_data, som innehåller förseningsdata per år.
    """

    # För att hantera de lite längre rubrikerna
    plt.rcParams.update({'font.size': 8})

    if analyserad_data:
        år = [ad[0] for ad in analyserad_data]
        minuter = [ad[1] for ad in analyserad_data]
        plotta_total_försening_per_år(år, minuter)

        plotta_genomsnittlig_försening_för_alla_tåg(analyserad_data)
        plotta_genomsnittlig_försening_för_försenade_tåg(analyserad_data)
        plotta_genomsnittlig_försening_för_riktigt_försenade_tåg(analyserad_data)


plotta_data(analyserad_data)
