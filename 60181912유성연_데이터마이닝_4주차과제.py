#60181912 유성연
#데이터마이닝 과제 4주차
import numpy as np

def main():
    Score = np.random.randint(100, size=(10, 4))
    print(Score) # 원래 점수
    prob1(Score) # 함수호출
    prob2(Score)# 함수호출
    prob3(Score)# 함수호출
    
    problem3 = prob3(Score) #return값 호출하여 대입
    prob4(Score,problem3) # 함수호출

def prob1(Score):
    print("------------------------------------------------")
    print("---국어--영어--수학--과학--------------------------")
    problem1 = np.where(Score < 70, 'D', np.where(Score < 80, 'C', np.where(Score < 90, 'B', 'A')))
    print(problem1)

def prob2(Score):
    print("------------------------------------------------")
    print("---국어--영어--수학--과학--------------------------")
    problem2 = np.array(Score)
    avg = np.zeros(6)

    for i in range(0,4,1):
        avg[i] = Score[:,i].sum()/10
    for j in range(0,4,1):
        problem2[:,j] = Score[:,j] - avg[j]
    print(problem2)
    return avg;

def prob3(Score):
    print("------------------------------------------------")
    print("---국어--영어--수학--과학--총합---------------------")
    sum = np.zeros(10)
    sumarray = sum.reshape(10,1)
    for i in range(0,10,1):
        sumarray[i] = Score[i,:].sum()
    problem3 = np.concatenate([Score,sumarray],axis=1)
    print(problem3)
    return problem3

def prob4(Score, problem3):
    print("------------------------------------------------")
    print("---국어----영어----수학----과학----총합-----평균-----")
    avg = np.zeros(6)
    for i in range(0, 4, 1):
        avg[i] = Score[:, i].sum() / 10

    average = np.zeros(10)
    averagearray = average.reshape(10,1)
    for i in range(0,10,1):
        averagearray[i] = problem3[i,4]/4
    problem4 = np.concatenate([problem3, averagearray],axis=1)
    avg[4] = problem4[:,4].sum()/10
    avg[5] = problem4[:,5].sum()/10
    pr4= np.concatenate([problem4, [avg]], axis=0)
    print(pr4)

main()
