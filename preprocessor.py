import os

def create2017ArgusFiles(init_dir):
	for cap_file in os.listdir(init_dir):
		if cap_file.endswith(".cap"):
			os.system("argus -r " + init_dir + cap_file + " -w " + init_dir + "ArgusFiles/"+cap_file.replace(".cap", ".argus"))


def create2019ArgusFiles(init_dir):
	for cap_file in os.listdir(init_dir):
		if os.path.isfile(init_dir + cap_file):
			if cap_file.endswith(".pcap"):
				os.system("argus -r " + init_dir + cap_file + " -w " + init_dir + "ArgusFiles/"+cap_file.replace(".pcap", ".argus"))
			else:
				os.system("argus -r " + init_dir + cap_file + " -w " + init_dir + "ArgusFiles/"+cap_file + ".argus")

def chooseFeatures(filename):
	listOfFeatures = []
	for line in open(filename, "r"):
		listOfFeatures.append(line.strip())
	features_string = ' '.join(listOfFeatures)
	return features_string.strip()


def createTxtFiles(init_dir):
	features_to_use = chooseFeatures("Features.txt")
	for argus_file in os.listdir(init_dir):
		if argus_file.endswith(".argus"):
			os.system("ra -nn -c ',' -r " + init_dir+argus_file + " -s " + features_to_use +  " > " + init_dir + "TextFiles/" + argus_file.replace(".argus", ".csv"))
