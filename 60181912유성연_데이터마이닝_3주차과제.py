# 60181912 유성연 데이터마이닝 3주차과제
import numpy as np

def main():
    Score = np.random.randint(100, size=(10, 4))
    print(Score)  # 원래 점수
    data = np.array(['T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'T', 'T'])
    math(Score)
    sumScore(Score)
    boolScore(Score, data)
    Transpose(Score)

def math(Score):
    print("---------------")
    print(Score[0:10, 2:3])  # 10명 수학점수

def sumScore(Score):
    print("---------------")
    sum = Score[:, 0:1] + Score[:,1:2] +Score[:,2:3] +Score[:,3:4]
    print(sum)

def boolScore(Score, data):
    print("---------------")
    print(Score[data == 'T'])  # 1,5,7,9,10번째 점수

def Transpose(Score):
    print("---------------")
    print(Score.T)  # 4 전치행렬

main()
