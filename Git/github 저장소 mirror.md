# Github 저장소 Mirror

---



>  기존의 환경(branch, commit 이력 등)을 유지하며 옮기는 방법



1. **깃허브 새로운 저장소 생성**

   깃허브 페이지에서 새로운 레포지토리 생성하면 된다.

2. **복사할 저장소 clone**

   복사할 프로젝트 저장소를 clone한다.

   ```bash
   git clone --mirror {복사할 프로젝트 저장소 주소}
   cd {복사한 프로젝트 저장소 이름}
   ```

   

3. **복사한 저장소의 원격 저장소 설정**

   새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정한다.

   ```bash
   git remote set-url --push origin {새롭게 생성한 저장소 주소}
   ```

   

4. **push**

   ```bash
   git push --mirror
   ```

   



오류가 나오는 경우

```bash
error: failed to push some refs to 'github.com:{깃허브 레포}.git'
```

branch를 못가지고 오는 오류이다.

