# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:41:38 2021

@author: Administrator
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 06 유형(DataSet_06.csv 이용)
#
# 구분자 : comma(“,”), 4,323 Rows, 19 Columns, UTF-8 인코딩

# 주택 관련 정보를 바탕으로 주택 가격을 예측해 보고자 한다. 
# 다음은 확보한 주택 관련 데이터로 총 19개 컬럼으로 구성되어
# 있다.

# 컬 럼 / 정 의 / Type
# id / 매물 번호 / Double
# date / 날짜 / String
# price / 거래 가격 / Double
# bedrooms / 방 개수 / Double
# bathrooms / 화장실 개수 (화장실은 있으나 샤워기 없는 경우 0.5로 처리) / Double
# sqft_living / 건축물 면적 / Double
# sqft_lot / 대지 면적 / Double
# floors / 건축물의 층수 / Double
# waterfront / 강변 조망 가능 여부 (0 / 1) / Double
# view / 경관 (나쁨에서 좋음으로 0 ~ 4로 표시) / Double
# condition / 관리 상태 (나쁨에서 좋음으로 1 ~ 5로 표시) / Double
# grade / 등급 (낮음에서 높음으로 1 ~ 13으로 표시) / Double
# sqft_above / 지상 면적 / Double
# sqft_basement / 지하실 면적 / Double
# yr_built / 건축 연도 / Double
# yr_renovated / 개축 연도 / Double
# zipcode / 우편번호 / Double
# sqft_living15 / 15개의 인근 주택의 평균 건물 면적 / Double
# sqft_lot15 / 15개의 인근 주택의 평균 대지 면적 / Double
# =============================================================================
# =============================================================================



#%%

# =============================================================================
# 1.강변 조망이 가능한지 여부(waterfront)에 따라 평균 주택 가격을 계산하고 조망이
# 가능한 경우와 그렇지 않은 경우의 평균 가격 차이의 절대값을 구하시오. 답은
# 소수점 이하는 버리고 정수부만 기술하시오. (답안 예시) 1234567
# =============================================================================

import pandas as pd

dataset6=pd.read_csv('Dataset/Dataset_06.csv')
                     
dataset6.columns
# ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#        'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#        'sqft_living15', 'sqft_lot15']

q1_1 = dataset6[dataset6.waterfront == 1]['price'].mean()

q1_2 = dataset6[dataset6.waterfront == 0]['price'].mean()

abs(q1_1 - q1_2)

# (정답)

# 1167272



#%%

# =============================================================================
# 2.price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, yr_built 등 7개의 변수 간의
# 상관분석을 수행하고 price와의 상관계수의 절대값이 가장 큰 변수와 가장 작은
# 변수를 차례로 기술하시오. (답안 예시) view, zipcode
# 
# =============================================================================


x_var = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'yr_built']

q2 = dataset6[x_var]

q2_out = q2.corr().iloc[1:,0]

q2_out.nlargest(1)
q2_out.nsmallest(1)

# (정답) sqft_living, yr_built







#%%

# =============================================================================
# 3. id, date, 그리고 zipcode를 제외한 모든 변수를 독립변수로, price를 종속변수로 하여
# 회귀분석을 수행하시오. 통계적 유의성을 갖지 못하는 독립변수를 제거하면 회귀
# 모형에 남는 변수는 모두
# 몇 개인가? 이 때 음의 회귀계수를 가지는 변수는 몇 개인가? (답안 예시) 5, 3
# =============================================================================

# =============================================================================
# (참고)
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from statsmodels.formula.api import ols
# =============================================================================

q3=dataset6.drop(columns=['id','date','zipcode'])

x_var = q3.columns.drop('price')

from statsmodels.formula.api import ols

form = 'price~'+'+'.join(x_var)

ols1=ols(form, data=q3).fit()

ols1.summary()

len(x_var)

# 통계적 유의성을 갖지 못하는 독립변수 P>|t| > 0.05 인 변수 sqft_lot, sqft_lot15

dir(ols1)

sum(ols1.pvalues < 0.05) - 1

# 13, 2

#%%

# =============================================================================
# =============================================================================
# # 문제 07 유형(DataSet_07.csv 이용)
#
# 구분자 : comma(“,”), 400 Rows, 9 Columns, UTF-8 인코딩
#
# 대학원 진학을 위하여 어떤 항목이 중요하게 영향을 미치는지
# 아래 데이터로 분석하고자 한다.

