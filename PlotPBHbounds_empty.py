import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import tools

#Specify the plot style
mpl.style.use("PBHbounds.mplstyle")

#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_all.txt" 
outfile_default = "plots/PBH_bounds.png"

#Parse command-line arguments (list file, plot file, and dark theme option)
#-------------------------------------------------------------------------

#Load in the filename with the list of bounds and the output filename
parser = argparse.ArgumentParser(description='...')
parser.add_argument('-lf','--listfile', help='File containing list of bounds to include',
                    type=str, default=tools.listfile_default)
parser.add_argument('-of','--outfile', help='Filename (with extension) of output plot', 
                    type=str, default=tools.outfile_default)
                    
parser.add_argument('-dark', '--dark', dest='dark', action='store_true')
parser.set_defaults(dark=False)

args = parser.parse_args()
listfile = args.listfile
outfile = args.outfile


#Load list of bounds from listfile
#---------------------------------
#bounds, colors, lines, xlist, ylist, anglist, labellist = tools.load_listfile(listfile)


#Set Dark theme and swap colors if necessary
#------------------------------------------
if (args.dark):
    tools.dark_theme()


#Make the figure and add the bounds
#----------------------------------

plt.figure(figsize=(8,5))

ax = plt.gca()

#--------------------
# DO PLOTTING IN HERE
#--------------------

plt.axhspan(1, 1.5, facecolor='grey', alpha=0.5, zorder=10)

Msun_min = 1e-18
Msun_max = 1e4

plt.xlim(Msun_min, Msun_max)
plt.ylim(5e-6, 1.5)

tools.setup_axes(ax)

plt.savefig(outfile, bbox_inches='tight')
    
plt.show()


