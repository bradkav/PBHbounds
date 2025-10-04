import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import tools

#Specify the plot style
mpl.style.use("PBHbounds.mplstyle")


#Parse command-line arguments (list file, plot file, and dark theme option)
#-------------------------------------------------------------------------

#Default values, overridden if you pass in command line arguments
listfile_default = "listfiles/bounds_review.txt" 
outfile_default = "plots/PBHbounds_review.pdf"

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


#Make the figure and add the bounds
#----------------------------------

scale = 0.7
fig = plt.figure(figsize=(8*scale,5*scale))

tbox = dict(facecolor='white', edgecolor='none', boxstyle='round', alpha=0.7)

for i in range(len(bounds)):  
    tools.addConstraint(bounds[i], color = colors[i], x = xlist[i], y = ylist[i], 
                        linestyle=lines[i], labeltext=labellist[i], rotation=anglist[i],
                        fontsize=13, zorder=20, weight='bold', bbox=tbox, c=colors[i])


plt.axhspan(1, 1.5, facecolor='grey', alpha=0.7, zorder=10)

Msun_min = 1e-18
Msun_max = 1e4

plt.xlim(Msun_min, Msun_max)
plt.ylim(1e-5, 1.5)

tools.setup_axes(fig, major_tick_spacing=3)

plt.savefig(outfile, bbox_inches='tight', dpi = 300)
    
plt.show()
