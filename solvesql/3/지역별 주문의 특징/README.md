# [난이도 3] 지역별 주문의 특징

[문제 링크](https://solvesql.com/problems/characteristics-of-orders/)

지역별 주문의 특징

난이도 3

출제자 [데이터리안] 선미

정답률 28.81% (4795회 / 16646회)

US E-Commerce Records 2020 데이터베이스는 미국 이커머스 웹사이트의 판매 데이터를 담고 있습니다. records 테이블은 주문 번호, 주문 날짜, 주문 지역, 카테고리 등 주문의 상세 정보가 들어 있습니다. 이 데이터를 이용하여 미국의 각 지역별로 어떤 카테고리의 상품이 많이 판매되는지 알아보려고 합니다. region, category 별 주문량을 계산해 출력하는 쿼리를 작성해주세요.

결과 데이터 형식

결과 데이터는 아래와 같은 테이블 형태로 출력되어야 하고, Region 컬럼 기준 오름차순으로 정렬되어 있어야 합니다.

| Region  | Furniture | Office Supplies | Technology |
| ------- | --------- | --------------- | ---------- |
| Central |           |                 |            |
| East    |           |                 |            |
| South   |           |                 |            |
| West    |           |                 |            |

결과 데이터의 각 컬럼은 다음과 같은 의미를 갖습니다.

- `Region` - 주문 지역
- `Furniture` - 해당 지역 내 가구(’Furniture’) 주문 수
- `Office Supplies` - 해당 지역 내 오피스 물품(’Office Supplies’) 주문 수
- `Technology` - 해당 지역 내 전자기기(’Technology’) 주문 수
