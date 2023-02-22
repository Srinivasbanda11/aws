import configparser
import shutil
from file_reader import read_file

config = configparser.ConfigParser()
config.read('config.ini')

source_file = config.get('source', 'file')
destination_file = config.get('destination', 'file')

content = read_file(source_file)
shutil.copyfile(source_file, destination_file)
