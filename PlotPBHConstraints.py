import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 16,'font.family':'serif'})

mpl.rcParams['xtick.major.size'] = 7
mpl.rcParams['xtick.major.width'] = 1
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.major.size'] = 7
mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['ytick.minor.size'] = 3
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


def addConstraint(boundID, col='blue',x = 1e-30,y=1e-4,ang=0, linestyle='-'):
    m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True)
    plt.fill_between(m , np.clip(f, 0,1), 1, alpha=0.15, color=col)
    plt.plot(m, np.clip(f, 0,1), color=col, lw=1.5, linestyle=linestyle)
    
    if (x > 1e-20):
        plt.text(x, y, boundID, rotation=ang, fontsize=12, ha='center', va='center')


bounds = np.loadtxt("bounds_list.txt", usecols=(0,), dtype=str)
colors = np.loadtxt("bounds_list.txt", usecols=(1,), dtype=str)
lines = np.loadtxt("bounds_list.txt", usecols=(2,), dtype=str)
xlist = np.loadtxt("bounds_list.txt", usecols=(3,))
ylist = np.loadtxt("bounds_list.txt", usecols=(4,))
anglist = np.loadtxt("bounds_list.txt", usecols=(5,))
#bounds = ["CMB", "ERI-II", "EROS", "evap", "FL", "HSC", "K", "M", "NS", "SNe", "WD"]



#plot_LIGO = False
plot_OGLE_hint = True
plot_SGWB_range = True
    
    
plt.figure(figsize=(8,5))

ax = plt.gca()

ax.set_xscale('log')
ax.set_yscale('log')

#addConstraint("CMB",x = xlist[0], y = ylist[0], ang = anglist[0])

for i in range(len(bounds)):    
    addConstraint(bounds[i], col = colors[i], x = xlist[i], y = ylist[i], ang=anglist[i], linestyle=lines[i])


if (plot_OGLE_hint):
    m, f = np.loadtxt('bounds/OGLE-hint.txt', unpack=True)
    plt.plot(m, f, color = 'k', linestyle=':', lw=1.5)
    
    plt.text(1e-5, 2.2e-2, "OGLE?", fontsize=12, ha='center', va='center', rotation=-75)
    #plt.fill(m, f, 1, )

if (plot_SGWB_range):
    #LISA
    plt.fill_between([6.6e-14, 6.6e-12], 5e-3, 1, color='red', alpha = 0.15, linewidth=0)
    #plt.plot([6.6e-14, 6.6e-12], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.plot([6.6e-14, 6.6e-14], [5e-3, 1], color = 'red', linestyle='--', lw=1.5)
    plt.plot([6.6e-12, 6.6e-12], [5e-3, 1], color = 'red', linestyle='--', lw=1.5)
    plt.text(8e-13, 7e-3, "LISA",fontsize=12, ha='center', va='bottom', rotation = 90)

    #AI/DECIGO
    plt.fill_between([1e-17, 1e-15], 5e-3, 1, color='red', alpha = 0.15, linewidth=0)
    plt.plot([1e-17, 1e-17], [5e-3, 1], color = 'red', linestyle='--', lw=1.5)
    plt.plot([1e-15, 1e-15], [5e-3, 1], color = 'red', linestyle='--', lw=1.5)
    #plt.plot([1e-17, 1e-15], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.text(1e-16, 7e-3, "DECIGO/AI",fontsize=12, ha='center', va='bottom', rotation = 90)
    
    plt.text(1e-14, 4e-3, "SIGWs", fontsize=12, ha='center', va='center')

plt.axhspan(1, 1.5, facecolor='grey', alpha=0.5)
    
plt.ylim(1e-3, 1.5)
plt.xlim(1e-18, 1e4)
    
ax.set_xticks(np.logspace(-18, 4, 23),minor=True)
ax.set_xticklabels([], minor=True)
    
plt.xlabel(r'$M_\mathrm{PBH}$ [$M_\odot$]')
plt.ylabel(r'$f_\mathrm{PBH} = \Omega_\mathrm{PBH}/\Omega_\mathrm{DM}$')

outfile_name = "PBHbounds"

plt.savefig("plots/" + outfile_name + ".pdf", bbox_inches='tight')
    
#plt.show()


