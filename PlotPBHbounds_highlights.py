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
listfile = "listfiles/bounds_review.txt" 
listfile_all = "listfiles/bounds_all.txt"

#Load list of bounds from listfile
#---------------------------------
bounds, colors, lines, xlist, ylist, anglist, labellist = tools.load_listfile(listfile)
bounds_all, _, lines_all, _, _, _, _ = tools.load_listfile(listfile_all)


#Make the figure and add the bounds
#----------------------------------

for j, boundID in enumerate(bounds_all):
    print("Plotting bound <" + boundID +">...")
    
    scale = 0.7
    fig = plt.figure(figsize=(8*scale,5*scale))

    tbox = dict(facecolor='white', edgecolor='none', boxstyle='round', alpha=0.7)

    for i in range(len(bounds)):  
        tools.addConstraint(bounds[i], color = colors[i], x = xlist[i], y = ylist[i], 
                            linestyle=lines[i],rotation=anglist[i],
                            fontsize=13, zorder=20, weight='bold', c=colors[i])

    tools.addConstraint(boundID, color = 'k', x = xlist[i], y = ylist[i], 
                        linestyle=lines_all[j],rotation=anglist[i], linewidth=3.0,
                        fontsize=13, zorder=20, weight='bold', c=colors[i])

    plt.axhspan(1, 1.5, facecolor='grey', alpha=0.7, zorder=10)

    Msun_min = 1e-18
    Msun_max = 1e4

    plt.xlim(Msun_min, Msun_max)
    plt.ylim(1e-5, 1.5)

    tools.setup_axes(fig, major_tick_spacing=3)

    outfile = "plots/highlights/" + boundID + ".png"

    plt.savefig(outfile, bbox_inches='tight', dpi = 300)
    
    plt.close("all")
