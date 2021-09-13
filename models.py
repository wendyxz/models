import os
import urllib.request

# read model_list.txt
with open('/Users/wendyzhang/Downloads/model_list.txt') as f:
    content = f.readlines()

# strip out newline characters
model_list = []
for item in content:
    model = item.split()
    model_list.append(model)

# list of models with different format, to be skipped over and manually
#   downloaded afterwards
manual_download = []

for item in model_list:
    model_name = item[0]
    main_path = "/Users/wendyzhang/Downloads"
    path = os.path.join(main_path, model_name)
    archs = ["GPU", "zcu102", "vck190", "u50", "u50lv9e", "u50-v3me"]
    os.makedirs(path, exist_ok=True)
    link = "https://raw.githubusercontent.com/Xilinx/Vitis-AI/master/models/AI-Model-Zoo/ \
            model-list/{}/model.yaml".format(model_name)
    i = 0
    for line in urllib.request.urlopen(link):
        if "download link:" in line.decode('utf-8'):
            if i > 5:
                manual_download.append(model_name)
                continue
            else:
                print(line.decode('utf-8')[17:])
                print(archs[i])
                urllib.request.urlretrieve(line.decode('utf-8')[17:], path + "/" + archs[i])
                i = i + 1

print(manual_download)
