# [난이도 3] 작품이 없는 작가 찾기

[문제 링크](https://solvesql.com/problems/artists-without-artworks/)

작품이 없는 작가 찾기

난이도 3

출제자 박치완

정답률 69.78% (1651회 / 2366회)

Museum of Modern Art Collection 데이터베이스는 미국 뉴욕의 근현대 미술관인 MoMA의 작품과 작가 정보를 담고 있습니다. `artists` 테이블에는 MoMA에 등록된 작가들의 정보가 있고, `artworks_artists` 테이블에는 각 작품에 참여한 작가들의 정보가 들어있습니다. 하나의 작품에 여러 명의 작가가 참여할 수 있기 때문에, `artworks_artists` 테이블의 artwork_id 컬럼과 artist_id 컬럼은 N:M 관계입니다.

MoMA에 등록된 작가이지만 전시된 작품이 없는 작가들의 마지막 작품을 전시하는 기획전을 준비하려 합니다. MoMA에 등록되어있고, 현재 살아있지 않은 작가 중 MoMA에 등록된 작품이 없는 작가의 ID와 이름을 출력하는 쿼리를 작성해주세요. 쿼리 결과에는 아래 컬럼이 있어야 합니다.

- `artist_id` - 작가 ID
- `name` - 작가 이름
