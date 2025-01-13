#print("Hello world! 깃허브 연결 테스트 입니다.")
#x = []
#print(len(x))

# import sys
# print(sys.maxsize)


# import time # time 라이브러리 import
# start = time.time() # 시작
 
# time.sleep(1) # 측정하고자 하는 코드 부분
 
# print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력


# def doesCircleExistForCommand(command):

#     if len(command)<1 or len(command)>2500:
#         return "문자열의 길이가 조건에 부합하지 않습니다" 

#     # 시작점의 좌표와 방향을 설정
#     x, y = 0, 0
#     direction = 0
    
#     # 움직임에 따라 방향을 확인하고 그에 따라서 좌표를 수정하는 함수를 선언
#     # 방향이 0일때는 위로 이동
#     # 방향이 1일때는 오른쪽으로 이동
#     # 방향이 2일때는 아래로 이동
#     # 방향이 3일때는 왼쪽로 이동
#     def move(x, y, direction):
#         if direction == 0:  
#             y += 1
#         elif direction == 1: 
#             x += 1
#         elif direction == 2: 
#             y -= 1
#         elif direction == 3: 
#             x -= 1
#         return x, y
    

#     # 명령어를 네 번 반복하여 로봇의 움직임을 확인
#     # 네 번 반복하면 원을 그리는지 혹은 원을 벗어나지 않는지 확인 가능
#     for i in range(4):  
#         for cmd in command:
#             if cmd not in ['G','R','L']:
#                 return  "조건에 부합하지 않는 문자가 포함"
#             if cmd == 'G':
#                 x, y = move(x, y, direction)
#             elif cmd == 'L':
#                 direction = (direction - 1) % 4
#             elif cmd == 'R':
#                 direction = (direction + 1) % 4
    
#     # 로봇이 처음 위치로 돌아왔다면 , 방향이 처음과 다를 경우 4번을 반복했을 때 원을 그리거나 특정 크기의 원에서 벗어나지 않는 것으로 간주 가능
#     if (x == 0 and y == 0) or direction != 0:
#         return "YES"
#     else:
#         return "NO"


# # 각 명령어 문자열을 요소로 가진 리스트를 파라미터로 가짐
# def doesCircleExist(commands):

#     if len(commands)<1 or len(commands)>10:
#         return "배열의 길이가 조건에 부합하지 않습니다" 
    
#     # 결과 저장을 위한 리스트 생성
#     results = []
#     #파라미터의 각 문자열을 각각 확인하고 결과를 저장
#     for command in commands:
#         results.append(doesCircleExistForCommand(command))
    
#     #결과 반환
#     return results


# commands = ["G", "LGR", "GGR"]
# result = doesCircleExist(commands)
# print(result)  # 출력: ['NO', 'NO, 'YES'] # 틀린 부분 


# def findSchedules(workHours, dayHours, pattern):

#     if workHours<1 or workHours>56:
#         return "주중에 일하는 시간이 범위에 맞지 않습니다"
    
#     if dayHours<1 or dayHours>8:
#         return "하루에 일하는 시간이 범위에 맞지 않습니다"
    
#     if len(pattern) !=7 :
#         return "패턴은 7자리여야 합니다"
    
#     for i in pattern:
#         if i not in ["0","1","2","3","4","5","6","7","8",'?']: # 틀린 부분 
#             return  "패턴은 1~8 그리고 ? 로만 입력해야 합니다"

#     # 백트레킹 함수 정의 (중간에 유효하지 않은 값이라면 되돌아감)
#     def backtrack(i, hours_left, current_pattern):
#         # 남은 시간이 0보다 작으면 유효하지 않은 경우이므로 종료
#         if hours_left < 0:
#             return
        
#         # 패턴의 끝까지 도달했을 때 남은 시간이 0이면 결과에 현재 패턴을 추가 (유효하지 않다면 추가하지 않고 되돌아감)
#         if i == len(pattern):
#             if hours_left == 0:
#                 result.append(''.join(map(str, current_pattern)))
#             return
        
