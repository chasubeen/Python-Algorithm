# [Gold III] 나머지 합 - 10986 

[문제 링크](https://www.acmicpc.net/problem/10986) 

### 성능 요약

메모리: 142240 KB, 시간: 788 ms

### 분류

수학, 누적 합

### 제출 일자

2024년 7월 31일 10:34:46

### 문제 설명

<p>수 N개 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.</p>

<p>즉, A<sub>i</sub> + ... + A<sub>j</sub> (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.</p>

### 입력 

 <p>첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 10<sup>6</sup>, 2 ≤ M ≤ 10<sup>3</sup>)</p>

<p>둘째 줄에 N개의 수 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (0 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.</p>

### 🚀 Trouble Shooting
- 확실히 골드는 어렵구나..
  - 답 보면 이해하겠는데 아이디어 혼자 생각 못함..ㅎ
- 문제와 인덱스를 맞춰주기 위해 prefix를 설정하는 트릭은 많이 사용되구나.
  - 그런데 합 문제 아니고는 안될 것 같기두 하고.. 여러 문제를 봐야할 듯
- 계속 C언어처럼 초기 메모리 공간을 할당하려는 버릇(?)이 있는 것 같다.
  - 파이썬은 파이썬답게 풀이하기!

**[Pseudo code]**  
(copyright: Do it! 알고리즘 코딩 테스트)  
<img src = "https://github.com/user-attachments/assets/bd82da77-d596-4242-921e-1cd2b21ac1d1" width = 700 height = 700>


