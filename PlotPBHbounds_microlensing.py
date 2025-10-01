import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import tools

#Specify the plot style
mpl.style.use("PBHbounds.mplstyle")
mpl.rcParams.update({'font.size': 14})

#Parse command-line arguments (list file, plot file, and dark theme option)
#-------------------------------------------------------------------------

#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_microlensing.txt" 
outfile_default = "plots/PBHbounds_microlensing_square.pdf"

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


#Load list of bounds from listfile
#---------------------------------
bounds, colors, lines, xlist, ylist, anglist, labellist = tools.load_listfile(listfile)


#Set Dark theme and swap colors if necessary
#------------------------------------------
if (args.dark):
    tools.dark_theme(colors)

#Generate the envelope of bounds
#--------------------------------

Mgrid = np.geomspace(1e-12, 1e5, 1000)
Mgrid, envelope = tools.getEnvelope(bounds, Mgrid, outfile = "Microlensing.txt")

#-------------------------------------------    
    
fig = plt.figure(figsize=(5,5))
 
for i in range(len(bounds)):  
    tools.addConstraint(bounds[i], color = colors[i], x = xlist[i], y = ylist[i], linestyle=lines[i], labeltext=labellist[i], rotation=anglist[i])

#Plot the envelope
plt.plot(Mgrid, envelope, linestyle='--', color='k')

plt.axhspan(1, 1.5, facecolor='grey', alpha=0.7, zorder=5)

xmin = 1e-12
xmax = 1e4
plt.xlim(xmin, xmax)
plt.ylim(1e-4, 1.5)

tools.setup_axes(fig, major_tick_spacing=3, obj_label="CO")

plt.text(0.5, 0.05, "Micro-lensing", va = "bottom", ha = "center", color='C0',  transform=plt.gca().transAxes)

plt.savefig(outfile, bbox_inches='tight')

    
plt.show()






