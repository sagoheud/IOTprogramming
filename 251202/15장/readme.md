# Pandas 데이터 과학 가이드

Python Pandas를 활용한 데이터 분석 및 시각화 완벽 가이드

## 목차
- [데이터 과학이란?](#데이터-과학이란)
- [Pandas 소개](#pandas-소개)
- [데이터 구조](#데이터-구조)
- [데이터 읽기/쓰기](#데이터-읽기쓰기)
- [데이터 선택과 필터링](#데이터-선택과-필터링)
- [데이터 정렬](#데이터-정렬)
- [행/열 추가 및 삭제](#행열-추가-및-삭제)
- [통계 분석](#통계-분석)
- [그룹화와 집계](#그룹화와-집계)
- [데이터 시각화](#데이터-시각화)
- [피벗 테이블](#피벗-테이블)
- [데이터 병합](#데이터-병합)
- [결손값 처리](#결손값-처리)

## 데이터 과학이란?

데이터 과학은 대량의 데이터에서 의미 있는 정보를 추출하는 학문입니다.

### 실생활 활용 예시
- 카드 결제 데이터로 상권 분석
- 산악기상 데이터로 산림재해 예측
- CCTV 데이터로 범죄 발생 패턴 분석
- 택시 승하차 정보로 심야버스 노선 설계
- 지하철 승하차 데이터 분석

### 데이터 처리 절차
1. **데이터 수집** (Data Collection)
2. **데이터 정제** (Data Cleaning)
3. **데이터 분석** (Data Analysis)
4. **데이터 시각화** (Data Visualization)
5. **의사결정** (Decision Making)

## Pandas 소개

**Pandas**는 Python에서 가장 강력한 데이터 분석 라이브러리입니다.

### 주요 기능
- CSV, Excel, TSV 파일 읽기/쓰기
- 데이터 필터링 및 정렬
- 통계 계산 (평균, 상관관계 등)
- 그룹화 및 집계
- 결손값 처리
- 데이터 병합

```python
import pandas as pd
```

## 데이터 구조

### 시리즈 (Series) - 1차원 데이터

```python
# 리스트에서 시리즈 생성
data = ['Kim', 'Park', 'Lee', 'Choi']
ser = pd.Series(data)
print(ser)
# 0    Kim
# 1    Park
# 2    Lee
# 3    Choi
```

### 데이터프레임 (DataFrame) - 2차원 데이터

```python
# 딕셔너리에서 데이터프레임 생성
data = {
    'Name': ['Kim', 'Park', 'Lee', 'Choi'],
    'Age': [20, 23, 21, 26]
}
df = pd.DataFrame(data)
print(df)
#   Name  Age
# 0  Kim   20
# 1  Park  23
# 2  Lee   21
# 3  Choi  26

# 인덱스 지정
df = pd.DataFrame(data, index=["학번 1", "학번 2", "학번 3", "학번 4"])
```

## 데이터 읽기/쓰기

### CSV 파일 읽기

```python
# 기본 읽기
titanic = pd.read_csv("titanic.csv")

# 특정 열을 인덱스로 지정
titanic = pd.read_csv('titanic.csv', index_col=0)

# 데이터 타입 확인
print(titanic.dtypes)
```

### 엑셀 파일 저장 및 읽기

```python
# 엑셀로 저장
titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)

# 엑셀 읽기
titanic = pd.read_excel('titanic.xlsx', sheet_name='passengers')
```

### 데이터 미리보기

```python
# 처음 5행 (기본값)
titanic.head()

# 처음 8행
titanic.head(8)

# 마지막 5행
titanic.tail()

# 기본 정보
titanic.info()

# 통계 요약
titanic.describe()
```

## 데이터 선택과 필터링

### 단일 열 선택

```python
# 한 개 열 선택
ages = titanic["Age"]

# 여러 열 선택
titanic[["Name", "Age", "Sex"]]
```

### 조건 필터링

```python
# 20세 미만 승객
below_20 = titanic[titanic["Age"] < 20]

# 1등석 또는 2등석 승객
first_or_second = titanic[titanic["Pclass"].isin([1, 2])]

# 여러 조건 조합
young_females = titanic[(titanic["Age"] < 30) & (titanic["Sex"] == "female")]
```

### 위치 기반 선택

```python
# loc: 레이블 기반 인덱싱
titanic.loc[titanic["Age"] < 20, "Name"]

# iloc: 정수 위치 기반 인덱싱
titanic.iloc[20:23, 5:7]  # 20~22행, 5~6열
```

## 데이터 정렬

```python
# 단일 열 정렬 (오름차순)
titanic.sort_values(by="Age")

# 내림차순 정렬
titanic.sort_values(by="Age", ascending=False)

# 다중 열 정렬
titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
```

## 행/열 추가 및 삭제

### 열 추가

```python
countries = pd.read_csv("countries.csv")

# 새 열 계산하여 추가
countries["density"] = countries["population"] / countries["area"]
```

### 행 추가

```python
# 새 데이터프레임 생성
new_row = pd.DataFrame({
    "code": ["CA"],
    "country": ["Canada"],
    "area": [9984670],
    "capital": ["Ottawa"],
    "population": [34300000]
})

# 기존 데이터프레임에 추가
df2 = countries.append(new_row, ignore_index=True)
```

### 행 삭제

```python
# 인덱스 2번 행 삭제
countries.drop(index=2, axis=0, inplace=True)
```

### 열 삭제

```python
# capital 열 삭제
countries.drop(["capital"], axis=1, inplace=True)
```

## 통계 분석

### 기본 통계 함수

```python
# 평균
titanic["Age"].mean()

# 중간값
titanic[["Age", "Fare"]].median()

# 최댓값/최솟값
titanic["Age"].max()
titanic["Age"].min()

# 표준편차
titanic["Age"].std()

# 분산
titanic["Age"].var()

# 합계
titanic["Age"].sum()

# 개수
titanic["Pclass"].count()
```

### 값의 빈도수

```python
# 각 값의 개수
titanic["Pclass"].value_counts()
# 3    491
# 1    216
# 2    184
```

## 그룹화와 집계

### 단일 기준 그룹화

```python
# 성별로 그룹화하여 평균 나이 계산
titanic[["Sex", "Age"]].groupby("Sex").mean()
#         Age
# Sex
# female  27.915709
# male    30.726645
```

### 다중 기준 그룹화

```python
# 성별과 등급으로 그룹화
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# Sex     Pclass
# female  1         106.125798
#         2          21.970121
#         3          16.118810
# male    1          67.226127
#         2          19.741782
#         3          12.661633
```

## 데이터 시각화

### 기본 설정

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Hong', 'Chung', 'Jang'],
    'age': [22, 26, 78, 17, 46, 32, 21],
    'city': ['Seoul', 'Busan', 'Seoul', 'Busan', 'Seoul', 'Daejun', 'Daejun'],
    'children': [2, 3, 0, 1, 3, 4, 3],
    'pets': [0, 1, 0, 2, 2, 0, 3]
})
```

### 선 그래프

```python
df.plot(kind='line', x='name', y='pets', color='red')
plt.show()
```

### 중첩 그래프

```python
ax = plt.gca()
df.plot(kind='line', x='name', y='children', ax=ax)
df.plot(kind='line', x='name', y='pets', color='red', ax=ax)
plt.show()
```

### 막대 그래프

```python
df.plot(kind='bar', x='name', y='age')
plt.show()
```

### 산포도

```python
df.plot(kind='scatter', x='children', y='pets', color='red')
plt.show()
```

### 그룹별 막대 그래프

```python
df.groupby('city')['name'].nunique().plot(kind='bar')
plt.show()
```

### 히스토그램

```python
df[['age']].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100], rwidth=0.8)
plt.show()
```

## 피벗 테이블

피벗 테이블은 데이터를 요약하여 2차원 테이블로 표현합니다.

### 단일 인덱스 피벗

```python
# 성별로 그룹화하여 평균 계산
table = pd.pivot_table(data=titanic, index=['Sex'])
#         Age        Fare      Parch    Pclass    SibSp  Survived
# Sex
# female  27.915709  44.479818  0.649682  2.159236  0.694268  0.742038
# male    30.726645  25.523893  0.235702  2.389948  0.429809  0.188908

# 그래프로 표시
table.plot(kind="bar")
```

### 다중 인덱스 피벗

```python
# 성별과 등급으로 그룹화
table = pd.pivot_table(titanic, index=['Sex', 'Pclass'])
```

### 특정 집계 함수 적용

```python
# 열마다 다른 함수 적용
table = pd.pivot_table(
    titanic,
    index=['Sex', 'Pclass'],
    aggfunc={'Age': np.mean, 'Survived': np.sum}
)
```

### 특정 값만 집계

```python
# 생존율만 계산
table = pd.pivot_table(
    titanic,
    index=['Sex', 'Pclass'],
    values=['Survived'],
    aggfunc=np.mean
)
table.plot(kind='bar')
```

### 열 기준 피벗

```python
# 행: 성별, 열: 등급
table = pd.pivot_table(
    titanic,
    index=['Sex'],
    columns=['Pclass'],
    values=['Survived'],
    aggfunc=np.sum
)
table.plot(kind='bar')
```

## 데이터 병합

### merge() - 공통 열 기준 병합

```python
df1 = pd.DataFrame({
    'employee': ['Kim', 'Lee', 'Park', 'Choi'],
    'department': ['Accounting', 'Engineering', 'HR', 'Engineering']
})

df2 = pd.DataFrame({
    'employee': ['Kim', 'Lee', 'Park', 'Choi'],
    'age': [27, 34, 26, 29]
})

# 공통 열(employee)로 병합
df3 = pd.merge(df1, df2)
#   employee    department  age
# 0   Kim       Accounting   27
# 1   Lee       Engineering  34
# 2   Park      HR           26
# 3   Choi      Engineering  29
```

### join() - 인덱스 기준 결합

```python
# 인덱스를 기준으로 결합
df1.join(df2, lsuffix='_left', rsuffix='_right')
```

### concat() - 행/열 연결

```python
# 행 방향으로 연결
pd.concat([df1, df2], axis=0)

# 열 방향으로 연결
pd.concat([df1, df2], axis=1)
```

## 결손값 처리

Pandas는 결손값(missing value)을 `NaN`으로 표현합니다.

### 결손값 확인

```python
# 결손값 확인
df.isnull()

# 결손값 개수
df.isnull().sum()

# 결손값이 있는 행 확인
df[df.isnull().any(axis=1)]
```

### 결손값 삭제

```python
# 결손값이 있는 행 모두 삭제
df.dropna()

# 모든 값이 NaN인 행만 삭제
df.dropna(how="all")

# 특정 열에서 결손값이 있는 행 삭제
df.dropna(subset=['Age'])
```

### 결손값 채우기

```python
# 0으로 채우기
df_0 = df.fillna(0)

# 평균값으로 채우기
df.fillna(df.mean()['area'])

# 특정 값으로 채우기
df['Age'].fillna(30, inplace=True)

# 앞/뒤 값으로 채우기
df.fillna(method='ffill')  # 앞 값으로
df.fillna(method='bfill')  # 뒤 값으로
```

## 실전 예제: 타이타닉 데이터 분석

### 데이터 로드 및 기본 정보

```python
import pandas as pd

# CSV 파일 읽기
titanic = pd.read_csv("titanic.csv")

# 데이터 구조 확인
print(titanic.head())
print(titanic.info())
print(titanic.describe())
```

### 분석 질문들

```python
# 1. 최고령 승객의 나이는?
print(titanic["Age"].max())  # 80.0

# 2. 평균 연령은?
print(titanic["Age"].mean())  # 29.7

# 3. 20세 미만 승객 수는?
print(len(titanic[titanic["Age"] < 20]))

# 4. 성별 생존율은?
survival_by_sex = titanic.groupby("Sex")["Survived"].mean()
print(survival_by_sex)

# 5. 등급별 평균 운임은?
fare_by_class = titanic.groupby("Pclass")["Fare"].mean()
print(fare_by_class)

# 6. 시각화
titanic.groupby("Pclass")["Survived"].mean().plot(kind='bar')
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()
```

## 유용한 팁

### 난수로 데이터프레임 생성

```python
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 100, size=(5, 4)),
    columns=list('ABCD')
)
```

### 체이닝 메서드

```python
# 여러 작업을 연결하여 수행
result = (titanic
          .dropna(subset=['Age'])
          .groupby('Pclass')['Age']
          .mean()
          .sort_values(ascending=False))
```

### 조건부 열 생성

```python
# 나이 그룹 생성
titanic['AgeGroup'] = pd.cut(
    titanic['Age'],
    bins=[0, 18, 35, 60, 100],
    labels=['Child', 'Young', 'Middle', 'Senior']
)
```

## 주요 함수 요약

| 함수 | 설명 |
|------|------|
| `read_csv()` | CSV 파일 읽기 |
| `to_csv()` | CSV 파일 저장 |
| `head()` | 처음 n행 표시 |
| `tail()` | 마지막 n행 표시 |
| `describe()` | 통계 요약 |
| `info()` | 데이터 정보 |
| `groupby()` | 그룹화 |
| `sort_values()` | 정렬 |
| `drop()` | 행/열 삭제 |
| `dropna()` | 결손값 삭제 |
| `fillna()` | 결손값 채우기 |
| `merge()` | 데이터 병합 |
| `pivot_table()` | 피벗 테이블 생성 |
| `plot()` | 시각화 |

## 참고자료

- [Pandas 공식 문서](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [타이타닉 데이터셋](https://www.kaggle.com/c/titanic)

## 라이선스

이 문서는 교육 목적으로 작성되었습니다.
