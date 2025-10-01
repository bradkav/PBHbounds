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
        
    elif (boundID == "LIGO-SGWB-O1-O2-O3"):
        m, f = np.loadtxt('bounds/LIGO-SGWB-O1-O2-O3.txt', unpack=True, usecols=(0, 1))
        
    elif (boundID == "Xrayevap"):
        m, f = np.loadtxt('bounds/Xrayevap.txt', unpack=True, usecols=(0, 4))
        
    elif (boundID in ["Xraylensing-NICER", "Xraylensing-NICER-proj", "Xraylensing-STROBEX-proj", "Xraylensing-Xmu-proj"]):    
        m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True, usecols=(0, 1))
        
    elif (boundID == "LyaEvap-Saha2024"):
        m, f = np.loadtxt('bounds/LyaEvap-Saha2024_conservative.txt', unpack=True, usecols=(0, 1))
        
    else:
        m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True)
        
    return m, f
    
#-----------------------------    
def addSIGWprojections(col='red', linestyle='--'):
    plt.fill_between([6.6e-14, 6.6e-12], 5e-3, 1, color=col, alpha = alpha_val, linewidth=0)
    #plt.plot([6.6e-14, 6.6e-12], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.plot([6.6e-14, 6.6e-14], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([6.6e-12, 6.6e-12], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    
    #Rough indication of sensitive mass ranges: see e.g. https://arxiv.org/abs/1810.12218
    plt.text(8e-13, 7e-3, "LISA",fontsize=12, ha='center', va='bottom', rotation = 90)

    #AI/DECIGO
    plt.fill_between([1e-17, 1e-15], 5e-3, 1, color=col, alpha = alpha_val, linewidth=0)
    plt.plot([1e-17, 1e-17], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([1e-15, 1e-15], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    #plt.plot([1e-17, 1e-15], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.text(1e-16, 7e-3, "DECIGO/AI",fontsize=12, ha='center', va='bottom', rotation = 90)
    
    plt.text(1e-14, 4e-3, "SIGWs", fontsize=12, ha='center', va='center')
    
#------------------------------
def addConstraint(boundID, col='blue',x = 1e-30,y=1e-4,
                    ang=0, linestyle='-', labeltext='', 
                    clip=False, textbox = False):
    m, f = tools.load_bound(boundID)
    if (boundID != "OGLE-hint"):
        plt.fill_between(m , f, 1e10, alpha=alpha_val, color=col)
    linewidth = 1.0
    if (clip):
        f = np.clip(f, 0, 1)
    plt.plot(m, f, color=col, lw=linewidth, linestyle=linestyle)
    
    if (x > 1e-20):
        if (textbox):
            tbox = dict(facecolor='white', edgecolor='none', boxstyle='round', alpha=0.7)
        else:
            tbox = None
        plt.text(x, y, labeltext.replace("_", " "), rotation=ang, fontsize=12, ha='center', va='center', bbox=tbox)

#--------------------------------
def getEnvelope(bounds, outfile = None):
    Mgrid = np.geomspace(1e-12, 1e5, 1000)
    envelope = 1e10 + 0.0*Mgrid

    for boundID in bounds:
        m, f = tools.load_bound(boundID)
        
        interped_lim = 10**np.interp(np.log10(Mgrid), np.log10(m), np.log10(f), left=10, right=10)
        envelope[interped_lim < envelope] = interped_lim[interped_lim < envelope]
        
    if outfile is not None:
        headertxt = "Envelope of bounds: " + ", ".join(bounds)
        headertxt += "\n Columns: PBH mass [Muns], PBH fraction f_PBH"
        np.savetxt("bounds/" + outfile, np.c_[Mgrid, envelope], header=headertxt)
        
    return Mgrid, envelope