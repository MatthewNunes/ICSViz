# ICS Intrusion Detection Visualisations using the SWaT dataset
This project uses the data from the SWaT testbed to construct intuitive visualisations to aid network administrators overseeing an ICS network to easily detect attacks. It also uses visualistions to illustrate how a machine learning algorithm trained on ICS data works. 

## Prerequisites
- Argus
- TODO keep adding to this list

## Setup
- Create Argus files from the pcap files. 
-- For 2017 SWaT dataset run: 
```python
python3 -c 'import preprocessor; preprocessor.create2017ArgusFiles("/dir/to/pcaps/")'
```
-- For 2019 SWaT dataset run: 
```python
python3 -c 'import preprocessor; preprocessor.create2019ArgusFiles("/dir/to/pcaps/")'
```
- Currently the Argus Files are stored in a folder called "ArgusFiles" in the directory containing the pcap files which you need to create before running the commands above. **TODO** allow user to specify where to save files
- When it comes to the Argus files created from the 2019 dataset, remove the final underscore in the name before the .argus (if there is one). *TODO* Fix this...
- Create CSVs from Argus files: 
```python
python3 -c 'import preprocessor; preprocessor.createTxtFiles("/dir/to/Argus/Files/")'
```
## Using the software
- Run the data loader first. Once that finishes, kill the notebook (it will represent the data as numpy arrays and store it in your working directory)
- Then run the data analyser.