# CSS Layout 실습 정리

---

CSS layout 기술 중 Flexbox

[Flexbox Froggy](https://flexboxfroggy.com/#ko)



- justify-content 속성
  - 인자
  - flex-start : 요소들을 컨테이너의 왼쪽으로 정렬
  - flex-end : 요소들을 컨테이너의 오른쪽으로 정렬
  - center : 요소들을 컨테이너의 가운데로 정렬
  - space-between : 요소들 사이에 동일한 간격을 둠
  - space-around : 요소들 주위에 동일한 간격을 둠



```css
#pond {
  display: flex;
  justify-content: flex-end;
}
```



- align-items 속성
  - 인자
  - flex-start : 요소들을 컨테이너의 꼭대기로 정렬
  - flex-end : 요소들을 컨테이너의 바닥으로 정렬
  - center : 요소들을 컨테이너의 세로선 상의 가운데로 정렬
  - baseline : 요소들을 컨테이너의 시작 위치에 정렬
  - stretch : 요소들을 컨테이너에 맞도록 늘림



- align-self 속성
  - 개별 요소에 적용할 수 있는 또 다른 속성
  - align-items가 사용하는 값들을 인자로 받음



```css
#pond {
  display: flex;
  align-items: flex-end;
}

.yellow {
  align-self: flex-end;
}
```



- flex-direction 속성
  - 인자
  - row : 요소들을 텍스트의 방향과 동일하게 정렬
  - row-reverse : 요소들을 텍스트의 반대 방향으로 정렬
  - column : 요소들을 위에서 아래로 정렬
  - column-reverse : 요소들을 아래에서 위로 정렬



```css
#pond {
  display: flex;
  flex-direction: row-reverse;
}
```

**column-reverse 또는 row-reverse를 사용하면 요소들의 start와 end의 순서도 뒤바뀐다!**



```css
#pond {
  display: flex;
  flex-direction: column-reverse;
  justify-content: flex-end;
}
```

**Flex의 방향이 column일 경우 justify-content의 방향이 세로로, align-items의 방향이 가로로 바뀐다!**



- order 속성
  - 기본값 0
  - 양수 (오른쪽으로 이동)
  - 음수 (왼쪽으로 이동)

```css
.red {
  order: -1
}
```



- flex-wrap 속성
  - 인자
  - nowrap : 모든 요소들을 한 줄에 정렬
  - wrap : 요소들을 여러 줄에 걸쳐 정렬
  - wrap-reverse : 요소들을 여러 줄에 걸쳐 반대로 정렬

```css
#pond {
  display: flex;
  flex-wrap: wrap;
}
```



- flex-flow 속성
  - flex-direction과 flex-wrap를 대신한다.

```css
요소들을 가로선 상의 여러줄에 걸쳐 정렬하기 위해
flex-flow: row wrap

ex)
#pond {
  display: flex;
  flex-direction: column-reverse;
  flex-wrap: wrap;
}

#pond {
  display: flex;
  flex-flow: column-reverse wrap;
}
```



- align-content
  - flex-start : 여러 줄들을 컨테이너의 꼭대기에 정렬
  - flex-end : 여러 줄들을 컨테이너의 바닥에 정렬
  - center : 여러 줄들을 세로선 상의 가운데에 정렬
  - space-between : 여러 줄들 사이에 동일한 간격을 둠
  - space-around : 여러 줄들 주위에 동일한 간격을 둠
  - stretch : 여러 줄들을 컨테이너에 맞도록 늘림

**align-content는 여러 줄들 사이의 간격을 지정하며, align-items는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정, 한줄만 있는 경우 align-content는 효과를 보이지 않음**

```css
#pond {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
}
```



```css
#pond {
  flex-flow: wrap-reverse column-reverse;
	justify-content: center;
	align-content: space-between;
}
```

