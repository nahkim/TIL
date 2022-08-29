# WEB

---

웹 사이트의 구성 요소

| -          | -                   |
| ---------- | ------------------- |
| HTML       | 웹 콘텐츠 의미/구조 |
| CSS        | 모양/표현           |
| Javascript | 기능/동작           |

[웹 사이트의 구성 요소](https://html-css-js.com)



### 웹 사이트와 브라우저

---



- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장
- ex) 크롬, 파이어폭스, 네이버웨일, 사파리 등



### 웹 표준

---

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)



HTML Living Standard



- 브라우저별 호환성 체크
  - [Can I use?](https://caniuse.com)



## 개발 환경 설정

---

### Visual Studio Code

- HTML/CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램

  - Open in browser

  - Auto Rename Tag

  - Auto Close Tag

  - Intellisense for CSS class names in HTML

  - HTML CSS Support



### 크롬 개발자 도구

- 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
- 주요 기능
  - Elements - DOM 탐색 및 CSS 확인 및 변경
    - Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listeners - 해당 요소에 적용된 이벤트 (JS)
  - Sources, Network, Performance, Application, Security, Audits 등





# HTML 기초

---

- HTML : Hyper Text Markup Language, 웹 페이지를 작성(구조화)하기 위한 언어
  - Hyper Text 
    - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
    - 웹 페이지를 다른 페이지로 연결하는 링크
  - Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - ex) HTML, Markdown
- 웹 페이지는 HTML 문서라고도 불리며, HTML 태그들로 구성된다.
- 각각의 HTML 태그는 웹 페이지의 디자인이나 기능을 결정하는데 사용됨



# HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HTML문서의 제목입니다.</title>
</head>
<body>
  <h1>제목 크기1입니다.</h1>
  <h2>제목 크기2입니다.</h2>
  <p>이 부분은 단락입니다.</p>
</body>
</html>
```

- !DOCTYPE html : 현재 문서가 HTML5 문서임을 명시

- html :  문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- title : HTML 문서의 제목
  - 웹 브라우저의 툴바에 표시됨
  - 웹 브라우저의 즐겨찾기에 추가할 때 즐겨찾기의 제목이 됨
  - 검색 엔진의 결과 페이지에 제목으로 표시됨
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용





### head

---



```html
<head>
  <!-- 브라우저 상단 타이틀 -->
  <title>HTML 수업</title>
  
  <!-- 문서 레벨 메타데이터 요소 -->
  <meta charset="UTF-8">
  
  <!-- 외부 리소스 연결 요소 (CSS파일, favicon 등) -->
  <link href="style.css" rel="stylesheet">
  
  <!-- 스크립트 요소 (JavaScript 파일/코드) -->
  <script src="javascript.js"></script>
  
  <!-- CSS 직접 작성 -->
  <style>
    p {
      color: black;
    }
  </style>
</head>
```



head 예시 : Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타 정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의



메타데이터 : 데이터의 데이터

ex) 사진데이터 : 0과 1로 이루어짐 -> 노출/조리개값, 셔터스피드, 장소, 시간, 사이즈 등 : 사진 데이터를 위한 데이터 = 메타데이터



### 요소 (element)

---

```html
<h1> <!-- (여는/시작)태그 -->
  contents
</h1> <!-- (닫는/종료)태그 -->
```

HTML의 요소는 **태그**와 **내용(contents)**로 구성되어 있다.



```html
<태그이름> // 시작 태그
</태그이름>	// 종료 태그
```

- HTML 태그는 보통 시작 태그(start tag, opening tag)와 종료 태그(end tag, closing tag)의 한쌍으로 구성
- 종료 태그는 시작 태그와 전부 똑같지만, 태그 이름 앞에 슬래시(/)가 존재
- 태그에 따라 시작 태그만 있는 태그도 존재 : 빈 태그(empty tag)



- HTML 요소는 "태그"를 사용해 문서의 다른 텍스트와 구분

  - 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - **<태그이름>content</태그이름>**
    - 여는 태그(opening tag) : **<태그이름>**
    - 닫는 태그(closing tag) : **</태그이름>**
    - 컨텐츠(content) : 요소의 내용 **content**
    - 요소(element) : 요소는 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어짐
  - 태그 안의 요소 이름은 대소문자를 구분하지 않는다.
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음) : 빈 태그(empty tag)
    - br, hr, img, input, link, meta

- 요소는 중첩(nested)될 수 있음

  - 요소의 중첩을 통해 하나의 문서를 구조화

  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함

    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음

  - ```html
    <p>다람쥐는 <strong>너무</strong> 귀여워</p>
    ```



### HTML with 개발자 도구

---

- elements : 해당 요소의 HTML 태그



## HTML 요소 구조

---



### 속성 (attribute)

---

```html
<a href="https://google.com"></a>
```

- a : 태그 이름
- href : 속성명

- https://google.com : 속성값



태그별로 사용할 수 있는 속성은 다르다.

속성은 HTML 요소 중에서도 언제나 시작 태그 내에서만 정의되며, 속성 이름과 속성값(value)으로 표현된다.



- 속성 (attribute) 작성 방식 통일하기

  - ```html
    <태그이름 속성일="속성값">

  - 속성 이름은 소문자로 작성

  - 속성값은 언제나 따옴표로 감싸기



- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 테그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음



#### HTML Global Attribute

---

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무효과가 없을 수 있음)
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
  - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - style : inline 스타일
  - title : 요소에 대한 추가 정보 지정
  - tabindex : 요소의 탭 순서

```html
<!DOCTYPe html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <!-- 주석 입니다. -->
  <h1>나의 첫번째 HTML</h1>
  <p>본문</p>
  <span>인라인 요소</span>
  <a href="http://www.naver.com">네이버로 이동!</a>
</body>
</html>
```



- 렌더링(Rendering)
  - 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정



### DOM(Document Object Model) 트리

---

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함



#### 인라인 / 블록 요소

---

- HTML 요소는 크게 인라인 / 블록 요소로 나눔

  ```html
  index.html
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <title>mySite</title>
  </head>
  <body>
    <!-- -->
    <h1 style="color: blue; font-size: 100px;">Hello</h1>
  	<!-- 해당 태그에 직접 style 속성을 활용 -->
  </body>
  </html>
  ```

  

- 인라인 요소는 글자처럼 취급

  ```html
  index.html
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <title>mySite</title>
  <!-- -->
  	<style>
    	h1 {
      	color: blue;
      	font-size: 100px;
    	}
  	</style>
  <!-- <head> 태그 내에 <style>에 지정 -->
  <body>
  </body>
  </html>
  ```

  

- 블록 요소는 한 줄 모두 사용

  ```html
  index.html
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <title>mySite</title>
    <!-- -->
    <link rel="stylesheet" href="mystyle.css">
  	<!-- 외부 CSS 파일을 <head>내 <link>를 통해 불러오기 -->
  </head>
  <body>
    <h1>This is my site</h1>
  </body>
  </html>
  
  
  ```

  ```css
  mystyle.css
  
  h1 {
  	color: blue;
  	font-size: 20px;
  }
  ```

  



## HTML 텍스트 요소

---

### 제목(Heading)

---

```html
<h1>제목1의 크기입니다.</h1>
<h2>제목2의 크기입니다.</h2>
<h3>제목3의 크기입니다.</h3>
<h4>제목4의 크기입니다.</h4>
<h5>제목5의 크기입니다.</h5>
<h6>제목6의 크기입니다.</h6>

<h>태그는 제목을 표현하기도 하지만 또 다른 중요역할을 함
여러 검색엔진은 각 웹 사이트의 내용을 바로 이 <h>태그를 이용하여 키워드를 수집하고, 그 내용을 파악함
  => HTML 문서에 포함되는 제목은 <h>태그로 작성해야만 검색엔진에 의해 제대로 검색될 확률을 높인다.
```



### 단락(Paragraph)

---

```html
<p>여기서부터 단락입니다.</p>
```

- 단락이란 내용상 끊어서 구분할 수 있는 하나하나의 부분, 문단이라고도 불림

  

- HTML 코드에서 띄어쓰기나 줄 나누기를 여러번 하더라도 웹 브라우저를 통해 나나타는 화면에는 전혀 영향을 주지 않음! => br 태그 사용해야함

- ```html
  <p>
    줄나누기1<br>
    줄나누기2<br>
  </p>
  ```

- 만약 HTML 코드에서 작성한 텍스트 서식을 그대로 표현하려면 pre 태그를 사용해야함

- ```html
  <pre>
  줄나누기1
  줄나누기2
  </pre>
  ```

- 수평 가로 구분선

  ```html
  <p>단락1</p>
  <hr>
  <p>단락2</p>
  <hr>
  <p>단락3</p>
  ```

  

### 서식(Formatting)

---

- 텍스트에 대양한 효과를 준다



- 강조 효과

```html
<p><b>"이 부분"</b>은 단순히 글씨가 굵은 부분이에요!</p>

<p><strong>"이 부분"</strong>은 중요한 부분이라서 굵게 표현됐어요!</p>

<b>태그는 단순히 화면의 텍스트를 굵게 표현해준다.
<strong>태그는 텍스트를 굵게 표현해줄 뿐만 아니라 그 내용이 중요하다는 의미도 함께 포함해준다.
```



```html
<p><i>"이 부분"</i>은 단순히 글씨가 이탤릭체인 부분이에요!</p>

<p><em>"이 부분"</em>은 중요한 부분이라서 이탤릭체로 표현됐어요!</p>

<i>태그는 단순히 화면의 텍스트를 이탤릭체로 표현해준다.
<em>태그는 텍스트를 이탤릭체로 변환해줄 뿐만 아니라 그 내용이 중요하다는 의미도 함께 포함해준다.
```

검색엔진은 strong 태그나 em 태그를 사용하여 강조된 텍스트를 더 중요하게 인식한다.



- 하이라이팅 효과 (mark)

```html
<p><mark>"이 부분"</mark>만 하이라이팅하고 싶어요.</p>
```



- 삭제 효과 (del)

