### web_crawling 유의 사항
1) 2020년 데이터는 28Round밖에 없고 2020년 이전에 데이터는 이후 데이터와 포맷이 다르다.
 => year의 변수는 2021~2024까지만 바꾸는 것을 추천
2) TIME_SLICE : 크롤링 하는 속도를 조절하는 코드로써 너무 빠르면 crwaling 중 버그가 날 수 있기 때문에 2초를 권장한다.
3) 가급적 Web_crawling 폴더 안에 있는 globals.py만 수정하는 것을 추천


### data 수집 과정
1. 공격, 수비, 패스, 골키퍼, passmatrix 데이터 따로 따로 crawling 과정에서 csv로 받음
2. 각 csv column명이 잘 인식이 되지 않아 직접 column명을 다시 적는다. (Parsing.py 참고)
3. 공격, 수비, 패스 || 골키퍼 || passmatrix 이렇게 나누어 폴더에 저장한다. (골키퍼까지 합치면 zero 값이 많기 때문에 따로 둠)
4. 따로 날씨, 습도, home, away, isWin 등은 따로 crwaling을 해서 csv파일을 넣어둔다.
5. 3번과 4번 csv을 합쳐 데이터 분석할 수 있도록 csv파일을 만든다.

***(add)*** => 한 라운드에 각각 팀에서 평점 상위 5명씩 뽑고 파일 합침 
6. 각 라운드에 각 팀에서 평점 상위 5명을 뽑는다. (출전 시간 일정 시간 밑이거나 후보는 뺌)
7. 그렇게 나온 모든 선수를 한 파일에 합친다. 


### position별로 data_visualation (data_visualation_position 폴더 참고) 
1. Data 가져오기
2. Visualization
  1) box_plot
  2) Histogram
  3) Correlation
  4) Scatter plot
  5) Distribution


### position별로 logistic, XGBoost, Randforest 등 model 돌리고 evaluate (model_position 폴더 참고)
1. 라이브러리 import
2. data load and Split
3. VIF 계산
4. LogisticRegression learning and evalutaion (RFE)
5. LogisticRegression learning and evalutaion 
6. RandomForest and evalutaion 
7. XGBoost and evalutaion 
8. Logistic, Random Forest, XGBoost overfit check
9. Logistic, Random, XGBoost Confusion matrix
10. XAI


### 모든 선수 데이터로 KNN이랑 Naivebaise model 돌리고 evaluate (model 폴더 참고)


## 데이터 파일 (`data`)
- **`DF_combined.csv`** : 2021~2023년 각 라운드 팀별 DF 평점 상위 5명씩 뽑아서 정리한 파일
- **`FW_combined.csv`** : 2021~2023년 각 라운드 팀별 FW 평점 상위 5명씩 뽑아서 정리한 파일
- **`GK_combined.csv`** : 2021~2023년 각 라운드 팀별 GK 평점 상위 5명씩 뽑아서 정리한 파일
- **`MF_combined.csv`** : 2021~2023년 각 라운드 팀별 MF 평점 상위 5명씩 뽑아서 정리한 파일

## 데이터 시각화 (`data_visualization_position`)
- **`데이터시각화_DF.ipynb`** : DF 포지션에 대한 데이터 시각화
- **`데이터시각화_FW.ipynb`** : FW 포지션에 대한 데이터 시각화
- **`데이터시각화_MF.ipynb`** : MF 포지션에 대한 데이터 시각화

## 모델 (`model`)
- **`knn.ipynb`** : 모든 선수 데이터를 대상으로 KNN 모델 학습 및 평가
- **`naviebaise.ipynb`** : 모든 선수 데이터를 대상으로 Naive Bayes 모델 학습 및 평가

## 포지션별 모델 (`model_position`)
- **`model_df.ipynb`** : DF 포지션을 대상으로 Logistic, XGBoost, Random Forest 모델 학습 및 평가
- **`model_fw.ipynb`** : FW 포지션을 대상으로 Logistic, XGBoost, Random Forest 모델 학습 및 평가
- **`model_mf.ipynb`** : MF 포지션을 대상으로 Logistic, XGBoost, Random Forest 모델 학습 및 평가

## 웹 크롤링 (`Web_crawling`)
- **`globals.py`** : 크롤링 속도 및 연도 설정 파일
- **`group_files.py`** : 공격, 수비, 패스 데이터 또는 골키퍼 데이터를 묶어 폴더에 저장
- **`Parsing.py`** : CSV 파일의 컬럼 이름을 수정하는 코드
- **`경기데이터_웹크롤링.ipynb`** : 날씨, 습도, 홈/어웨이 팀, 승패, 점수 등의 경기 데이터를 크롤링하여 CSV로 저장
- **`main_crawling.py`** : 메인 크롤링 실행 파일
- **`K명 자르기.py`** : 각 라운드에서 팀별 평점 상위 5명을 선택 (후보 또는 출전 시간 제한 적용)
- **`gathering_and_then_position_division.py`** : 모든 CSV 파일을 포지션과 연도별로 묶음

## 요구 사항 (`requirement.txt`)
- 프로젝트 실행에 필요한 패키지 목록이 포함되어 있음
