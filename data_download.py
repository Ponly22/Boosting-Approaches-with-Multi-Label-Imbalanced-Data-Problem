from ucimlrepo import fetch_ucirepo

def download_data(filename:str)->tuple:
    """
    Script for downloading data from https://archive.ics.uci.edu/dataset page
    filename = wine: for wine dataset
    filename = Convertype: for contvertype dataset
    """
    if filename == "wine":
        wine = fetch_ucirepo(id=109)
        return (wine.data.features,wine.data.targets)
    if filename == "Contraceptive":
        contraceptive_method_choice = fetch_ucirepo(id=30) 
        return (contraceptive_method_choice.data.featues,contraceptive_method_choice.data.targets)
    if filename == "convertype":
        covertype = fetch_ucirepo(id=31) 
        return (covertype.data.features,covertype.data.targets)
    else:
        print(Exception("Unknown name"))
    

