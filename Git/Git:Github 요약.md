# Git/Github 정리



- **Git은 무엇인가**

  - 분산버전관리시스템

    

- **Staging Area (임시공간)이 의미하는 것은?**

  - 

  

- **작업이 완료 되었을 때, 버전을 기록하는 과정을 명령어로 작성하고, 커밋이 가지는 의미가 무엇인지**

  ```
  $ git add
  $ git status
  $ git commit -m “메세지”
  
  커밋은 로컬 내에 버전을 남기는 것을 의미한다.
  ```

  

- **.gitignore를 활용하는 이유**

  - 

  

- **커밋 내역을 확인하는 명령어는 $ git ____ 이다.**

  - log

    

- **원격저장소를 제공하는 서비스는 GitHub 이외에도 있다.**

  - O

    

![Untitled](Git:Github 요약.assets/Untitled.png)

- **위의 이미지의 오류의 원인과 해결 방안은?**

  - 원인 : 원격 저장소와 로컬 저장소의 버전이 달라서 나는 오류

  ```
  // 해결 방안
  $ git pull origin mater
  $ git push
  ```

  

- **원격저장소(https://github.com/nahkim/TIL.git)를 복제하기 위한 명령어**

  ```
  git clone <https://github.com/nahkim/TIL.git>
  ```

  

- **브랜치를 사용하는 목적은 무엇인지**

  - 독립적인 작업의 흐름을 만들기 위해

  

- **merge conflict가 발생하였을 때 해야 하는 일**

  

- **GitHub에서 1) Shared Repository와 2) Fork & Pull Request의 차이점**

  - 저장소 권한의 유무