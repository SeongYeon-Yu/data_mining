import random

def main():
    concatenate_list()
    calculateGrade()
    
def concatenate_list(): #문제1
    Lst1 = [random.randint(1,100) for i in range(20)]
    Lst2 = [random.randint(1,100) for i in range(20)]
    Lst = Lst1+Lst2
    Lst.sort() #중복된 값 보기 힘들어서 정렬했습니다!
    print('List : ',Lst)
    
    result = [] 
    for i in Lst:
        for j in Lst:
            result.append(str(str(i) + str(j)))
    result = list(set(Lst))
    print('중복된 값 제거된 List : ',result)
    
def calculateGrade(): #문제2

    answer= [[0,1,2,3,4,5,6,7,8,9],
              ['D','B','D','C','C','D','A','E','A','D']]

    student=[['A', 'B', 'A', 'C' ,'C' ,'D' ,'E' ,'E' ,'A' ,'D'],
             ['D', 'B', 'A', 'B' ,'C' ,'A' ,'E' ,'E' ,'A' ,'D'],
             ['E', 'D', 'D', 'A' ,'C' ,'B' ,'E' ,'E' ,'A' ,'D'],
             ['C', 'B', 'A', 'E' ,'D' ,'C' ,'E' ,'E' ,'A' ,'D'],
             ['A', 'B', 'D', 'C' ,'C' ,'D' ,'E' ,'E' ,'A' ,'D'],
             ['B', 'B', 'E', 'C' ,'C' ,'D' ,'E' ,'E' ,'A' ,'D'],
             ['B', 'B', 'A', 'C' ,'C' ,'D' ,'E' ,'E' ,'A' ,'D'],
             ['E', 'B', 'E', 'C' ,'C' ,'D' ,'E' ,'E' ,'A' ,'D']]

    for i in range(0,8):
        score=0
        for j in range(0,10):
            if student[i][j]==answer[1][j]:
                score += 1
        print(i," 번 학생의 정답 문항의 개수는 ",score,"입니다.")
        
main()
