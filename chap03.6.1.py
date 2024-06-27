#index 다루기

import seaborn as sns

#seaborn 패키지의 mpg 데이터셋을 사용
df=sns.load_dataset('mpg')
print(df.head())
print()
print()

#set_index() 메소드를 사용하여 인덱스 설정
#set_index() 내에 인덱스로 설정하고자 하는 열을 입력하면 해당 열이 인덱스로 변경되며
#inplace=True 를 입력하면 원본 객체를 변경한다
df.set_index('name', inplace=True)
print(df.head())
print()
print()

#인덱스를 순서대로 정렬(sort_index())
#sort_index() 메서드를 통해 인덱스가 알파벳 순서로 정렬(A->Z)
df.sort_index(inplace=True)
print(df.head())
print()
print()

#인덱스의 순서가 내림차순(Z->A) 순서로 정렬하고 싶은 경우 ascending=False 입력
df.sort_index(inplace=True, ascending=False)
print(df.head())
print()
print()

#인덱스 재설정에는 reset_index() 메서드 사용
#reset_index()를 사용하면 인덱스가 다시 [0, 1, 2, ...]로 변경
df.reset_index(inplace=True)
print(df.head())
