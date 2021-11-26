# Data
This repository contains all the datafiles you can use for your own hackathon
projects. 

Good luck!

<img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Rubber_duck.svg" width="50" height="50">

```
The `data` folder with the pre-processed data will be published around 16:00 26-11.
```

## Content

### Raw-data:
The raw data is available on the [FTM repository](https://github.com/ftmnl/asr).
It can be loaded using `scripts\load_data.py`, which loads and stores the
raw data-file to the `data` folder. 

### Split-raw-data:
`split_raw_data.py` splits the raw data downloaded using the `scripts\load_data.py` script mentioned above into a
specified number of parts and can be used as **testing material for your new
pre-processing scripts**.

### Basic-pre-processed-data:
This data can be **useful for the visualization and smart-screening track**. 
However, even if you are in the pre-processing track, you can still use the
data in this reposity as inspiration or even as a starting point. 

The script used for the basic-pre-processing can be found in the
[asreview-ftm-hackathon/Example-for-data-pre-processing-track](https://github.com/asreview-ftm-hackathon/Example-for-data-pre-processing-track)
repository.

> If you choose to use the basic-pre-processed-data as a starting point for the
>  data pre-processing track make sure to do the following:
> 1. Continue or expand on your own copy of the pre-processing-script.
> 2. Credit the original work.

### Split-basic-pre-processed-data:
`split-basic-pre-processed-data.py` splits the pre-processed data from the
`output` folder into a specified amount of parts and can be used as **testing
material for the smart screening track**.

The same goes for the [semantic clustering example](https://github.com/asreview-ftm-hackathon/Example-for-visualization-track)
of the visualization track!
