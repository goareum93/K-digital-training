## 210609

## 평균, 분산, 공분산

### 평균 (mean)

평균값, 다 더해서 그 개수로 나눠줌.

![img](https://t1.daumcdn.net/cfile/tistory/99D87E4A5DF0496135)



### 편차 (deviation)

: **평균값으로부터의 차이.**

: 그러나 합계가 0임. --> 평균값을 기준으로 차이를 계산했기 때문.

: 고로 합계를 이용하여 흩어진 정도를 파악할 수 없음.

![img](https://t1.daumcdn.net/cfile/tistory/99D334445DF0494B34)

### 분산 (variance)

: 흩어진 정도를 파악하고자하니 편차는 합계가 0이라 이용할 수 없음..

: 대신 **편차에서 부호를 없애고 사용하기 위해 제곱을 하고 다시 평균**을 냄.



### 표준편차 (standard deviation)

: 분산(variance)는 단위도 함께 제곱되면서 그 의미가 애매해지는데 이를 위해 **분산(variance)의 제곱근**인 표준편차를 사용함.

![img](https://t1.daumcdn.net/cfile/tistory/997E31365DF04B7502)



### 공분산 (covariance)

: 위에서 봤던 분산과 표준편차들은 하나의 변수를 위한 값이었음.

: 공분산은 **서로 다른 두 변수 사이의 관계를 보기 위함**. 

: 두 변수가 서로 다른 단위를 사용하더라도 신경쓰지않고 구하면 됨. --> 애초에 서로 다른 데이터 간 관계를 표현하는 지표를 사용했기 때문.

: **공분산의 절대값 크기는 아무런 의미가 없음!!!!**

![image-20210609145410412](readme.assets/image-20210609145410412.png)

- **Cov(X, Y) > 0** : 양의 관계에 있다고 표현. --> 어느 하나가 증가하면 다른 하나도 증가함

- **Cov(X, Y) < 0** : 음의 관계에 있다고 표현. --> 어느 하나가 증가하면 다른 하나는 감소함

- **Cov(X, Y) = 0** : 선형관계 없음

Reference :

https://hyeonnii.tistory.com/292



------



## 분류모델

### Confusion matrix

- True Positive(TP) : 실제 True인 정답을 True라고 예측 (정답)

- False Positive(FP) : 실제 False인 정답을 True라고 예측 (오답)

- False Negative(FN) : 실제 True인 정답을 False라고 예측 (오답)

- True Negative(TN) : 실제 False인 정답을 False라고 예측 (정답)

  ![image-20210609113614482](readme.assets/image-20210609113614482.png)



### Accuracy(정확도)

정확도란 전체 중에서 정답을 맞춘 비율

![img](https://blog.kakaocdn.net/dn/4DfPN/btqELziI6tH/lYckUKFZb0RmEwYjBGcQK1/img.png)



### Precision(정밀도)

![img](https://blog.kakaocdn.net/dn/Z1zbF/btqELyjMO93/qKHW4lBQhB5bwC1dV7AmaK/img.png)

정밀도란 모델이 True라고 분류한 것 중에서 실제 True인 것의 비율이다.



### Recall(재현율)

![img](https://blog.kakaocdn.net/dn/rAJBK/btqEJiJpb5Q/dvLk6LAzrI9mBY87Rscc21/img.png)

재현율이란 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율이다.  sensitivity 또는 hit rate라고도 불리고 1에 가까울 수록 좋다. 재현율은 단점은 정밀도와 비슷하다.

 

Reference :

- https://rk1993.tistory.com/entry/%EB%AA%A8%EB%8D%B8-%EC%84%B1%EB%8A%A5-%ED%8F%89%EA%B0%80-%EC%A7%80%ED%91%9C-%ED%9A%8C%EA%B7%80-%EB%AA%A8%EB%8D%B8-%EB%B6%84%EB%A5%98-%EB%AA%A8%EB%8D%B8?category=880112



------



## PCA

### PCA를 왜 쓸까? 

PCA를 사용하면 다중공선성 문제, 차원의 저주 문제를 해결할 수 있고, 차원을 축소해주기때문에 사람이 쉽게 관찰하고 이해할 수 있는 2차원으로 데이터들을 보여줄 수 있기 때문에 사용한다.



### PCA는 어떤 알고리즘인가?

PCA는 차원축소 알고리즘으로 생각하기보다는 기존 변수를 조합해 새로운 변수를 만드는 변수 추출(Feature Extraction)기법

 이때, 변수 선택(Feature Selection) 기법과 용어가 헷갈릴 수 있는데

1. 변수 선택(Feature Selection) : 있는 변수 중 결과값을 잘 표현할 수 있는 변수를 (있는 변수들 중에서) 단순히 고르는것

2. 변수 추출(Feature Extraction) : 변수들을 조합해 새로운 변수를 만들어 결과값을 잘 표현하는 방법

좀 더 스마트하게 PCA 알고리즘을 설명해보면, 기존의 변수들을 선형 결합(linear combination)하여 새로운 변수를 만들어 내는 기법



### 차원의 저주 문제와 다중공선성 문제를 어떻게 해결?

#### 1) 차원의 저주

![image-20210609140607022](readme.assets/image-20210609140607022.png)

![image-20210609140617213](readme.assets/image-20210609140617213.png)

차원은 커졌지만 데이터의 양이 부족하다면, 차원의 일부 공간에 제한되서 혹은 공간별로 소수의 데이터만을 설명하기 때문에 학습된 것만 잘 맞추는 과적합(Overfitting) 문제가 발생할 수 있다.

따라서, PCA 알고리즘으로 차원을 줄여주게 된다면 데이터가 적은 차원에서 밀도있게 표현되기 때문에 차원의 저주 문제를 해결할 수 있다.

**고차원 → 저차원 으로 줄이게 된다면 계산량이 줄어드는 효과도 기대할 수 있음**



#### 2) 다중공선성(multicollinearity) 문제

다중공선성 문제는 변수들간의 상관관계가 높을때 문제가 발생한다.

유식하게 표현해보자면 독립변수들 간의 강한 상관관계가 나타날때 다중공선성 문제가 발생한다.

다중공선성이 왜 문제냐?

회귀분석의 가정(전제 조건)인 변수들간의 상관관계가 높으면 안된다는 가정을 위배함

상관계수가 높다면 X1, X2라는 변수가 있을때 오롯이 X1이 Y값에 어느정도 영향을 미쳤는지

X2값은 얼마나 영향을 미쳤는지 알 수 없다. 따라서 X1, X2에 붙게되는 계수(=회귀계수)를 신뢰할 수 없게된다.

따라서, PCA 알고리즘은 주성분 PC1과 PC2를 찾는 과정에서 두 변수가 직교해야하기때문에

두 변수 사이의 상관관계가 0으로 나타나 다중공선성 문제를 해결할 수 있게된다



Reference :

https://specialscene.tistory.com/11



------



## XGBoost: A Scalable Tree Boosting System  
- XG Boost와 엔트로피 관련 설명

  Reference : 

  https://brunch.co.kr/@hvnpoet/95

![image-20210609145725934](readme.assets/image-20210609145725934.png)

![image-20210609145736583](readme.assets/image-20210609145736583.png)

