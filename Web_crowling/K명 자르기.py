import pandas as pd
import os

def filter_and_save_csv(input_folder, output_folder, columns_to_keep, k):
    """
    주어진 폴더의 CSV 파일을 읽어서 필요한 컬럼만 필터링한 후, 
    이긴 팀은 평점 상위 k명, 진 팀은 평점 하위 k명만 필터링하여 다른 폴더에 저장하는 함수.
    
    Args:
        input_folder (str): 입력 CSV 파일들이 있는 폴더 경로
        output_folder (str): 필터링된 CSV 파일을 저장할 폴더 경로
        columns_to_keep (list): 필터링할 컬럼 이름 리스트
        k (int): 상위/하위 k명의 데이터를 추출
    """
    # 출력 폴더가 없으면 생성
    os.makedirs(output_folder, exist_ok=True)

    # 폴더 내 모든 CSV 파일 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_folder, filename)  # 입력 파일 경로
            output_file_home = os.path.join(output_folder, f"home_{filename}")
            output_file_away = os.path.join(output_folder, f"away_{filename}")

            # 데이터 읽기
            df = pd.read_csv(input_file)
            # isWin 컬럼이 모두 2가 아닌닌 경우 건너뛰기
            if 'isWin' in df.columns and all(df['isWin'] == 2):
                print(f"Skipping file with all isWin=2: {filename}")
                continue

            try:
                # 필요한 컬럼만 필터링
                filtered_df = df[columns_to_keep]  

                filtered_df = filtered_df[
                    (filtered_df['출전시간'] > 10)|
                    ((filtered_df['출전시간'] <= 10) & (filtered_df['득점'] != 0))
                ]

                filtered_df = filtered_df[
                    (filtered_df['평점'] > 5)
                ]
              
                # 이긴 팀과 진 팀 분리
                Home_team = filtered_df[filtered_df['Ishome'] == 1]
                Away_team = filtered_df[filtered_df['Ishome'] == 0]
                
                # 이긴 팀은 평점 상위 k명, 진 팀은 평점 하위 k명 추출
                Home_top_k_win = Home_team.nlargest(k, '평점')
                #Home_bottom_k_lose = Home_team.nsmallest(k, '평점')

                Away_top_k_win = Away_team.nlargest(k, '평점')
                #Away_bottom_k_lose = Away_team.nsmallest(k, '평점')

                # 두 팀 데이터를 합쳐서 저장
                result_df = pd.concat([Home_top_k_win, Away_top_k_win])
                #result_df_away = pd.concat([Away_top_k_win, Away_bottom_k_lose])
                # 저장
                output_file = os.path.join(output_folder, f"combined_{filename}")
                result_df.to_csv(output_file, index=False, encoding='utf-8-sig')
                print(f"Processed and saved: {output_file}")
            except KeyError as e:
                print(f"Error processing {input_file}: {e}")

# 함수 호출 예시
columns_to_keep = [
    '출전시간', '평점', '득점', '도움', '슈팅', '유효슈팅', '블락된 슈팅', '벗어난 슈팅',
    'PA내슈팅', 'PA외슈팅', '오프사이드', '프리킥', '코너킥', '스로인', '드리블 성공',
    '드리블 성공률(%)', 'Ishome', '경합(지상)성공', '경합(지상)성공률(%)',
    '경합(공중)성공', '경합(공중)성공률(%)', '태클성공', '태클성공률(%)', '클리어링',
    '인터셉트', '차단', '획득', '블락', '볼미스', '파울', '피파울', '경고', '퇴장',
    '패스성공', '패스성공률(%)', '키패스', '공격진영패스성공', '공격진영패스성공률(%)',
    '중앙지역패스성공', '중앙지역패스성공률(%)', '수비진영패스성공', '수비진영패스성공률(%)',
    '롱패스성공', '롱패스성공률(%)', '중거리패스성공', '중거리패스성공률(%)',
    '숏패스성공', '숏패스성공률(%)', '전진패스성공', '전진패스성공률(%)',
    '횡패스성공', '횡패스성공률(%)', '백패스성공', '백패스성공률(%)', '크로스성공',
    '크로스성공률(%)', '탈압박', '포지션_DF', '포지션_FW', '포지션_GK', '포지션_MF',
    'isWin', '번호', '선수',
]
# 실행할 때 원하는 경로와 k 값 넣어주면 돼

filter_and_save_csv(
    './진짜마지막/2021_공격_수비_패스_포지션',
    './2021_상위5개_자르기',
    columns_to_keep,
    k=5  # 상위/하위 k명 설정
)
filter_and_save_csv(
    './진짜마지막/2022_공격_수비_패스_포지션',
    './2022_상위5개_자르기',
    columns_to_keep,
    k=5  # 상위/하위 k명 설정
)

filter_and_save_csv(
    './진짜마지막/2023_공격_수비_패스_포지션',
    './2023_상위5개_자르기',
    columns_to_keep,
    k=5  # 상위/하위 k명 설정
)


