# [난이도 5] 세션 재정의하기

[문제 링크](https://solvesql.com/problems/redefine-session/)

세션 재정의하기

난이도 5

출제자 [데이터리안] 선미

정답률 42.41% (1290회 / 3042회)

ga 테이블은 2022년 1월 데이터리안 웹사이트에서 발생한 Google Analytics 사용자 행동 데이터의 일부입니다. 사용자 아이디(`user_pseudo_id`), 세션 아이디(`ga_session_id`), 이벤트의 종류(`event_name`), 이벤트가 발생한 시각(`event_timestamp_kst`) 등의 정보를 가지고 있습니다.

데이터리안 웹사이트에 블로그 기능이 추가되면서 사용자들이 한 페이지에 체류하는 시간이 길어졌습니다. GA는 30분 이상 사용자가 행동하지 않을 때 세션을 종료하는데, 사용자들의 페이지 체류 시간이 증가했기 때문에 이 기준을 1시간으로 늘리려고 합니다.

세션을 종료하는 기준을 사용자가 1시간 이상 행동하지 않을 때로 수정하여, 사용자 'S3WDQCqLpK’의 세션을 재정의하고 로그 내 모든 세션의 시작 시각과 종료 시각을 출력하는 쿼리를 작성해주세요. 쿼리 결과는 세션 시작 시각 기준으로 정렬되어 있어야 합니다.

- user_pseudo_id - 사용자 아이디 (S3WDQCqLpK)
- session_start - 세션 시작 시각
- session_end - 세션 종료 시각

참고 자료

- How a web session is defined in Universal Analytics
