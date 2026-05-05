# [lv1] 정수 제곱근 판별 - 12934 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12934) 

### 구분

코딩테스트 연습 > 연습문제

### 제출 일자

2026년 05월 05일 20:16:07

### 문제 설명

<p>임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.<br>
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>n은 1이상,  50000000000000 이하인 양의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>121</td>
<td style="text-align: center">144</td>
</tr>
<tr>
<td>3</td>
<td style="text-align: center">-1</td>
</tr>
</tbody>
      </table>
<h6>입출력 예 설명</h6>

<p><strong>입출력 예#1</strong><br>
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.</p>

<p><strong>입출력 예#2</strong><br>
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges