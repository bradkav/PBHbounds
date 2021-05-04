## PBHbounds

[![DOI](https://zenodo.org/badge/220053456.svg)](https://zenodo.org/badge/latestdoi/220053456) [![arXiv](https://img.shields.io/badge/arXiv-2007.10722-B31B1B.svg)](http://arxiv.org/abs/2007.10722) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*A collection of bounds on primordial black holes (PBHs) and code for plotting them.*

 ![Messy summary of all PBH bounds](plots/PBH_bounds.png)


### Bounds

The list of available, tabulated bounds is in the [bounds/](bounds/) folder (see the readme there). The fact that I've included or omitted a particular bound shouldn't be taken as an endorsement or otherwise. I'll leave the user to exercise their own judgement when choosing which bounds are relevant. Note also that some of the bounds plotted above as dashed lines are projections.

If you'd like to add a bound to the repo, you can submit a pull request, create an issue or just contact me directly.

### Plots

Some example plots summarising the bounds are in the [plots/](plots/) folder.

You can produce a plot with
```
python PlotPBHbounds.py -listfile LIST_FILE -outfile OUT_FILE
```
where `LIST_FILE` is a text file containing a list of bounds to be plotted (see `listfiles/list_all.txt` for an example) and `OUT_FILE` is the full filename of the image to be output (e.g. `plots/PBHbounds.pdf`). You can use the short flags `-lf` and `-of` for specifying the list file and output file.

A dark theme (with black background and white text) can be set using the flag `--dark`.

The plot style and some of the bounds are inspired by [arXiv:1801.00808](https://arxiv.org/abs/1801.00808).

Constraints on the primordial power spectrum can be plotted with
```
python PlotPSbounds.py
```
which is roughly inspired by plots from [arXiv:1811.11158](https://arxiv.org/abs/1811.11158), [arXiv:1812.00674](https://arxiv.org/abs/1812.00674) and [arXiv:1909.01593](https://arxiv.org/abs/1909.01593).

### Versions

**Version 1.0 (12/11/2019):** Release version. Created for the first [GW4FP workshop](https://indico.cern.ch/event/843270/) (Amsterdam 2019).

**Updates:**
- 04/05/2021: Added some projected constraints in the asteroid-mass region, as well as a new flag for dark themes.
- 24/03/2021: Added Lyman alpha forest constraint and SKA forecast, shown in [arXiv:2103.12087](https://arxiv.org/abs/2103.12087).
- 13/01/2021: Added code for plotting Power Spectrum constraints (Fig. 1 of PBH review).
- 20/07/2020: Substantial updates, to coincide with PBH review article (more details to follow).
- 07/01/2020: added bounds on PBH evaporation from 511 keV gamma ray line

### Citation

Feel free to use the bounds and code for anything you like, but please link to the repo if you do and cite the DOI: [10.5281/zenodo.3538999](https://doi.org/10.5281/zenodo.3538999).
