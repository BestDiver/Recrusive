# # 퀴즈 개구리가 밟은 발판 return하기
# #arr[i] 만큼 점프

# #3 1 1 2
# arr = [2,0,1,1,3,5,1]

# def abc(index):
#    if index >= len(arr):
#        return
#    abc(index+arr[index])
#    print(arr[index],end=' ')
# abc(0)

# #카드 뽑기해서 합 구하기

# arr = [3,7,1,2]
# sum = 0
# def abc(level,sum):

#    if level == 3:
#        print(sum,end=' ')
#        return

#    for i in range(4):
#        abc(level+1,sum +arr[i])

# abc(0,0)



arr = [2,7,1,4,3]
N = int(input())
# 다음 숫자가 무작위로 섞여있는 N개의 카드 묶음에서
# 각각 1개씩 카드를 뽑아서 더했을때 합이 20이 넘는 경우개수
# set써도 되나
#깊이우선탐색
cnt = 0
def abc(level,sum):
   global cnt
   if sum > 20:
       cnt+= 1
       return
   if level == N:
       if sum > 20:
           cnt += 1
       return
   for i in range(5):
       abc(level+1,sum+arr[i])
abc(0,0)
print(cnt)

