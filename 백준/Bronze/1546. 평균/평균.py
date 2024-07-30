## 입력
# 과목 개수
N = int(input())

# 현재 성적
scores = list(map(int, input().split(' ')))

## 점수 계산
# 최댓값
M = max(scores)
# 점수 수정
new_scores = [score/M * 100 for score in scores] # list comprehension

# 새로운 점수 평균
score_sum = 0
for score in new_scores:
    score_sum += score
score_mean = score_sum / N

## 출력
print(score_mean)