import pandas as pd
import os
# data 폴더의 데이터들은 외부 반출이 금지되어 있으므로, .gitignore처리
dir1 = 'data'
dfs = []
fileList = os.listdir(dir1)
for ffile in fileList:
    with open(os.path.join(dir1, ffile), encoding='utf-8') as inputfile:
        # pd.read_json(inputfile)의 결과가 json파일의 데이터를 가짐
        # dfs에 파일을 통째로 삽입
        dfs.append(pd.read_json(inputfile))

# dfs 배열을 통합하고 csv 파일로 출력
df = pd.concat(dfs, sort=False)
df.to_csv('csvfile.csv', encoding='utf-8', index=False)


# data가 json 데이터를 가짐. main_data는 json 파일의 jobs 필드를 가짐.
main_data = data.get('jobs')
# res는 name 필드와 result 필드를 가짐
res = {'name':[], 'result':[]}

# jobs 필드의 데이터들을 순회하며 jobs 바로 하위의 필드에 접근할 것
for name_dict in main_data:
    # builds 필드가 비어있으면 건너뜀
    if len(name_dict['builds'])==0:
        continue
    # 데이터에서 name 필드를 추가
    res['name'].append(name_dict.get('name', 'NA'))
    # 데이터에서 builds 필드의 첫번째 항목의 result 필드를 받고 추가
    resultval = name_dict['builds'][0].get('result')
    res['result'].append(resultval)
print(res)
import pandas as pd
# 읽은 데이터를 데이터프레임으로 변환 후 csv 출력
df = pd.DataFrame(res)
df.to_csv("/home/akash.pagar/shell_learning/file_timer/jobs.csv", index=False)