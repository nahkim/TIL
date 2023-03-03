### PDU (Protocol Data Unit)

---

네트워크의 어떠한 계층에서 계층으로 데이터가 전달될 때 하나의 단위



**PDU 구성**

헤더와 페이로드로 구성되며, 각 계층마다 부르는 명칭이 다름

- 헤더
  - 제어 관련 정보들 포함
- 페이로드
  - 데이터



- **애플리케이션 계층**: 메시지
- **전송 계층**: 세그먼트(TCP), 데이터그램(UDP)
- **인터넷 계층**: 패킷
- **링크 계층**: 프레임(데이터 링크 계층), 비트(물리 계층)



ex) 애플리케이션 계층은 ‘메시지’를 기반으로 데이터를 전달하는데, HTTP의 헤더가 문자열인 것

curl 명령어를 이용하여 www.naver.com으로 HTTP 요청을 해서 PDU 테스팅 하기

- curl 테스팅 사이트 링크: **https://reqbin.com/curl**

![img](https://blog.kakaocdn.net/dn/cZBUgh/btr1KPjU1wt/kqw01JmXicEXCnvGU0QWu1/img.png)



"curl [www.naver.com](http://www.naver.com/)" 명령어를 통해 요청하면 응답(response) 헤더 값이 나오는데 모두 문자열이다.

PDU 중 아래 계층인 비트로 송수신하는 것이 모든 PDU 중 가장 빠르고 효율성이 높다.

그러나 애플리케이션 계층에서는 문자열을 기반으로 송수신을 한다. → 헤더에 authorization 값 등 다른 값들을 넣는 확장이 쉽기 때문!





참고 : [**면접을 위한 CS 전공지식 노트**](https://search.shopping.naver.com/book/catalog/32478035848?cat_id=50010920&frm=PBOKPRO&query=cs+면접&NaPm=ct%3Dlek2tw0w|ci%3D5f7c24f8231a09f6e7d9e1f2a16abb311f84205d|tr%3Dboknx|sn%3D95694|hk%3D81f9b580de8803af9d189a29d0e29135be6f780b)