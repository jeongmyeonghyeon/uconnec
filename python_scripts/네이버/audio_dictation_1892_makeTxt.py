"""
[네이버] 음성 텍스트 내용 수정하기 (1892) - 맞춤법 검사용 .txt

이 프로젝트 같은 경우에는 맞춤법 검사를 조성우매니저님이 직접하시기 때문에
모든 스크립트가 들어있는 .txt 파일로 먼저 만든 후에 맞춤법 검사를 마치면
그 때 라인별로 파일을 나누는 작업을 한다.

※ .txt 파일 형식 > 파일명 \t 스크립트
"""

from crowdworks.commonUtil import *

import datetime

now = datetime.datetime.now()
year = str(now.year)
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
EXT_FOLDER = year + month + day

EXT_PATH = "/Users/myeonghyeonjeong/Desktop/DATA_EXT/네이버/음성_텍스트_내용_수정하기(1892)/" # TODO: 폴더 미리 만들어야함!

SQL = "SELECT result_json FROM TB_PRJ_DATA WHERE prj_idx=3420 AND prog_state_cd='ALL_FINISHED' AND problem_yn=0"
sql_result = getDatabaseData(SQL, "", "", "")

txt = open(EXT_PATH + "labeled_data_1892_" + EXT_FOLDER + '.txt', 'w', encoding='UTF-8-sig')
print("audio_dictation_lineSplit.py PATH: ", EXT_PATH + "labeled_data_1892_" + EXT_FOLDER + '.txt')

for row in sql_result:
    data = json.loads(row[0])

    idx = data['idx']
    edit = data['edit']
    script = data['script']
    fileName = data['originalFileName'].split('.wav')[0]

    txt.write(fileName + "\t" + script + "\n")
