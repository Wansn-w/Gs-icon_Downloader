import requests
import json
import os


except_json = ['talents.json'] # 不自动识别的索引
index_list = os.listdir('index')

if not os.path.exists('icon'):
    os.makedirs('icon')

for i in index_list:
    if i in except_json:
        continue
    types = i.split('.')[0]
    print(f'## Start {types} Downloading...  ##')
    with open(f'index/{i}', 'r') as f:
        d = json.loads(f.read())
    for t1 in list(d.keys()):
        name = t1.split('.')[0]
        print(f'Downloading {name}...')
        dirs = f'icon/{types}/{name}' # 对应文件夹
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        for t2 in list(d[t1].keys()): # 对应图片
            filename = d[t1][t2].split('/')[-1:][0]
            wpath = f'{dirs}/{filename}'
            if os.path.exists(wpath):
                print(f'    [SKIP] {filename} already in {name}!')
                continue
            print(f'    -{t2}...')
            with open(wpath, 'wb+') as f:
                content = requests.get(d[t1][t2]).content
                f.write(content)
        print(f'\\o/    {types} of {name} already save done!')
print('All Image save done!')