import os
from collections import defaultdict
import shutil

def parseAndAlign(folder_paths):
    files_dict = defaultdict(lambda:0)
    files_mapping = defaultdict(lambda:[])
    for _, path in enumerate(folder_paths):
        for file in os.listdir(path):
            map_file_name = "_".join(file.split('_')[1:])
            files_dict[map_file_name] += 1
            files_mapping[map_file_name].append(os.path.join(path, file))
    
    final_list = []
    for file, count in files_dict.items():
        if count != len(folder_paths):
            continue

        lines = []
        for path in files_mapping[file]:
            with open(path, 'r') as f:
                data = f.readlines()
                lines.append(len(data))

        if min(lines) != max(lines):
            continue

        for path in files_mapping[file]:
            name = path.split('/')[-1].split('_')[0]
            wr = open(name+'.txt', 'a')
            with open(path, 'r') as f:
                data = f.readlines()
                for d in data[2:]:
                    d = d.strip()
                    wr.write(d+"\n")
            wr.close()

if __name__ == '__main__':
    folder_paths = ['./data/en/', './data/hi/', './data/gu/', './data/ka/', './data/ta/']
    parseAndAlign(folder_paths)

