import numpy as np


def load_bound(boundID):
    if (boundID in ["OGLE"]):
        raise ValueError("boundID <" + boundID  + "> has been deprecated. Please check the bounds/README.md file.")
    
    if (boundID == "OGLE-strict"):
        m, f = np.loadtxt('bounds/OGLE.txt', unpack=True, usecols=(0, 1))
    elif (boundID == "OGLE-MW1"):
        m, f = np.loadtxt('bounds/OGLE.txt', unpack=True, usecols=(0, 2))
    elif (boundID == "OGLE-MW2"):
        m, f = np.loadtxt('bounds/OGLE.txt', unpack=True, usecols=(0, 3))
        
    elif (boundID == "Xrayevap"):
        m, f = np.loadtxt('bounds/Xrayevap.txt', unpack=True, usecols=(0, 4))
        
    elif (boundID in ["Xraylensing-NICER", "Xraylensing-NICER-proj", "Xraylensing-STROBEX-proj", "Xraylensing-Xmu-proj"]):    
        m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True, usecols=(0, 1))
        
    else:
        m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True)
        
    return m, f