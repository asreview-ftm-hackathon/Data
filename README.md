# Data
This repository contains all the datafiles you can use for your own hackathon
projects.

Good luck!

<img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Rubber_duck.svg" width="50" height="50">

## Content

### raw-data:
The raw data is available on the [FTM repository](https://github.com/ftmnl/asr),
it can be loaded using `scripts\load_data.py`. This script loads and stores the
file to the `data` folder. 

### split-raw-data:
`split_raw_data.py` splits the loaded data from the `data` folder into a
specified amount of parts and can be used as testing material for your new
preprocessing scripts.

### basic-pre-processed-data:
Preliminary preprocessing can be found in the
[asreview-ftm-hackathon/Example-for-data-pre-processing-track](https://github.com/asreview-ftm-hackathon/Example-for-data-pre-processing-track)
reporsitory. Even if you are in the pre-processing track, you can still use the
data in this reposity as inspiration or even as a starting point. 

> If you choose to use the basic-pre-processed-data as a starting point for the
>  data pre-processing track make sure to do the following:
> 1. Continue or expand on your own copy of the pre-processing-script.
> 2. Credit the original work.

### split-basic-pre-processed-data:
`split-basic-pre-processed-data.py` splits the preprocessed data from the
`output` folder into a specified amount of parts and can be used as testing
material for the smart screening track.

The same goes for the [semantic clustering example](https://github.com/asreview-ftm-hackathon/Example-for-visualization-track)
of the visualization track!
