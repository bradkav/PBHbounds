import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse


#Specify the plot style
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

#General options
plot_SGWB_range = True

#Default values, overridden if you pass in command line arguments
listfile_default = "list_all.txt" 
outfile_default = "PBH_bounds.pdf"

#Load in the filename with the list of bounds and the output filename
parser = argparse.ArgumentParser(description='...')
parser.add_argument('-lf','--listfile', help='File containing list of bounds to include',
                    type=str, default=listfile_default)
parser.add_argument('-of','--outfile', help='Filename (with extension) of output plot', 
                    type=str, default=outfile_default)

args = parser.parse_args()
listfile = "listfiles/" + args.boundsfile
outfile = "plots/" + args.outfile

bounds = np.loadtxt(boundsfile, usecols=(0,), dtype=str)
colors = np.loadtxt(boundsfile, usecols=(1,), dtype=str)
lines = np.loadtxt(boundsfile, usecols=(2,), dtype=str)
xlist = np.loadtxt(boundsfile, usecols=(3,))
ylist = np.loadtxt(boundsfile, usecols=(4,))
anglist = np.loadtxt(boundsfile, usecols=(5,))


def addConstraint(boundID, col='blue',x = 1e-30,y=1e-4,ang=0, linestyle='-'):
    m, f = np.loadtxt('bounds/' + boundID + '.txt', unpack=True)
    if (boundID != "OGLE?"):
        plt.fill_between(m , np.clip(f, 0,1), 1, alpha=0.15, color=col)
    plt.plot(m, np.clip(f, 0,1), color=col, lw=1.0, linestyle=linestyle)
    
    if (x > 1e-20):
        plt.text(x, y, boundID, rotation=ang, fontsize=12, ha='center', va='center')

def addSIGWprojections(col='red', linestyle='--'):
    plt.fill_between([6.6e-14, 6.6e-12], 5e-3, 1, color=col, alpha = 0.15, linewidth=0)
    #plt.plot([6.6e-14, 6.6e-12], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.plot([6.6e-14, 6.6e-14], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([6.6e-12, 6.6e-12], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.text(8e-13, 7e-3, "LISA",fontsize=12, ha='center', va='bottom', rotation = 90)

    #AI/DECIGO
    plt.fill_between([1e-17, 1e-15], 5e-3, 1, color=col, alpha = 0.15, linewidth=0)
    plt.plot([1e-17, 1e-17], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    plt.plot([1e-15, 1e-15], [5e-3, 1], color = col, linestyle=linestyle, lw=1.0)
    #plt.plot([1e-17, 1e-15], [3e-3, 3e-3], 0, color='red', linestyle='--')
    plt.text(1e-16, 7e-3, "DECIGO/AI",fontsize=12, ha='center', va='bottom', rotation = 90)
    
    plt.text(1e-14, 4e-3, "SIGWs", fontsize=12, ha='center', va='center')

#-------------------------------------------    
    
plt.figure(figsize=(8,5))

ax = plt.gca()

ax.set_xscale('log')
ax.set_yscale('log')

for i in range(len(bounds)):  
    if (bounds[i] == "SIGWs"):
        addSIGWprojections(col=colors[i], linestyle=lines[i])
    else:
        addConstraint(bounds[i], col = colors[i], x = xlist[i], y = ylist[i], ang=anglist[i], linestyle=lines[i])



#Plotting stuff
plt.axhspan(1, 1.5, facecolor='grey', alpha=0.5)
    
plt.ylim(1e-3, 1.5)
plt.xlim(1e-18, 1e4)
    
ax.set_xticks(np.logspace(-18, 4, 23),minor=True)
ax.set_xticklabels([], minor=True)
    
plt.xlabel(r'$M_\mathrm{PBH}$ [$M_\odot$]')
plt.ylabel(r'$f_\mathrm{PBH} = \Omega_\mathrm{PBH}/\Omega_\mathrm{DM}$')

plt.savefig(outfile, bbox_inches='tight')
    
#plt.show()


