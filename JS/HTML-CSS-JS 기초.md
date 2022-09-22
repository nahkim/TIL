# HTML / CSS / JS 기초

---





## HTML

---

- Hyper Text Markup Language의 줄임말
- HTML의 요소(Element)는 여는 태그와 닫는 태그로 이루어져 있다.
- 웹 사이트에서 구조화를 담당한다.



### head 태그

---

- 일반적으로 문서 제목, 문자 인코딩 등의 문서 정보를 담고 있음
- meta 태그를 이용하여 웹 문서에 대한 추가정보를 선언함
- 브라우저에 내용이 나타나지 않음



### Form 태그

---

- 웹 페이지에서 입력 양식
- 사용자의 정보를 입력 받기 위해 사용



### 시맨틱(Semantic) 태그

---

- 태그 중 특정 목적, 역할 및 의미적 가치를 가지는 태그
- 코드의 가독성을 높이고 유지보수를 쉽게하기 위해 사용
- ex) header 태그



## CSS

---

- Cascading Style Sheets의 줄임말
- CSS는 웹 사이트에서 표현을 담당
- CSS는 인라인, 내부참조, 외부참조 세가지 방법으로 정의 가능



### CSS 선택자 우선순위

---

!important > inline style > id > class > tag





#### 배치

---



![문제8](HTML-CSS-JS 기초.assets/문제8.png)

 

그림의 justify-content 속성의 값 : space-between



### sticky

---

- top, bottom, left, right 중 하나를 필수로 설정해야한다.
- 특정 영역에 도달하기 전까지는 static 속성처럼 작동하지만 설정된 위치에 도달하면 fixed 속성처럼 작동한다.



![문제 10](HTML-CSS-JS 기초.assets/문제10.png)

```html
<div class="row">
  <div class="col-3">
    1
  </div>
  <div class="col-9">
    <div class="row">
      <div class="col-4">
        2
      </div>
      <div class="col-4">
        3
      </div>
      <div class="col-4">
        4
      </div>
    </div>
  </div>
</div>
```





## JavaScript

---

- JS는 웹 사이트에서 동작을 담당
- 브라우저를 조작할 수 있는 유일한 언어이다.
- JS의 == 연산자는 값만 같으면 참(True)를 반환함



#### JavaScript의 변수 선언 키워드

- var
- let
- const



#### JavaScript의 원시 타입

- undefined
- String
- Number



### DOM

---

#### 메서드

- document.getElementById()
  - 아이디를 인자로 받으며, 일치하는 id를 가진 요소를 반환
- document.querySelector()
  - 
- document.querySelectorAll()
  - 선택자를 인자로 받으며, 일치하는 모든 요소를 반환
- document.createElement()
  - 태그이름을 인자로 받으며, 지정한 이름의 요소를 만들어 반환
- document.addEventListener()
  - 
- filter
  - 배열 메서드 중 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

