import os

blank = {'my_project': [{'settings': []}, {'main_app': []}, {'admin_app': []}, {'authapp': []}]}

for key, value in blank.items():
    if not os.path.exists(key):
        for item in value:
            for i in item.keys():
                os.makedirs(os.path.join(key, i))



