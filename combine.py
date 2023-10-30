import yaml
import os

directory_path = os.getcwd()
folders = os.listdir(directory_path)
with open('front.yml', 'r') as file:
    base = yaml.safe_load(file)

ids = []
for folder in folders:
    if 'vol' in folder:
        dir = os.path.join(directory_path, folder)
        with open(os.path.join(dir,'config.yml'), 'r') as file:
            volume_config = yaml.safe_load(file)
        ids += volume_config
        
base['website']['sidebar'] = ids

with open(r'_quarto.yml', 'w') as file:
    yaml.safe_dump(base, file)
