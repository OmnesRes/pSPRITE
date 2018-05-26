# pSPRITE
The code in this repository is for Python 2.7, uses NumPy 1.11 and Matplotlib 1.5.

This repository contains the code for pSPRITE, as well as the code and SVG files for the figures of "Recovering data from summary statistics: Sample Parameter Reconstruction via Iterative TEchniques SPRITE)"

-The figure numbers don't match the publication due to figures getting rearranged during drafting of the paper.

Once pSPRITE.py is loaded, these are the parameters of the SPRITE function:
SPRITE(u,mean_decimals,sd,sd_decimals,n,min_value,max_value,restrictions=[],random_start="Yes",min_start="No")

A simple call would be:
SPRITE(3.00,2,2.00,2,10,1,7)

And the output will be of this format:
['solution', {1: 2, 2: 3, 3: 3, 4: 0, 5: 0, 6: 1, 7: 1}]

If no solution is found, the SD of the closest solution will be at the end of the list.

restrictions are optional, do not have to be the same number, and can be outside the scale

random_start will force pSPRITE to start from a randomly generated distribution (unless restrictions are present)

min_start will force pSPRITE to start from the distribution with the smallest SD (unless restrictions are present)

