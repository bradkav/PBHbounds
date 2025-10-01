import numpy as np
from matplotlib import pyplot as plt

alpha_val = 0.15

#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_all.txt" 
outfile_default = "plots/PBH_bounds.png"


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
    
#----------------------------
def load_listfile(listfile):
    bounds = np.loadtxt(listfile, usecols=(0,), dtype=str)
    colors = np.loadtxt(listfile, usecols=(1,), dtype=str)
    lines = np.loadtxt(listfile, usecols=(2,), dtype=str)
    xlist = np.loadtxt(listfile, usecols=(3,))
    ylist = np.loadtxt(listfile, usecols=(4,))
    anglist = np.loadtxt(listfile, usecols=(5,))

    try:
        labellist = np.loadtxt(listfile, usecols=(6,), dtype=str)
    except:
        print("> Problem loading labels in column 6 of listfile. Using boundIDs instead...")
        labellist = bounds
        
    return bounds, colors, lines, xlist, ylist, anglist, labellist
    
#-----------------------------    
def addSIGWprojections(color='red', linestyle='--'):
    plt.fill_between([6.6e-14, 6.6e-12], 5e-3, 1, color=color, alpha = alpha_val, linewidth=0)
    #plt.plot([6.6e-14, 6.6e-12], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.plot([6.6e-14, 6.6e-14], [5e-3, 1], color = color, linestyle=linestyle, lw=1.0)
    plt.plot([6.6e-12, 6.6e-12], [5e-3, 1], color = color, linestyle=linestyle, lw=1.0)
    
    #Rough indication of sensitive mass ranges: see e.g. https://arxiv.org/abs/1810.12218
    plt.text(8e-13, 7e-3, "LISA",fontsize=12, ha='center', va='bottom', rotation = 90)

    #AI/DECIGO
    plt.fill_between([1e-17, 1e-15], 5e-3, 1, color=color, alpha = alpha_val, linewidth=0)
    plt.plot([1e-17, 1e-17], [5e-3, 1], color = color, linestyle=linestyle, lw=1.0)
    plt.plot([1e-15, 1e-15], [5e-3, 1], color = color, linestyle=linestyle, lw=1.0)
    #plt.plot([1e-17, 1e-15], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.text(1e-16, 7e-3, "DECIGO/AI",fontsize=12, ha='center', va='bottom', rotation = 90)
    
    plt.text(1e-14, 4e-3, "SIGWs", fontsize=12, ha='center', va='center')
    
#------------------------------
def addConstraint(boundID, clip=False, color='blue',linestyle='-', 
                    linewidth=1.0, fill = True,
                    x = 1e-30, y=1e-4, labeltext='', **text_kwargs):
    
    m, f = load_bound(boundID)
    
    if fill:
        plt.fill_between(m , f, 1e10, alpha=alpha_val, color=color)
        
    if (clip):
        f = np.clip(f, 0, 1)
    
    plt.plot(m, f, color=color, lw=linewidth, linestyle=linestyle)
    
    if (x > 1e-20):
        plt.text(x, y, labeltext.replace("_", " "), **text_kwargs)

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
    
    
    
#---------------------------------
def setup_axes(ax):
    
    Msun_min, Msun_max = ax.get_xlim()
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.xaxis.tick_bottom()
    ax.xaxis.set_tick_params(pad=5)
    
    xticks = 10**np.arange(np.floor(np.log10(Msun_min)), np.ceil(np.log10(Msun_max))+1)
    ax.set_xticks(xticks, minor=True)
    ax.set_xticklabels([], minor=True)
    
    ax.set_xlabel(r'$M_\mathrm{PBH}$ [$M_\odot$]')
    plt.ylabel(r'$f_\mathrm{PBH} = \Omega_\mathrm{PBH}/\Omega_\mathrm{DM}$')

    ax_top = ax.twiny()
    ax_top.xaxis.tick_top()
    ax_top.set_xscale('log')
    ax_top.set_xlim(ax.get_xlim())
    ax_top.set_xlabel(r'$M_\mathrm{PBH}$ [g]', labelpad=7)

    g_to_Msun = 1/1.989e+33

    g_ticks_minor =  10**np.arange(np.floor(np.log10(Msun_min/g_to_Msun)), np.ceil(np.log10(Msun_max/g_to_Msun))+1)
    g_ticks = g_ticks_minor[::3]

    g_tick_labels = [r"$10^{" + str(int(np.log10(x))) +"}$" for x in g_ticks]

    ax_top.set_xticks(g_ticks*g_to_Msun)
    ax_top.set_xticklabels(g_tick_labels)
    ax_top.xaxis.set_tick_params(pad=0)

    ax_top.set_xticks(g_ticks_minor*g_to_Msun,minor=True)
    ax_top.set_xticklabels([],minor=True)
    