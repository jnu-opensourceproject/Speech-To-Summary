import pandas as pd
import os
# data 폴더의 데이터들은 외부 반출이 금지되어 있으므로, .gitignore처리
dir1 = 'data'
# res는 news 필드와 summary 필드를 가짐
res = {'news':[], 'summary':[]}
fileList = os.listdir(dir1)
for ffile in fileList:
    with open(os.path.join(dir1, ffile), encoding='utf-8') as inputfile:
        # main_data는 pd.read_json(inputfile)의 결과, json파일의 데이터를 가짐
        main_data = pd.read_json(inputfile)
       
        # 데이터에서 Meta(Refine) 필드의 passage 필드를 추가
        res['news'].append(main_data["Meta(Refine)"].get('passage'))
        # 데이터에서 Annotation 필드의 summary1 필드를 받고 추가
        res['summary'].append(main_data['Annotation'].get('summary1'))

# 읽은 데이터를 데이터프레임으로 변환 후 기존 tsv에 합성
df = pd.DataFrame(res)
df = df.dropna(axis=0)
df.to_csv("train.tsv", mode='a', header=0, encoding='utf-8', index=False, sep='\t')