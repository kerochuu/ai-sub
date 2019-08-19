import numpy as np
import csv
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

"""
./advertising.csv 에서 데이터를 읽어, X와 Y를 만듭니다.

X는 (200, 3) 의 shape을 가진 2차원 np.array,
Y는 (200,) 의 shape을 가진 1차원 np.array여야 합니다.

X는 TV, Radio, Newspaper column 에 해당하는 데이터를 저장해야 합니다.
Y는 Sales column 에 해당하는 데이터를 저장해야 합니다.
"""

# Req 1-1-1. advertising.csv 데이터 읽고 저장
X = []
Y = []

# Req 1-1-2. 학습용 데이터와 테스트용 데이터로 분리합니다.
X_train, X_test, Y_train, Y_test = train_test_split(None)

"""
Req 1-2-1.
LinearRegression()을 사용하여 학습합니다.

이후 학습된 beta값들을 학습된 모델에서 입력 받습니다.

참고 자료:
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
"""
'''
lrmodel = None

# Req 1-2-2. 학습된 가중치 값 저장
beta_0 = None
beta_1 = None
beta_2 = None
beta_3 = None

print("Scikit-learn의 결과물")
print("beta_0: %f" % beta_0)
print("beta_1: %f" % beta_1)
print("beta_2: %f" % beta_2)
print("beta_3: %f" % beta_3)

# Req. 1-3-1.
# X_test_pred에 테스트 데이터에 대한 예상 판매량을 모두 구하여 len(y_test) X 1 의 크기를 갖는 열벡터에 저장합니다.
X_test_pred = None

"""
Mean squared error값을 출력합니다.
Variance score값을 출력합니다.

함수를 찾아 사용하여 봅니다.
https://scikit-learn.org/stable/index.html
"""
# Req. 1-3-2. Mean squared error 계산
print("Mean squared error: %.2f" % None)
# Req. 1-3-3. Variance score 계산
print("Variance score: %.2f" % None)

# Req. 1-4-1.


def expected_sales(tv, rd, newspaper, beta_0, beta_1, beta_2, beta_3):
    """
    TV에 tv만큼, radio에 rd만큼, Newspaper에 newspaper 만큼의 광고비를 사용했고,
    트레이닝된 모델의 weight 들이 beta_0, beta_1, beta_2, beta_3 일 때
    예상되는 Sales 값을 출력합니다.
    """
    return


# Req. 1-4-2.
# test 데이터에 있는 값을 직접적으로 넣어서 예상 판매량 값을 출력합니다.
print("TV: {}, Radio: {}, Newspaper: {} 판매량: {}".format(
    X_test[3][0], X_test[3][1], X_test[3][2], Y_test[3]))

print("예상 판매량: {}".format(expected_sales(
    float(X_test[3][1]), float(X_test[3][1]), float(X_test[3][2]), beta_0, beta_1, beta_2, beta_3)))

"""
Req. 1-5. pickle로 lrmodel 데이터 저장
파일명: model.clf
"""

# Linear Regression Algorithm Part
# 아래의 코드는 심화 과정이기에 사용하지 않는다면 주석 처리하고 실행합니다.

"""
Req. 3-1-1.
N_LinearRegression():

Linear Regression 학습을 위한 알고리즘입니다.
학습데이터와 반복횟수를 받아서 최적의 직선(평면)으로 근사하는 가중치 값을 리턴합니다.

알고리즘 구성
1) 가중치 값인 beta_x, beta_3 초기화
2) Y label 데이터 reshape
3) 가중치 업데이트 과정 (iters번 반복)
3-1) prediction 함수를 사용하여 error 계산
3-2) gadient_beta 함수를 사용하여 가중치 값 업데이트
4) 가중치 값들 리턴

"""


def N_LinearRegression(X, Y, iters):
    """
    초기값 beta_0, beta_1, beta_2, beta_3 = 0
    여러가지 초기값을 실험해봅니다..
    초기값에 따라 iters간의 관계를 확인 가능합니다.
    """
    beta_x = None
    beta_3 = None

    # 행렬 계산을 위하여 Y데이터의 사이즈를 (len(Y),1)로 저장합니다.
    Y = Y.reshape(-1, 1)

    for i in range(iters):
        # 실제 값 y와 예측 값(prediction()함수를 사용)의 차이를 계산하여 error를 정의합니다.
        error = None
        # gradient_beta함수를 통하여 델타값들을 업데이트 합니다.
        beta_x_delta, beta_3_delta = gradient_beta(None)
        beta_x -= None
        beta_3 -= None

    return beta_x, beta_3


"""
Req. 3-1-2.
prediction():
beta값들을 받아서 예측값을 계산합니다.
X행렬의 크기와 beta의 행렬 크기를 맞추어 계산합니다.
"""

def prediction(None):
    # 예측 값을 계산하는 식을 만든다.
    equation = None

    return equation


"""
Req. 3-1-3.
gradient_beta():
beta값에 해당되는 gradient값을 계산하고 learning rate를 곱하여 출력합니다.
"""


def gradient_beta(X, error, lr):
    # beta_x를 업데이트하는 규칙을 정의한다.
    beta_x_delta = None
    # beta_3를 업데이트하는 규칙을 정의한다.
    beta_3_delta = None

    return beta_x_delta, beta_3_delta


# N_LinearRegression 학습 파트

# Req 3-2-4. challenge
# 학습률(learning rate)를 설정합니다. (권장: 1e-3 ~ 1e-6)
learning_rate = None
# 반복 횟수(iteration)를 설정합니다. (자연수)
iteration = None

# Req. 3-2-1. 모델 학습
N_beta_x, N_beta_3 = N_LinearRegression(None)

# Req. 3-2-2. 학습된 가중치 저장
print("\nN_LinearRegression의 결과물")
print("beta_0: %f" % None)
print("beta_1: %f" % None)
print("beta_2: %f" % None)
print("beta_3: %f" % None)

# Req. 3-3-1. 테스트 데이터의 예측 label값 계산
# X_test_pred에 테스트 데이터에 대한 예상 판매량을 모두 구하여 len(y_test) X 1 의 크기를 갖는 열벡터에 저장합니다.
N_X_test_pred = None

# Req. 3-3-2. Mean squared error 계산
print("Mean squared error: %.2f" % None)
# Req. 3-3-3. Variance score 계산
print("Variance score: %.2f" % None)

# Req. 3-4-1. 예상 판매량 출력
print("TV: {}, Radio: {}, Newspaper: {} 판매량: {}".format(
    X_test[3][0], X_test[3][1], X_test[3][2], Y_test[3]))

print("예상 판매량: {}".format(expected_sales(
    float(X_test[3][0]), float(X_test[3][1]), float(X_test[3][2]), beta_0, beta_1, beta_2, beta_3)))
'''
