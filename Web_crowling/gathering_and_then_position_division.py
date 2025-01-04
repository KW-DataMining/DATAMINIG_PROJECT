import pandas as pd
import os

# # 현재 디렉토리부터 시작
# folder_path = os.getcwd()
# count = 0
# # 디렉토리 내의 모든 하위 폴더를 포함한 파일 목록을 가져오기
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if file.endswith('.csv'):  # CSV 파일만 처리
#             file_path = os.path.join(root, file)
#             # CSV 파일 읽기
#             df = pd.read_csv(file_path)
            
#             # '선수' 컬럼이 있다고 가정하고, 중복된 선수가 있는지 확인
#             if df['선수'].duplicated().any():
#                 count += 1
#                 print(f'{file} 파일에 중복된 선수가 있습니다. 경로: {file_path}')

# print(f'총 {count}개의 CSV 파일을 처리했습니다.')

# if(count != 0):
#     exit(0)

year_list = [2021,2022,2023]
position_list = ['_상위5개_자르기']
# CSV 파일들이 저장된 폴더 경로

for year in year_list:
    for position_name in position_list:

        folder_path = str(year) + position_name

        # 모든 CSV 파일 경로 가져오기
        csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

        # 모든 데이터를 하나로 병합
        dataframes = [pd.read_csv(file) for file in csv_files]
        merged_data = pd.concat(dataframes, ignore_index=True)

        # 병합된 데이터를 새 CSV 파일로 저장
        output_file = str(year) + position_name + '_merged_data.csv'
        merged_data.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"병합된 데이터가 '{output_file}'에 저장되었다.")



year_list = ["2021","2022","2023"]

for year in year_list:
    # CSV 파일 경로
    file_path = "./" + year + "_상위5개_자르기_merged_data.csv"

    # CSV 파일 읽기
    df = pd.read_csv(file_path)

    # 포지션별로 나누기 위한 컬럼 이름
    positions = ['포지션_GK', '포지션_DF', '포지션_MF', '포지션_FW']

    # 저장할 기본 경로 (파일이 저장될 디렉토리)
    base_dir = "./position_division2"

    # 폴더가 없다면 생성
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # 포지션별 데이터 나누기 및 저장
    for position in positions:
        # 해당 포지션만 필터링
        position_df = df[df[position] == 1]
        
        # 데이터 저장 경로
        save_path = os.path.join(base_dir, f"{position}_data_5개_자르기.csv")
        
        # 파일 존재 여부 확인
        if os.path.exists(save_path):
            # 기존 파일에 이어 붙이기
            position_df.to_csv(save_path, mode='a', header=False, index=False, encoding='utf-8')
            print(f"{position} 데이터를 기존 파일에 추가했습니다: {save_path}")
        else:
            # 새 파일로 저장
            position_df.to_csv(save_path, index=False, encoding='utf-8')
            print(f"{position} 데이터를 새 파일로 저장했습니다: {save_path}")

# for year in year_list:
#     # CSV 파일 경로
#     file_path = "./" + year + "_공격_수비_패스_4개_자르기_merged_data.csv"

#     # CSV 파일 읽기
#     df = pd.read_csv(file_path)

#     # 포지션별로 나누기 위한 컬럼 이름
#     positions = ['포지션_GK', '포지션_DF', '포지션_MF', '포지션_FW']

#     # 저장할 기본 경로 (파일이 저장될 디렉토리)
#     base_dir = "./position_division"

#     # 폴더가 없다면 생성
#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)

#     # 포지션별 데이터 나누기 및 저장
#     for position in positions:
#         # 해당 포지션만 필터링
#         position_df = df[df[position] == 1]
        
#         # 데이터 저장 경로
#         save_path = os.path.join(base_dir, f"{position}_data_4개_자르기.csv")
#         position_df.to_csv(save_path, index=False, encoding='utf-8')
#         print(f"{position} 데이터를 저장했습니다: {save_path}")


# for year in year_list:
#     # CSV 파일 경로
#     file_path = "./" + year + "_공격_수비_패스_5개_자르기_merged_data.csv"

#     # CSV 파일 읽기
#     df = pd.read_csv(file_path)

#     # 포지션별로 나누기 위한 컬럼 이름
#     positions = ['포지션_GK', '포지션_DF', '포지션_MF', '포지션_FW']

#     # 저장할 기본 경로 (파일이 저장될 디렉토리)
#     base_dir = "./position_division"

#     # 폴더가 없다면 생성
#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)

#     # 포지션별 데이터 나누기 및 저장
#     for position in positions:
#         # 해당 포지션만 필터링
#         position_df = df[df[position] == 1]
        
#         # 데이터 저장 경로
#         save_path = os.path.join(base_dir, f"{position}_data_5개_자르기.csv")
#         position_df.to_csv(save_path, index=False, encoding='utf-8')
#         print(f"{position} 데이터를 저장했습니다: {save_path}")


# for year in year_list:
#     # CSV 파일 경로
#     file_path = "./" + year + "_공격_수비_패스_6개_자르기_merged_data.csv"

#     # CSV 파일 읽기
#     df = pd.read_csv(file_path)

#     # 포지션별로 나누기 위한 컬럼 이름
#     positions = ['포지션_GK', '포지션_DF', '포지션_MF', '포지션_FW']

#     # 저장할 기본 경로 (파일이 저장될 디렉토리)
#     base_dir = "./position_division"

#     # 폴더가 없다면 생성
#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)

#     # 포지션별 데이터 나누기 및 저장
#     for position in positions:
#         # 해당 포지션만 필터링
#         position_df = df[df[position] == 1]
        
#         # 데이터 저장 경로
#         save_path = os.path.join(base_dir, f"{position}_data_6개_자르기.csv")
#         position_df.to_csv(save_path, index=False, encoding='utf-8')
#         print(f"{position} 데이터를 저장했습니다: {save_path}")


# for year in year_list:
#     # CSV 파일 경로
#     file_path = "./" + year + "_공격_수비_패스_7개_자르기_merged_data.csv"

#     # CSV 파일 읽기
#     df = pd.read_csv(file_path)

#     # 포지션별로 나누기 위한 컬럼 이름
#     positions = ['포지션_GK', '포지션_DF', '포지션_MF', '포지션_FW']

#     # 저장할 기본 경로 (파일이 저장될 디렉토리)
#     base_dir = "./position_division"

#     # 폴더가 없다면 생성
#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)

#     # 포지션별 데이터 나누기 및 저장
#     for position in positions:
#         # 해당 포지션만 필터링
#         position_df = df[df[position] == 1]
        
#         # 데이터 저장 경로
#         save_path = os.path.join(base_dir, f"{position}_data_7개_자르기.csv")
#         position_df.to_csv(save_path, index=False, encoding='utf-8')
#         print(f"{position} 데이터를 저장했습니다: {save_path}")
