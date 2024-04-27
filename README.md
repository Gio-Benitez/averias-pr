# AveriasPR
Capstone Final project for INSO 4151/CIIC 4151 at the University of Puerto Rico - Mayagüez

2023-2024 - Spring Semester

Title: Averías PR

Desc: Online platform that offers users: 
- A reporting tool to report infrastructure issues (averías) in their region, reports contain: Location, Report Category and an image of the issue being reported.
- An interactive map where users can select a region (municipio) and report category of their choise and see statistics regarding reports from that region.
- An data visualization dashboard where users can select different filtering options and generate graphs comparing report quantities per region, category, or a combination of these.

Authors: Wester Aldarondo Torres, Giovanni Benítez Rivera, Greg Viera Pérez

## Setting Up

### Create Docker Container 
First things first, make sure to [Download Docker](https://docs.docker.com/get-docker/?_gl=1*155k8vt*_ga*MTc1ODU3ODIwMC4xNzA4NTQ0NjQw*_ga_XJWPQMJYHQ*MTcwODU1NDM4Ny4yLjEuMTcwODU1NDM5OC40OS4wLjA.).

Generate the Docker container by running `bash build.sh` inside of the db_setup directory. 

### Python Environment

***To install new python packages and dependencies***

Please enter the environment first, by running the following command `source env/bin/activate`. Now, you can install any necessary python packages. 

Once finished, run `deactivate` to exit the python environment. However, make sure to export the installed packages to requirements.txt by running the command `pip freeze > requirement.txt`. Also remember to add requirements.txt to your commit!