# 컬 럼 / 정 의 / Type
# Serial_No / 구분자 번호 / Double
# GRE / GRE 시험 성적 / Double
# TOEFL / TOEFL 시험 성적 / Double
# University_Rating / 대학 평가 그룹 (1 ~ 5) / Double
# SOP / 자기 소개서 점수 (1 ~ 5) / Double
# LOR / 추천서 점수 (1 ~ 5) / Double
# CGPA / 학부 평량 평점 (10점 만점 환산 점수) / Double
# Research / 연구 참여 경험 여부 (0 / 1) / Double
# Chance_of_Admit / 합격 가능성 / Double
# =============================================================================
# =============================================================================

# =============================================================================
# (참고)
# #1
# import pandas as pd
# #2
# import scipy.stats as stats
# #3
# from sklearn.linear_model import LogisticRegression
# Solver = ‘liblinear’, random_state = 123
# =============================================================================


#%%

# =============================================================================
# 1. 합격 가능성에 GRE, TOEFL, CGPA 점수 가운데 가장 영향이 큰 것이 어떤 점수인지
# 알아 보기 위해서 상관 분석을 수행한다.
# - 피어슨(Pearson) 상관계수 값을 구한다.
# - Chance_of_Admit와의 가장 큰 상관계수 값을 가지는 항목의 상관계수를 소수점 넷째
# 자리에서 반올림하여 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

import pandas as pd

dataset7=pd.read_csv('Dataset/Dataset_07.csv')
                     
q1 = dataset7[['GRE', 'TOEFL', 'CGPA','Chance_of_Admit']].corr()

answer_7_1 = round(q1.iloc[:-1, -1].max(),3)

# (정답) 0.873

#%%

# =============================================================================
# 2.GRE 점수의 평균 이상을 받은 그룹과 평균 미만을 받은 그룹의 CGPA 평균은 차이가
# 있는지
# 검정을 하고자 한다.
# - 적절한 검정 방법을 선택하고 양측 검정을 수행하시오 (등분산으로 가정)
# - 검정 결과, 검정통계량의 추정치를 소수점 셋째 자리에서 반올림하여 소수점 두 자리까지
# 기술하시오.
# (답안 예시) 1.23
# =============================================================================

q7_2 = dataset7.copy()

GRE_avg = q7_2.GRE.mean()

q7_2['GRE_gr'] = 'under'
q7_2.loc[q7_2['GRE'] >= GRE_avg , 'GRE_gr'] = 'over'

from scipy.stats import ttest_ind

a = q7_2[q7_2['GRE_gr'] == 'over']['CGPA']
b = q7_2[q7_2['GRE_gr'] == 'under']['CGPA']

ttest_ind(a, b, equal_var=True)
# Ttest_indResult(statistic=19.443291692470982, pvalue=1.1127037052806161e-59)

# (정답) 19.44







#%%

# =============================================================================
# 3.Chance_of_Admit 확률이 0.5를 초과하면 합격으로, 이하이면 불합격으로 구분하고
# 로지스틱 회귀분석을 수행하시오.
# - 원데이터만 사용하고, 원데이터 가운데 Serial_No와 Label은 모형에서 제외
# - 각 설정값은 다음과 같이 지정하고, 언급되지 않은 사항은 기본 설정값을 사용하시오
# Seed : 123
# - 로지스틱 회귀분석 수행 결과에서 로지스틱 회귀계수의 절대값이 가장 큰 변수와 그 값을
# 기술하시오. 
# (로지스틱 회귀계수는 반올림하여 소수점 둘째 자리까지 / Intercept는 제외)
# (답안 예시) abc, 0.12
# =============================================================================

dataset7.columns
dataset7.dtypes
q7_3 = dataset7.drop(columns=['Serial_No'])


import numpy as np
q7_3['ch_ad']=np.where(q7_3.Chance_of_Admit > 0.5, 1, 0) 
# 합격, 불합격이라고 쓰면 Logistic의 경우 한국말 오류 생김

from sklearn.linear_model import LogisticRegression

x = q7_3.drop(columns=['Chance_of_Admit','ch_ad'])
y = q7_3.ch_ad

# Solver = ‘liblinear’, random_state = 12
logit = LogisticRegression(fit_intercept=True, 
                           random_state=12, 
                           solver='liblinear', 
                           C=100000).fit(x,y)
# 함수 설명 Ctrl + i
# 최적으로 떨어지기 위해 다양한 옵션 추가 random_state=123, solver='newton-cg', C=100000

q7_3 = pd.DataFrame({'var' : x.columns.values,
                     'coef' : logit.coef_.reshape(-1)})

# (정답) CGPA , 3.34

#%%

