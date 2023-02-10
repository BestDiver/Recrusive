# 주사위 경우의 수 모두 출력하기 lv N branch 6
N = int(input())
arr = [1,2,3,4,5,6]
path = [0] * 1100
def abc(level):
   if level == N:
       for i in range(N):
           print(path[i],end='')
       print()
       return

   for i in range(6):
       path[level] = i +1
       abc(level + 1)

abc(0)
