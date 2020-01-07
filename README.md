## PBHbounds

[![DOI](https://zenodo.org/badge/220053456.svg)](https://zenodo.org/badge/latestdoi/220053456) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A collection of bounds on primordial black holes (PBHs) and code for plotting them.*

 ![Messy summary of all PBH bounds](plots/PBH_bounds.png)


### Bounds

The list of available, tabulated bounds is in the [bounds/](bounds/) folder. The fact that I've included or omitted a particular bound shouldn't be taken as an endorsement or otherwise. I'll leave the user to exercise their own judgement when choosing which bounds are relevant.

If you'd like to add a bound to the repo, you can submit a pull request, create an issue or just contact me directly.

### Plots

Some example plots summarising the bounds are in the [plots/](plots/) folder.

You can produce a plot with
```
python PlotPBHbounds.py -listfile LIST_FILE -outfile OUT_FILE
```
where `LIST_FILE` is a text file containing a list of bounds to be plotted (see `listfiles/list_all.txt` for an example) and `OUT_FILE` is the full filename of the image to be output (e.g. `plots/PBHbounds.pdf`). You can use the short flags `-lf` and `-of` for specifying the list file and output file. 

The plot style and some of the bounds are inspired by [arXiv:1801.00808](https://arxiv.org/abs/1801.00808).

### Versions

**Version 1.0 (12/11/2019):** Release version. Created for the first [GW4FP workshop](https://indico.cern.ch/event/843270/) (Amsterdam 2019).

**Updates:** 
- 07/01/2020: added bounds on PBH evaporation from 511 keV gamma ray line

### Citation

Feel free to use the bounds and code for anything you like, but please link to the repo if you do and cite the DOI: [10.5281/zenodo.3538999](https://doi.org/10.5281/zenodo.3538999).
