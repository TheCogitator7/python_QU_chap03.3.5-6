import seaborn as sns

df=sns.load_dataset('titanic')
print(df.head())
print()
print()


#deck 열에는 203 개의 값 밖에 없음
print(df.info())
print()
print()


#isnull(): 결측치면 True를 유효한 데이터면 False 를 반환
#notnull() : 유효한 데이터면 True를, 결측치면 False를 반환
print(df.head().isnull())
print()
print()


#dropna() : 결측치가 있는 행 또는 열을 삭제
#891 개 였던 행이 182 개로 줄어듦.
print(df.dropna())
print()
print()

#subset=['age'], age 열 중에서 결측치가 있는 행을 삭제(axis=0 은 행 방향으로 동작)
print(df.dropna(subset=['age'], axis=0))
print()
print()

#axis=1은 결측치가 있는 열을 삭제(15개 행이 11개로 줄어듦)
print(df.dropna(axis=1))
print()
print()

#axis=1 은 결측치가 있는 열을 삭제, thresh=300 은 결측치가 300 개 이상 갖는 열을 삭제한다는 의미
#deck 열만 이 조건에 부합되어 삭제
print(df.dropna(axis=1, thresh=300))
print()
print()



#결측치를 대체하기
#결측치를 다른 값(예, 평균)으로 변경하는 것
df_2=df.copy()
print(df_2.head(6))
print()
print()


#'age' 열의 평균을 구하면 대략 30세가 나오는데 결측치를 해당 값으로 변경(fillna())
mean_age=df_2['age'].mean()
print(mean_age)
print()
print()


#'age' 열의 평균을 평균값으로 변경
df_2['age'].fillna(mean_age, inplace=True)
print(df_2['age'].head(6))
print()
print()

#embark_town의 결측치를 가장 데이터가 많은 'Southampton'으로 변경
df_2['embark_town'].fillna('Southampton', inplace=True)
print(df_2['embark_town'].head(10))
print()
print()

#결측치를 직전 행의 값으로 변경
#method='ffill' 를 입력하면 결측치가 나타나기 전의 값으로 바꾸어 주고
#method='bfill' 를 입력하면 결측치가 있는 아래의 행 중 결측치가 아닌 첫 번째 값으로 바꾸어 
df_2['deck_ffill']=df_2['deck'].fillna(method='ffill')
df_2['deck_bfill']=df_2['deck'].fillna(method='bfill')

print(df_2[['deck', 'deck_ffill', 'deck_bfill']].head(12))
print()
print()



