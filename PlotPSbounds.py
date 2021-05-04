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



#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_PowerSpectrum.txt" 
outfile_default = "plots/PowerSpectrumConstraints.pdf"

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

alpha_val = 0.3
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

           
#    if (x > 1e-20):
#        plt.text(x, y, boundID, rotation=ang, fontsize=12, ha='center', va='center')

#-------------------------------------------    
    
def addConstraint(boundID, col='blue',x = 1e-30,y=1e-4,ang=0, linestyle='-', labeltext='_'):
    m, f = np.loadtxt('bounds/PowerSpectrum/' + boundID + '.txt', unpack=True)
    
    #Let's only fill for colored solid lines
    if ((linestyle == "-") and (col not in ["k", "black"])):
        #If the boundID ends in '2', let's fill down to small values, 
        #rather than filling up to 1 (this gives the Planck and Lyman-alpha regions)
        if (boundID[-1] == "2"):
            plt.fill_between(m , np.clip(f, 0,1), 1e-10, alpha=alpha_val, color=col)
        else:  
            plt.fill_between(m , np.clip(f, 0,1), 1, alpha=alpha_val, color=col)
        
    if (DARKMODE and col in ["k", "black"]):
        col = "w"
        
    linewidth = 1.0
    plt.plot(m, np.clip(f, 0,1), color=col, lw=linewidth, linestyle=linestyle)
    
    if (x > 1e-20):
        plt.text(x, y, labeltext.replace("_", " "), rotation=ang, fontsize=12, ha='center', va='center')
    
plt.figure(figsize=(8,5))

ax1 = plt.gca()

ax1.set_xscale('log')
ax1.set_yscale('log')

ax2=ax1.twiny()

ax2.set_xscale('log')

#Plotting stuff
#plt.axhspan(1, 1.5, facecolor='grey', alpha=0.5)
    
#plt.ylim(1e-10, 1e-1)
#plt.xlim(1e-4, 1e16)

ax1.set_xlim(1e-4, 1e16)
ax1.set_ylim(1e-10, 1e-1)

ax2.set_xlim(1.4e21, 1.4e-19)

ax1.set_xlabel(r'$k$ [${\rm Mpc}^{-1}$]')
ax1.set_ylabel(r'${\cal P}_{\cal R}(k)$')

plt.sca(ax1)

for i in range(len(bounds)):  
    addConstraint(bounds[i], col = colors[i], x = xlist[i], y = ylist[i], ang=anglist[i], linestyle=lines[i], labeltext=labellist[i])


        
ax2.set_xticks([1e21, 1e15, 1e9, 1e3, 1e-3, 1e-9, 1e-15])
ax2.tick_params(axis='x', which='major', pad = 1)
ax2.set_xlabel(r'$M_{\rm H}$ [$M_{\odot}$]', labelpad=7)


plt.savefig(outfile, bbox_inches='tight')
    
plt.show()


