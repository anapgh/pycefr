#-- PROGRAMME TO CREATE A DICTIONARY OF THE CONFIGURATION

import configparser
configuration = configparser.ConfigParser()

#-- Read the configuration file
configuration.read('configuration.cfg')

#-- Dictionary of LEVELS
levels = {}

#-- Show list of read sections in the archive
configuration.sections()
for section in configuration.sections():
    levels[section] = []
    #-- List options and values of a section:
    for option, value in configuration[section].items():
        levels[section].append({option : value})


#-- Create .txt file with dictionary
with open('dicc.txt', 'w') as file:
    file.write(str(levels))
    file.close()
