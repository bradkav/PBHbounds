## List Files

Here are some examples of 'list files'. Each file is a list of bounds to be plotted (and how it should be plotted). List files are passed to the `PlotPBHbounds.py` code with the flag `-lf`. 

The different columns are:
`BoundID`, `colour`, `linestyle`, `x`, `y`, `rotation`.

`colour` and `linestyle` specify the properties of the plotted region, while `x`, `y` and `rotation` specify the position and orientation of the label.

The list of `BoundID`s is [here](https://github.com/bradkav/PBHbounds/tree/master/bounds). An example list file is given in (bounds_all.txt)[https://github.com/bradkav/PBHbounds/tree/master/listfiles/bounds_all.txt], which has all the currently included bounds.