<h1 align="center">Download Data from GOES-17/GOES-16</h1>
<br>
<p align="center">Code created based on ready script from <b><a target="_blank" href="https://gist.github.com/blaylockbk/d60f4fce15a7f0475f975fc57da9104d#file-download_goes_aws-py">Brian Blaylock</a></b>. 
I added lines to help with the continuous data download, there is still a lot to be added. In case of lack of data the library itself returns an error message and for the download.</p>
<p>First you have to specify the satellite on which you will download the data, then say the year, day and time for it to start downloading from that date</p>
<p>Requires <b><a target="_blank" href="https://s3fs.readthedocs.io/en/latest/">s3fs</a></b></p>
<p>In Anaconda, download via conda-forge.</p>
Link of site where data is downloaded: <a target="_blank" href="http://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/generic_AWS_download.cgi?DATASET=noaa-goes16">Click Here</a>
