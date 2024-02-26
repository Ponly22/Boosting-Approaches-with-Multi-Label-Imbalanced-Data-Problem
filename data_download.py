from ucimlrepo import fetch_ucirepo

def download_data(filename:str)->tuple:
    """
    Script for downloading data from https://archive.ics.uci.edu page
    filename = wine: for wine dataset
    """
    if filename == "wine":
        wine = fetch_ucirepo(id=109)
        return wine.data.features,wine.data.targets
    else:
        print(Exception("Unknown name"))