#         # 현재 패턴이 '?'인 경우 가능한 모든 시간을 시도
#         if pattern[i] == '?':
#             for h in range(0, dayHours + 1):
#                 current_pattern[i] = h
#                 backtrack(i + 1, hours_left - h, current_pattern)
#                 current_pattern[i] = '?'

#         # '?'가 아닌 경우 해당 시간을 그대로 사용
#         else:
#             current_pattern[i] = int(pattern[i])
#             # 해당 시간 만큼을 제외하고 남은 시간으로 계산
#             backtrack(i + 1, hours_left - current_pattern[i], current_pattern)
#             current_pattern[i] = '?'

#     result = []

#     backtrack(0, workHours, list(pattern))

#     return result


# # 예시 사용
# workHours = 24
# dayHours = 6
# pattern = "08?4???"
# result = findSchedules(workHours, dayHours, pattern)
# print(result)



# def findSchedules(workHours, dayHours, pattern):
#     # 입력 검증
#     if workHours < 1 or workHours > 56:
#         return "주중에 일하는 시간이 범위에 맞지 않습니다"
    
#     if dayHours < 1 or dayHours > 8:
#         return "하루에 일하는 시간이 범위에 맞지 않습니다"
    
#     if len(pattern) != 7:
#         return "패턴은 7자리여야 합니다"
    
#     for i in pattern:
#         if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", '?']:
#             return "패턴은 1~8 그리고 ? 로만 입력해야 합니다"

#     # 백트래킹 함수 정의
#     def backtrack(i, hours_left, current_pattern):
#         # 남은 시간이 0보다 작으면 유효하지 않은 경우이므로 종료
#         if hours_left < 0:
#             return
        
#         # 패턴의 끝까지 도달했을 때 남은 시간이 0이면 결과에 현재 패턴을 추가
#         if i == len(pattern):
#             if hours_left == 0:
#                 result.append(''.join(map(str, current_pattern)))
#             return
        
#         # 현재 패턴이 '?'인 경우 가능한 모든 시간을 시도
#         if pattern[i] == '?':
#             for h in range(0, dayHours + 1):
#                 current_pattern[i] = h
#                 backtrack(i + 1, hours_left - h, current_pattern)
#                 current_pattern[i] = '?'  # 원래 상태로 되돌리기

#         # '?'가 아닌 경우 해당 시간을 그대로 사용
#         else:
#             current_pattern[i] = int(pattern[i])
#             # 해당 시간 만큼을 제외하고 남은 시간으로 계산
#             backtrack(i + 1, hours_left - current_pattern[i], current_pattern)
#             current_pattern[i] = '?'  # 원래 상태로 되돌리기

#     result = []
#     # 현재 패턴을 리스트로 변환하여 백트래킹 시작
#     backtrack(0, workHours, list(pattern))

#     return result

# # 예시 사용
# workHours = 24
# dayHours = 6
# pattern = "08?4???"
# result = findSchedules(workHours, dayHours, pattern)
# print(result)


# def largestSubgrid(grid, maxSum):
#     n = len(grid)
#     max_size = 0

#     # 모든 가능한 시작 위치와 크기 검사
#     for row in range(n):
#         for col in range(n):
#             # 최대 크기는 그리드의 크기에서 현재 위치(row, col)까지의 거리
#             for size in range(1, n - max(row, col) + 1):
#                 current_sum = 0
#                 # 현재 하위 그리드의 합 계산
#                 for i in range(size):
#                     for j in range(size):
#                         current_sum += grid[row + i][col + j]

#                 # 현재 하위 그리드의 합이 maxSum 이하인 경우
#                 if current_sum <= maxSum:
#                     max_size = max(max_size, size)
#                     print(current_sum)
#     return max_size

# # 예시 사용
# grid = [
#     [2, 2, 3],
#     [3, 2, 3],
#     [4, 3, 1]
# ]
# maxSum = 10
# result = largestSubgrid(grid, maxSum)
# print(result)  # 출력: 2