```html
<p><del>"이 부분"</del>을 지운 것처럼 하고 싶어요.</p>
```



- 삽입 효과 (ins)

```html
<p><ins>"밑줄 친 부분"</ins>에 들어갈 알맞은 말을 고르세요.</p>
```



- 위첨자와 아래첨자 효과 (sup, sub)

```html
<p>X<sup>2</sup> + Y<sup>3</sup> = Z</p>

<p>물을 나타내는 화학식은 H<sub>2</sub>O 입니다.</p>
```



### 인용구 (Quotation)

---

1. 짧은 인용구 (q)

   자동으로 앞뒤에 큰따옴표가 붙는다.

```html
<p>HTML의 정의는
<q>웹 페이지를 만들기 위한 하이퍼텍스트 마크업 언어</q>
입니다.</p>
```



2. 블록 인용구 (blockquote)

   인용 부분을 별도의 단락으로 구분하여 나타낸다.

```html
<p>HTML의 정의</p>
<blockquote>
인터넷 서비스의 하나인 월드 와이드 웹을 통해 볼 수 있는 문서를 만들 때 사용하는 프로그래밍 언어의 한 종류이다.
</blockquote>
```



- 축약형 표현 (abbr)

  abbr태그 위에 마우스를 위치시키면 title 속성에 명시한 용어의 원형이 나타남

```html
<p><strong><abbr title="HyperText Markup Language 5">HTML5</abbr></strong>
란 웹 문서를 제작하는 데 쓰이는 프로그래밍 언어인 HTML의 최신규격입니다.</p>
```









### 텍스트 요소

---



| 태그              | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| <a></a>           | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| <b></b>           | 굵은 글씨 요소                                               |
| <strong></strong> | 중요한 강조하고자 하는 요소 (보통 굵은 글씨로 표현)          |
| <i></i>           | 기울임 글씨 요소                                             |
| <em></em>         | 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현)        |
| <br>              | 텍스트 내에 줄 바꿈 생성                                     |
| <img>             | src 속성을 활용하여 이미지 표현,<br />alt 속성을 활용하여 대체 텍스트 |
| <span></span>     | 의미 없는 인라인 컨테이너                                    |



```html
<a></a>		<!-- href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 -->
<b></b>		<!-- 굵은 글씨 요소 -->
<strong></strong>		<!-- 중요한 강조하고자 하는 요소 (보통 굵은 글씨로 표현) -->
<i></i>		<!-- 기울임 글씨 요소 -->
<em></em>		<!-- 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현) -->
<br>		<!-- 텍스트 내에 줄 바꿈 생성 -->
<img>		<!-- src 속성을 활용하여 이미지 표현, alt 속성을 활용하여 대체 텍스트 -->
<span></span>		<!-- 의미 없는 인라인 컨테이너 -->
```



- a 태그

  <a>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</a>

- b 태그

  <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</b>

- strong 태그

  <strong>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</strong>

- i 태그

  <i>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</i>

- em 태그

  <em>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</em>

- span 태그

  <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>



img 요소

src="이미지 파일 경로"

alt="설명" : 대체 텍스트



**alt 용도**

1. 무언가 잘못되어 이미지를 표시할 수 없는 경우
2. 시각 장애가 심한 사용자의 경우 alt 텍스트(대체 텍스트)를 통해 무엇인지 알 수 있음

​	[웹 접근성 경험](https://nax.naver.com/index)





### 그룹 컨텐츠

---

```html
<p></p>  <!-- 하나의 문단 (paragraph) -->
<hr>  <!-- 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule) -->
<ol></ol>  <!-- 순서가 있는 리스트 (ordered) -->
<ul></ul>  <!-- 순서가 없는 리스트 (unordered) -->
<pre></pre>  <!-- HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지 -->
<blockquote></blockquote>  <!-- 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨 -->
<div></div>  <!-- 의미 없는 블록 레벨 컨테이너 -->
```



- p 태그

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

- hr 태그

  <hr></hr>

- ol 태그

  <ol>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</ol>

- ul 태그

  <ul>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</ul>

- pre 태그

  <pre>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</pre>

- blockquote 태그

  <blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</blockquote>

- div 태그

  <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>



[브라우저는 어떻게 동작하는가?](https://d2.naver.com/helloworld/59361)





# CSS 기초

---



- CSS
  - Cascading Style Sheets
  - 문서에 스타일을 지정하기 위한 언어



- CSS 구문

  ```html
  h1 {	# 선택자(Selector)
  	color: blue;	# 선언(Declaration)
  	font-size: 15px;	# 속성(Property) : 값(value)
  }
  ```

  

- CSS 구문은  선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인 (inline)
- 내부 참조(embedding) - < style >
- 외부 참조(link file) - 분리된 CSS 파일



유지보수, 재사용가능성을 늘리기 위해 2번 방법(내부참조)를 사용함



### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 CSS



### CSS 기초 선택자

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - "#" 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



### 우선순위 

id > class > 태그

같은 위치(같은 클래스)라면 나중에 되어있는게 적용



### 요약

HTML : 문서의  구조, 태그

CSS : 스타일링 무엇인가를 선택해서 스타일