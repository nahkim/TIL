```python
with open("./data/fruits.txt", "r", encoding="utf-8") as f:
    str = f.read()
    res = {}
    fruit_list = str.split("\n")
```

```python
f = open(...)
str = f.read()
res = {}
fruit_list = str.split("\n")
f.close()
```

같은 코드로 첫번째 코드의 경우 들여쓰기 때문에 코드블럭으로 보여서

첫번째 코드 안의 변수가 지역변수 같을 수 있으나

첫번째 코드를 풀면 두번째 코드가 되므로 코드블럭으로 묶여있지않다.