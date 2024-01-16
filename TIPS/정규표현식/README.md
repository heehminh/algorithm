# 정규표현식

## 1. 정규 표현식의 기초, 메타 문자

메타 문자: 원래 그 문자가 가진 뜻이 아니라 특별한 의미를 가진 문자  
종류: `. ^ $ * + ? { } [ ] \ | ( )`

### 1-1. [ ] 문자 - 문자 클래스

정규 표현식이 `[abc]`라면 이 표현식의 의미는 a, b, c 중 한 개의 문자와 매치를 뜻함.  
[ ] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미함.

- `[a-c]` == `[abc]`
- `[0-5]` == `[012345]`
- `[a-zA-Z]`: 모든 알파벳
- `[0-9]`: 모든 숫자
- `[^0-9]`: 숫자가 아닌 문자 (^: not)

#### 자주 사용하는 문자 클래스 (대문자로 사용된 것은 소문자의 반대)

`\d`: 숫자, `\D`: 숫자가 아님 `[^0-9]`  
`\s`: 화이트스페이스, `\S`: `[^ \t\n\r\f\v]`  
`\w`: 문자+숫자, `\W`: 문자+숫자가 아닌 문자 `[^a-zA-Z0-9_]`

### 1-2. .(dot) 문자 - `\n`을 제외한 모든 문자

줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치

> 정규식을 작성할 때 `re.DOTALL` 옵션을 주면 . 문자와 `\n` 문자도 매치됨.

`a.b` == `a+모든문자+b`  
`a[.]b` == `a+.+b`

### 1-3. \* 문자 (반복)

`ca*t`: 바로 앞에 있는 문자 a가 0부터 무한대까지 반복될 수 있음. (무한대 == 2억 개)  
매치되는 문자열 예시: `ct`, `cat`, `caaaat`

### 1-4. + 문자 (반복)

`*`가 반복 횟수가 0부터라면 `+`는 반복 횟수가 1부터
`ca+t` == `c+a가 1번 이상 반복+t`

### 1-5. { } 문자와 ? 문자

`{m, n}`: 반복 횟수가 m부터 n까지인 문자와 매치

#### 1-5-1. `{m}`

`ca{2}t` == `c+a를 반드시 2번 반복+t`  
매치되는 문자열: `caat`

#### 1-5-2. `{m, n}`

`ca{2,5}t` == `c+a를 2~5회 반복+t`  
매치되는 문자열: `caat`, `caaaaat`

#### 1-5-3. `?`

`?` == `{0, 1}`  
`ab?c` == `a+b가 있어도 되고 없어도 됨+c`

## 2. 파이썬에서 정규 표현식을 지원하는 re 모듈

```
import re
p = re.compile('ab*')
```

## 3. 정규식을 이용한 문자열 검색

- `match()`: 문자열의 처음부터 정규식과 매치되는지 조사.
- `search()`: 문자열 전체를 검색하여 정규식과 매치되는지 조사.
- `findall()`: 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴.
- `finditer()`: 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴.

### 3-1. match

```
n = p.match("python")
print(n)
# <re.Match object; span=(0, 6), match='python'>
# [a-z]+ 정규식에 부합되므로 match 객체가 리턴됨
```

```
m = p.match("3 python")
print(m) # None
```

### 3-2. search

```
m = p.search("python")
print(m) # <re.Match object; span=(0, 6), match='python'>
```

```
m = p.search("3 python")
print(m) # <re.Match object; span=(2, 8), match='python'>
```

### 3-3. findall

패턴과 매치되는 모든 값을 찾아 리스트로 리턴

```
result = p.findall("life is too short")
print(result) # ['life', 'is', 'too', 'short']
```

### 3-4. finditer

finditer는 findall과 동일하지만, 그 결과 반복 가능한 객체를 리턴, 반복 가능한 객체가 포함되는 각각의 요소는 match 객체.

```
result = p.finditer("life is too short")

for r in result:
    print(r)

# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
```

## 4. match 객체의 메서드

- 어떤 문자열이 매치되었는가?
- 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

`group`: 매치된 문자열을 리턴한다.  
`start`: 매치된 문자열의 시작 위치를 리턴한다.  
`end`: 매치된 문자열의 끝 위치를 리턴한다.  
`span`: 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.

```
m = p.match("python")
m.group() # 'python'
m.start() # 0
m.end() # 6
m.span() # (0, 6)
```

## 5. 컴파일 옵션

- `DOTALL(S)`: `.`(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치될 수 있게 함
- `IGNORECASE(I)`: 대소문자에 관계없이 매치될 수 있게 함
- `MULTILINE(M)`: 여러 줄과 매치될 수 있게함, `^`, `$` 메타 문자 사용과 관계있는 옵션

> 옵션을 사용할 때 `re.DOTRALL`처럼 전체 옵션 이름을 써도 되고, `re.S`처럼 약어를 써도 됨

### 5-1. DOTALL, S

`.` 메타 문자는 `\n`을 제외한 모든 문자와 매치되는 규칙이 있음. 만약 `\n` 문자도 포함하여 매치하고 싶다면 `re.DOTALL` 또는 `re.S` 옵션을 사용해 정규식을 컴파일

```
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m) # None
```

```
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m) # <re.Match object; span=(0, 3), match='a\nb'>
```

### 5-2. IGNORECASE, I

`re.IGNORECASE` 또는 `re.I` 옵션은 대소문자 구별없이 매치를 수행할 때 사용하는 옵션

```
p = re.compile('[a-z]+', re.I)
p.match('python') # <re.Match object; span=(0, 6), match='python'>
p.match('Python') # <re.Match object; span=(0, 6), match='Python'>
p.match('PYTHON') # <re.Match object; span=(0, 6), match='PYTHON'>
```

`[a-z]+` 정규식은 소문자만을 의미하지만, `re.I` 옵션으로 대소문자 구별없이 매치됨

### 5-3. MULTILINE, M

`re.MULTILINE` 또는 `re.M` 옵션은 `^`, `$`와 연관이 있다. -> 문자열의 각 줄마다 적용

- `^`: 문자열의 처음, `^python`: 문자열의 처음은 항상 `python`으로 시작해야 매치됨.
- `$`: 문자열의 마지막, `python$`: 문자열의 마지막은 항상 `python`으로 끝나야 매치됨.
- 예시

  ```
  import re
  p = re.compile("^python\s\w+")

  data = """python one
  life is too short
  python two
  you need python
  python three"""

  print(p.findall(data)) # ['python one']
  ```

  정규식 `^python\s\w+`: python이란 문자열로 시작하고 . 그뒤에 화이트 스페이스, 그 뒤에 단어가 와야 한다.

`^` 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶을 때 -> `re.MULTILINE` 또는 `re.M` 사용

```
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
# ['python one', 'python two', 'python three']
```
