# Git을 활용한 버전 관리

------

> git

분산 버전 관리 시스템(DVCS)

컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율

## 버전 관리 기본

------

> 버전

컴퓨터 소프트웨어의 특성 상태

> 기본 흐름

1. 작업하면 2) add하여 Staging area에 모아 3) commit으로 버전 기록

📑 → add → 🗂️ → commit → 🗄️



📑 작업(수정)한 파일 Working directory(파일의 변경사항)

🗂️ 커밋할 목록 INDEX(staging area) (버전으로 기록하기 위한 파일 변경사항의 목록)

🗄️ 버전 HEAD (커밋(버전)들이 기록되는 곳)

Git은 파일을 modified, staged, committed로 관리

> staging area(중간 과정)가 필요한 이유

여러 파일이 있을 경우 특정 파일만 버전을 기록하기 위해서

버전 기록 파일들을 모으기 위한 임시공간

소스코드를 수정하고 신규 기능을 개발하였을 때 스테이징 서버에 반영하여 임시적으로 테스트할 수 있음



a.txt ⇒ add ⇒ a.txt ⇒ commit ⇒ v1, v2, v3…

1통 (working directory)

2통 임시 공간 (staging area)

3통 커밋 (repository)

1통, 2통 확인 : git status

3통 확인 : git log

------

| git init                     | 로컬 저장소 생성                                     |
| ---------------------------- | ---------------------------------------------------- |
| git add <file>               | 특정 파일/폴더의 변경사항 추가                       |
| git status                   | Git 저장소에 있는 파일의 상태를 확인하기 위해 사용   |
| git log                      | 현재 저장소에 기록된 커밋을 조회 $ git log --oneline |
| git commit -m ‘<커밋메세지>’ | 커밋 (버전 기록)                                     |
| git push                     | 원격저장소                                           |
| git pull                     | 원격 저장소로부터 변경된 내역 받아옴                 |

1. 보고서 파일을 새로 만듬 ⇒ untracked (빨강) Working directory
2. 보고서 파일 add ⇒ staged (초록)
3. commit ⇒ unmodified
4. 보고서 수정 ⇒ modified (빨강)

## Git branch

------

> 빈폴더를 만들고 싶을 때

1. 빈 폴더는 status에 나타나지 않는다.
2. 일반적으로 .gitkeep이라고 하는 파일 생성

.gitkeep : 비어있는 폴더를 만들고 싶을때 관용적으로 그 폴더 안에 저 파일을 넣음

> 원격저장소 경로 설정 (push 전에 해줘야함)

```
$ git remote add origin URL
// 깃에 원격저장소를 origin이라는 이름으로 URL을 추가
```

> 원격저장소 정보 확인

```
$ git remote -v
```

> 원격 저장소를 로컬 저장소 변경사항(commit)을 올림(push)

```
$ git push
```

> git push시 원격저장소에서 한 작업이 로컬에는 없을때(엉켰을때)

```
git log --oneline
git log --oneline --graph
```