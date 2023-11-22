![GitHub](https://img.shields.io/github/license/till-teb/expenses-management-tool)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/till-teb/expenses-management-tool/main.yml)

# SleepQuality_GARMIN

This Python project is part of a [ZDD](https://github.com/ZDDduesseldorf)-HSD digital health study exploring the effects of physical activity on sleep quality. The data is collected using a GARMIN Forerunner 255 watch, and analysis involves AI/ML techniques.

## Contribution
Feel free to contribute by opening a pull request or filing an issue if you have suggestions for improvements.

## Installation and Run

**Note: This code requires a GARMIN watch and a GARMIN account.**

Download and install:
```bash
git clone https://github.com/l4nz8/SleepQuality_GARMIN.git
cd SleepQuality_GARMIN
pip install -r requirements.txt
```
First, navigate to the *Get_GARMIN_Data/* folder and run the *main.py* file to download your data as a .csv file to your computer.  
```bash
cd Get_GARMIN_Data
python main.py 
```
This script automatically creates a *data/* folder to save the data required for the AI model as a .csv file, which will be needed for later model training.