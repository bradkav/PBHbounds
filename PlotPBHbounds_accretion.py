import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import tools

#Specify the plot style
mpl.rcParams.update({'font.size': 14,'font.family':'serif'})
mpl.rcParams['xtick.major.size'] = 7
mpl.rcParams['xtick.major.width'] = 1
mpl.rcParams['xtick.minor.size'] = 3.5
mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.major.size'] = 7
mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['ytick.minor.size'] = 3.5
mpl.rcParams['ytick.minor.width'] = 1
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['lines.linewidth'] = 1.5
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rc('text', usetex=True)

mpl.rcParams['legend.edgecolor'] = 'inherit'



# Bounds taken from 1801.00808

#General options
plot_SGWB_range = True

#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_accretion.txt" 
outfile_default = "plots/PBHbounds_accretion_square.pdf"

#Load in the filename with the list of bounds and the output filename
parser = argparse.ArgumentParser(description='...')
parser.add_argument('-lf','--listfile', help='File containing list of bounds to include',
                    type=str, default=listfile_default)
parser.add_argument('-of','--outfile', help='Filename (with extension) of output plot', 
                    type=str, default=outfile_default)
                    
parser.add_argument('-dark', '--dark', dest='dark', action='store_true')
parser.set_defaults(dark=False)

args = parser.parse_args()
listfile = args.listfile
outfile = args.outfile

DARKMODE = args.dark

alpha_val = 0.15
if (DARKMODE):
    plt.style.use('dark_background')
    alpha_val = 0.35

bounds = np.loadtxt(listfile, usecols=(0,), dtype=str)
colors = np.loadtxt(listfile, usecols=(1,), dtype=str)
lines = np.loadtxt(listfile, usecols=(2,), dtype=str)
xlist = np.loadtxt(listfile, usecols=(3,))
ylist = np.loadtxt(listfile, usecols=(4,))
anglist = np.loadtxt(listfile, usecols=(5,))
labellist = np.loadtxt(listfile, usecols=(6,), dtype=str)

if (DARKMODE):
    for i, col in enumerate(colors):
        if (col == "C1"):
            colors[i] = "C5"
        if (col == "C2"):
            colors[i] = "C6"


Mgrid = np.geomspace(1e-2, 1e3, 1000)
envelope = 1e10 + 0.0*Mgrid

def addConstraint(boundID, col='blue',x = 1e-30,y=1e-4,ang=0, linestyle='-', labeltext=''):
    m, f = tools.load_bound(boundID)
    if (boundID != "OGLE-hint"):
        plt.fill_between(m , np.clip(f, 0,1), 1, alpha=alpha_val, color=col)
    linewidth = 1.0
    if (boundID in ["Microlensing", "Evaporation"]):
        linewidth=2.0
    plt.plot(m, f, color=col, lw=linewidth, linestyle=linestyle)
    
    if (x > 1e-20):
        plt.text(x, y, labeltext.replace("_", " "), rotation=ang, fontsize=12, ha='center', va='center')

    interped_lim = 10**np.interp(np.log10(Mgrid), np.log10(m), np.log10(f), left=10, right=10)
    envelope[interped_lim < envelope] = interped_lim[interped_lim < envelope]

def addSIGWprojections(col='red', linestyle='--'):
    plt.fill_between([6.6e-14, 6.6e-12], 5e-3, 1, color=col, alpha = alpha_val, linewidth=0)
    #plt.plot([6.6e-14, 6.6e-12], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.plot([6.6e-14, 6.6e-14], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([6.6e-12, 6.6e-12], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.text(8e-13, 7e-3, "LISA",fontsize=12, ha='center', va='bottom', rotation = 90)

    #AI/DECIGO
    plt.fill_between([1e-17, 1e-15], 5e-3, 1, color=col, alpha = alpha_val, linewidth=0)
    plt.plot([1e-17, 1e-17], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([1e-15, 1e-15], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    #plt.plot([1e-17, 1e-15], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.text(1e-16, 7e-3, "DECIGO/AI",fontsize=12, ha='center', va='bottom', rotation = 90)
    
    plt.text(1e-14, 4e-3, "SIGWs", fontsize=12, ha='center', va='center')

#-------------------------------------------    
    
plt.figure(figsize=(5,5))

ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.xaxis.tick_bottom()
ax.xaxis.set_tick_params(pad=5)

for i in range(len(bounds)):  
    if (bounds[i] == "SIGWs"):
        addSIGWprojections(col=colors[i], linestyle=lines[i])
    else:
        addConstraint(bounds[i], col = colors[i], x = xlist[i], y = ylist[i], ang=anglist[i], linestyle=lines[i], labeltext=labellist[i])



#Plotting stuff
plt.axhspan(1, 1.5, facecolor='grey', alpha=0.5)
    
plt.ylim(1e-4, 1.5)

xmin = 1
xmax = 1e3
plt.xlim(xmin, xmax)

ticks_minor = np.geomspace(1e-18, 1e4, 23)
ticks_minor = ticks_minor[(xmin <= ticks_minor) & (ticks_minor <= xmax)]
#print(ticks_minor)
ax.set_xticks(ticks_minor,minor=True)
ax.set_xticklabels([], minor=True)
    
ax.set_xlabel(r'$M_\mathrm{PBH}$ [$M_\odot$]')
plt.ylabel(r'$f_\mathrm{PBH} = \Omega_\mathrm{PBH}/\Omega_\mathrm{DM}$')

ax_top = ax.twiny()
ax_top.xaxis.tick_top()
ax_top.set_xscale('log')
ax_top.set_xlim(ax.get_xlim())
ax_top.set_xlabel(r'$M_\mathrm{PBH}$ [g]', labelpad=7)

g_to_Msun = 1/1.989e+33

g_ticks_minor = np.geomspace(1e15, 1e37, 23)
g_ticks_minor = g_ticks_minor[(xmin <= g_to_Msun*g_ticks_minor) & (g_to_Msun*g_ticks_minor <= xmax)]
g_ticks = g_ticks_minor


g_tick_labels = [r"$10^{" + str(int(np.log10(x))) +"}$" for x in g_ticks]

ax_top.set_xticks(g_ticks*g_to_Msun)
ax_top.set_xticklabels(g_tick_labels)
ax_top.xaxis.set_tick_params(pad=0)

ax_top.set_xticks(g_ticks_minor*g_to_Msun,minor=True)
ax_top.set_xticklabels([],minor=True)

ax.text(0.45, 0.05, "Accretion", va = "bottom", ha = "center", color='C3',  transform=ax.transAxes, fontsize=16)

#Plot the envelope
plt.plot(Mgrid, envelope, linestyle='--', color='k')

plt.savefig(outfile, bbox_inches='tight')
    
#Save envelope to file
headertxt = "Envelope of accretion bounds: " + ", ".join(bounds)
headertxt += "\n Columns: PBH mass [Muns], PBH fraction f_PBH"
np.savetxt("bounds/Accretion.txt", np.c_[Mgrid, envelope], header=headertxt)
    
plt.show()


