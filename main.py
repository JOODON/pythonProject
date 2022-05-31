##파이썬 슬라이더
jumin="011111-3001154"
print("성별:"+jumin[7])
print("연:"+jumin[0:2])
print("생년월일"+jumin[:6])
print("뒤 7자리"+jumin[7:])
print("뒤 (뒤에서 부터 출력)7자리"+jumin[-7:])

##문자열 함수
python="python is Amazing"
print(python.upper())
print(python.lower())
print(python.isupper())
print(len(python))
print(python.replace("python","Java"))
index=python.index("n")
print(index)
index=python.index("n",index+1)
print(index)

##find와 index의 차이
# print(python.index('java'))오류를 출력
print(python.find("java"))##-1로 주고 계속 진행
##문자열 갯수 새기 
print(python.count("n"))##총 몇개가 들어가는지 
