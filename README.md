## PBHbounds

[![DOI](https://zenodo.org/badge/220053456.svg)](https://zenodo.org/badge/latestdoi/220053456) [![arXiv](https://img.shields.io/badge/arXiv-2007.10722-B31B1B.svg)](http://arxiv.org/abs/2007.10722) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A collection of bounds on primordial black holes (PBHs) and code for plotting them.*

 ![Messy summary of all PBH bounds](plots/PBH_bounds.png)


### Bounds

The list of available, tabulated bounds is in the [bounds/](bounds/) folder (see the readme there). The fact that I've included or omitted a particular bound shouldn't be taken as an endorsement or otherwise. I'll leave the user to exercise their own judgement when choosing which bounds are relevant. Note also that some of the bounds plotted above as dashed lines are projections.

### Contributing

If you'd like to add a bound to the repo, there are a few options:
1. Make the changes yourself:
	* Add the new bound as a `.txt` file in the [bounds/](bounds/) folder. Each file should have two columns, corresponding to the PBH mass in Solar mass, and the constraint on the PBH fraction. Also include a comment at the top of the file giving a link to the source of the bound.  
	* Update the [bounds/README.md](https://github.com/bradkav/PBHbounds/blob/master/bounds/README.md) file with information about the new bound.
	* Submit a pull request
2. Create an issue here on the github repo, pointing to the paper/bound which is missing.  
3. Contact me directly at bradkav@gmail.com and let me know which bound you think should be added.

### Plots

Some example plots summarising the bounds are in the [plots/](plots/) folder.

You can see the basic functioning of the code in the example notebook here: [PBHboundsNotebook.ipynb](PBHboundsNotebook.ipynb). There, you can add constraints one-by-one according to the `boundID`s listed in the readme of the [bounds/](bounds/) folder. It's also straightforward to adjust the line styles and text labels in this notebook view. 

In practice, for a large number of bounds, it can be more sensible to provide a list of bounds. You can produce a plot with
```
python PlotPBHbounds.py -listfile LIST_FILE -outfile OUT_FILE
```
where `LIST_FILE` is a text file containing a list of bounds to be plotted (see `listfiles/list_all.txt` for an example) and `OUT_FILE` is the full filename of the image to be output (e.g. `plots/PBHbounds.pdf`). You can use the short flags `-lf` and `-of` for specifying the list file and output file.

A dark theme (with black background and white text) can be set using the flag `--dark`.

There are several preset scripts for plotting collected limits from Accretion, GWs, etc. There is also an 'empty' script if you want to plot from scratch using the tools. 

The plot style and some of the bounds are inspired by [arXiv:1801.00808](https://arxiv.org/abs/1801.00808).

#### Primordial Power Spectrum

Constraints on the primordial power spectrum can be plotted with
```
python PlotPSbounds.py
```
which is roughly inspired by plots from [arXiv:1811.11158](https://arxiv.org/abs/1811.11158), [arXiv:1812.00674](https://arxiv.org/abs/1812.00674) and [arXiv:1909.01593](https://arxiv.org/abs/1909.01593).

### Versions

**Version 1.0 (12/11/2019):** Release version. Created for the first [GW4FP workshop](https://indico.cern.ch/event/843270/) (Amsterdam 2019).

A list of updates and recently added bounds can be found here: [UPDATES.md](UPDATES.md)

### Citation

Feel free to use the bounds and code for anything you like, but please link to the repo if you do and cite the DOI: [10.5281/zenodo.3538999](https://doi.org/10.5281/zenodo.3538999).

An list of papers (probably incomplete) using the PBHbounds code can be found here: [PAPERS.md](PAPERS.md). Please also get in touch to let me know you've used the code. That way I can keep track! Thanks.