# =============================================================================
# =============================================================================
# # 문제 08 유형(DataSet_08.csv 이용)
#
# 구분자 : comma(“,”), 50 Rows, 5 Columns, UTF-8 인코딩
#
# 스타트업 기업들의 수익성에 대한 분석을 하기 위하여
# 아래와 같은 데이터를 입수하였다
#
# 
# 컬 럼 / 정 의 / Type
# RandD_Spend / 연구개발비 지출 / Double
# Administration / 운영관리비 지출 / Double
# Marketing_Spend / 마케팅비 지출 / Double
# State / 본사 위치 / String
# Profit / 이익 / Double
# =============================================================================
# =============================================================================

# =============================================================================
# (참고)
# #1
# import pandas as pd
# import numpy as np
# #3
# from sklearn.linear_model import LinearRegression
# =============================================================================

#%%

# =============================================================================
# 1.각 주(State)별 데이터 구성비를 소수점 둘째 자리까지 구하고, 알파벳 순으로
# 기술하시오(주 이름 기준).
# (답안 예시) 0.12, 0.34, 0.54
# =============================================================================






#%%

# =============================================================================
# 2.주별 이익의 평균을 구하고, 평균 이익이 가장 큰 주와 작은 주의 차이를 구하시오. 
# 차이값은 소수점 이하는 버리고 정수부분만 기술하시오. (답안 예시) 1234
# =============================================================================








#%%

# =============================================================================
# 3.독립변수로 RandD_Spend, Administration, Marketing_Spend를 사용하여 Profit을 주별로
# 예측하는 회귀 모형을 만들고, 이 회귀모형을 사용하여 학습오차를 산출하시오.
# - 주별로 계산된 학습오차 중 MAPE 기준으로 가장 낮은 오차를 보이는 주는 어느
# 주이고 그 값은 무엇인가? (반올림하여 소수점 둘째 자리까지 기술하시오)
# - (MAPE = Σ ( | y - y ̂ | / y ) * 100/n )
# (답안 예시) ABC, 1.56
# =============================================================================












#%%

# =============================================================================
# =============================================================================
# # 문제 09 유형(DataSet_09.csv 이용)
#
# 구분자 : comma(“,”), 2000 Rows, 16 Columns, UTF-8 인코딩
#
# 항공사에서 고객만족도 조사를 하고 서비스 개선에 활용하고자
# 아래와 같은 데이터를 준비하였다.
#
# 컬 럼 / 정 의 / Type
# satisfaction / 서비스 만족 여부 / String
# Gender / 성별 / String
# Age / 나이 / Double
# Customer_Type / 고객 타입 / String
# Class / 탑승 좌석 등급 / String
# Flight_Distance / 비행 거리 / Double
# Seat_comfort / 좌석 안락도 점수 / Double
# Food_and_Drink / 식사와 음료 점수 / Double
# Inflight_wifi_service / 기내 와이파이 서비스 점수 / Double
# Inflight_entertainment / 기내 엔터테인먼트 서비스 점수 / Double
# Onboard_service / 탑승 서비스 점수 / Double
# Leg_room_service / 다리 공간 점수 / Double
# Baggage_handling / 수하물 취급 점수 / Double
# Cleanliness / 청결도 점수 / Double
# Departure_Daly_in_Minutes / 출발 지연 (분) / Double
# Arrival_Delay_in_Minutes / 도착 지연 (분) / Double
# =============================================================================
# =============================================================================

# =============================================================================
# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# import scipy.stats as stats
# #3
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# 
# =============================================================================

#%%

# =============================================================================
# 1.데이터 타입을 위 표에 정의된 타입으로 전처리를 한 후, 데이터 파일 내에 결측값은
# 총 몇 개인가? (답안 예시) 1
# =============================================================================







#%%
# =============================================================================
# 2.다음에 제시된 데이터 처리를 하고 카이제곱 독립성 검정을 수행하시오.
# - 결측값이 있다면 해당 행을 제거하시오.
# - 나이는 20 이하이면 10, 30 이하이면 20, 40 이하이면 30, 50 이하이면 40, 60 이하이면 50, 
# 60 초과는 60으로 변환하여 Age_gr으로 파생변수를 생성하시오.
# - Age_gr, Gender, Customer_Type, Class 변수가 satisfaction에 영향이 있는지 카이제곱
# 독립성 검정을 수행하시오. 
# - 연관성이 있는 것으로 파악된 변수의 검정통계량 추정치를 정수 부분만 기술하시오. 
# (답안 예시) 123
# =============================================================================












#%%

# =============================================================================
# 3.고객 만족도를 라벨로 하여 다음과 같이 로지스틱 회귀분석을 수행하시오. 
# - 결측치가 포함된 행은 제거
# - 데이터를 7대 3으로 분리 (Seed = 123)
# - 아래의 11개 변수를 Feature로 사용
# Flight_Distance, Seat_comfort, Food_and_drink, Inflight_wifi_service, 
# Inflight_entertainment,Onboard_service, Leg_room_service, Baggage_handling,
# Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes
# 
# - Seed = 123, 이외의 항목은 모두 Default 사용
# - 예측 정확도를 측정하고 dissatisfied의 f1 score를 소수점 넷째 자리에서 반올림하여
# 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================















