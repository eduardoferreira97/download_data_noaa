# Brian Blaylock
# Modificado por Eduardo José para baixar um série temporal 
# Requres `s3fs`
# Website: https://s3fs.readthedocs.io/en/latest/
# In Anaconda, download via conda-forge.
#  Página usada para baixar os dados caso queira baixar diretamente: http://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/generic_AWS_download.cgi?DATASET=noaa-goes16&BUCKET=
import s3fs
import numpy as np

# Use the anonymous credentials to access public data
fs = s3fs.S3FileSystem(anon=True)

# List contents of GOES-16 bucket.
fs.ls('s3://noaa-goes16/')
# print(fs.ls('s3://noaa-goes16/'))

# List specific files of GOES-17 CONUS data (multiband format) on a certain hour
###NÃO MEXER###
zero=0   ######
###############

hour = 5
day = 290
year = 2020
satelite ='ABI-L2-DSRF'

while(day <= 365):

    if(day <=9):

         while(hour <= 24):

            if(hour <= 9 and hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(zero)+''+str(zero)+''+str(day)+'/'+str(zero)+''+str(hour)+'/'+'/'))
                print(files)

            elif(hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(zero)+''+str(zero)+''+str(day)+'/'+str(hour)+'/'))
                print(files)
            
            if(hour == 24):
                hour=00
                break
            
            else:
                hour+=1
            
            # Download the first file, and rename it the same name (without the directory structure)
            fs.get(files[0], files[0].split('/')[-1])

    elif(day >= 10 and day < 100):

        while(hour <= 24):

            if(hour <= 9 and hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(zero)+''+str(day)+'/'+str(zero)+''+str(hour)+'/'+'/'))
                print(files)

            elif(hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(zero)+''+str(day)+'/'+str(hour)+'/'))
                print(files)
            
            if(hour == 24):
                hour=00
                break

            else:
                hour+=1

            # Download the first file, and rename it the same name (without the directory structure)
            fs.get(files[0], files[0].split('/')[-1])

    elif(day >= 100):

       while(hour <= 24):

            if(hour <= 9 and hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(day)+'/'+str(zero)+''+str(hour)+'/'+'/'))
                print(files)

            elif(hour!=24):
                files = np.array(fs.ls('noaa-goes16/'+satelite+'/'+str(year)+'/'+str(day)+'/'+str(hour)+'/'))
                print(files)
            
            if(hour == 24):
                hour=00
                break

            else:
                hour+=1
            
            # Download the first file, and rename it the same name (without the directory structure)
            fs.get(files[0], files[0].split('/')[-1])          

    day+=1
