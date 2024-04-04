# AveriasPR

## Setting Up

### Create Docker Container 
First things first, make sure to [Download Docker](https://docs.docker.com/get-docker/?_gl=1*155k8vt*_ga*MTc1ODU3ODIwMC4xNzA4NTQ0NjQw*_ga_XJWPQMJYHQ*MTcwODU1NDM4Ny4yLjEuMTcwODU1NDM5OC40OS4wLjA.).

Generate the Docker container by running `bash build.sh` inside of the db_setup directory. 

### Python Environment

***To install new python packages and dependencies***

Please enter the environment first, by running the following command `source env/bin/activate`. Now, you can install any necessary python packages. 

Once finished, run `deactivate` to exit the python environment. However, make sure to export the installed packages to requirements.txt by running the command `pip freeze > requirement.txt`. Also remember to add requirements.txt to your commit!