#%%

# =============================================================================
# =============================================================================
# # 문제 10 유형(DataSet_10.csv 이용)
#
# 구분자 : comma(“,”), 1538 Rows, 6 Columns, UTF-8 인코딩

# 중고 자동차 가격에 대한 분석을 위하여 아래와 같은 데이터를
# 확보하였다.

# 컬 럼 / 정 의 / Type
# model / 모델명 / String
# engine_power / 엔진 파워 / Double
# age_in_days / 운행 일수 / Double
# km / 운행 거리 / Double
# previous_owners / 이전 소유자 수 / Double
# price / 중고차 가격 / Double
# =============================================================================
# =============================================================================

# =============================================================================
# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# import scipy.stats as ststs
# #3
# from sklearn.linear_model import LinearRegression
# =============================================================================


#%%

# =============================================================================
# 1.이전 소유자 수가 한 명이고 엔진 파워가 51인 차에 대해 모델별 하루 평균 운행
# 거리를 산출하였을 때 가장 낮은 값을 가진 모델이 가장 큰 값을 가진 모델에 대한
# 비율은 얼마인가? 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지
# 기술하시오.
# (모델별 평균 → 일평균 → 최대최소 비율 계산) (답안 예시) 0.12
# =============================================================================

import pandas as pd

dataset10 = pd.read_csv('Dataset/Dataset_10.csv')
dataset10 = dataset10.dropna(axis=1, how='all')
dataset10.columns
# ['model', 'engine_power', 'age_in_days', 'km', 'previous_owners',
#        'price']

q10_1_1 = dataset10[dataset10.previous_owners == 1]
q10_1_2 = q10_1_1[q10_1_1.engine_power == 51]

len(dataset10)# 1538
len(q10_1_1) # 1389
len(q10_1_2) # 1312

q10_1_2.columns
q10_1_3 = pd.pivot_table(data=q10_1_2, index='model', 
                       values=['age_in_days','km'])

q10_1_3['days']=q10_1_3['km']/q10_1_3['age_in_days']

answer = round(q10_1_3['days']['sport']/q10_1_3['days']['lounge'],2)

# (정답) 0.97












#%%

# =============================================================================
# 2.운행 일수에 대한 운행 거리를 산출하고, 위 1번 문제에서 가장 큰 값을 가지고 있던
# 모델과 가장 낮은 값을 가지고 있던 모델 간의 운행 일수 대비 운행거리 평균이 다른지
# 적절한 통계 검정을 수행하고 p-value를 소수점 세자리 이하는 버리고 소수점
# 두자리까지 기술하고 기각 여부를 Y / N로 답하시오. (등분산을 가정하고 equal_var = 
# True / var.equal = T로 분석을 실행하시오.)
# (답안 예시) 0.23, Y
# =============================================================================

q10_2 = q10_1_1.copy()
q10_2['km_per_day'] = q10_2['km']/q10_2['age_in_days']

big = q10_2[q10_2.model == 'lounge']['km_per_day']
small = q10_2[q10_2.model == 'sport']['km_per_day']

from scipy.stats import ttest_ind

ttest_ind(big, small, equal_var = True)
# Ttest_indResult(statistic=1.1025375913936746, pvalue=0.27047828249848516)

# (정답) 0.27, N
# 네네 유의수준 0.05보다 작아야 귀무가설을 기각하니까 기각 못해서 N






#%%

# =============================================================================
# 3.독립변수로 engine_power, age_in_days, km를 사용하고 종속변수로 price를 사용하여
# 모델별 선형회귀분석을 수행하고, 산출된 모형을 사용하여 다음과 같은 조건의
# 중고차에 대한 가격을 예측하고 예측된 가격을 정수부만 기술하시오.
# - model : pop / engine_power : 51 / age_in_days : 400 / km : 9500 / previous_owners : 2

# (답안 예시) 12345
# =============================================================================

q10_3 = q10_1_1.copy()

from sklearn.linear_model import LinearRegression

x_var = ['engine_power', 'age_in_days', 'km']

lm = LinearRegression().fit(q10_3[x_var],q10_3.price)

new_data = pd.DataFrame({
    'engine_power' : [51],
    'age_in_days' : [400],
    'km' : [9500]
    })
# ValueError: If using all scalar values, you must pass an index -> []으로 넣음

new_data2 = np.array([[51, 400, 9500]])

lm.predict(new_data)
lm.predict(new_data2)

# (정답) 10463












