branch 관리
- develop/${이름}: 개인 파트 개발 후 해당 브랜치에 커밋하기 위한 브랜치, **develop/team 하위에 각자 자기 브랜치 만들어주세요! ex) develop/gh**
- develop/team: 개인 파트 개발 후 기능/화면 단위로 완성된 것만 해당 브런치에 커밋
- production: dev branch에서 문제 없는 기능만 해당 브런치에 최종 pr, pr생성자 이외의 사람이 확인 후 merge

---

cli 작업이 익숙하지 않으신 분들은 `깃허브 데스크탑` 사용해서 작업해주세요~

✅ 초기 설정
본인 브랜치를 하나 만들어서 해당 브랜치에서만 작업해주세요 :)

✅ 작업을 시작할 때
항상 current branch 가 본인 브랜치인지 확인하고 작업 시작하기!! 꼭!! 본인 브랜치에서 작업해주세요. 만약 다른 브랜치에서 작업을 모르고 시작해버렸다면, 로컬 기기에 파일을 백업해두고 다시 본인 브랜치로 가서 작업합시다.

✅ 머지할 때
머지 과정은 크게 3단계인데요,
(1) 메인에서 변경 내용을 받아와서 내 작업물에 합치고
(2) 합친 작업물을 커밋하고
(3) 메인으로 가서 내가 한 커밋을 머지!
하면 됩니다.

다시말해, 이 프로젝트에서 `develop/${이름}`에서 develop/team에 merge하려면 아래와 같은 순서로 진행하면 돼요.
(1) `develop/team` 브랜치에서 변경 내용을 받아온다(pull).
(2) 에러가 발생하지 않는지 확인하고, 받아온 내용과 작업한 내용을 현재 있는 `develop/${이름}` 브랜치에서 push & commit한다.
(3) commit을 완료하면,`develop/team`에 pull request를 생성한다.

---

깃허브 데스크탑을 사용하시는 분들은 아래를 확인해주세요!
꼭 아래의 단계대로 똑같이 따라해주셔야 에러가 없습니다!!

1. current branch 클릭
2. Choose a branch to merge into ... 클릭
3. main 클릭 -> Create a merge commit 클릭
4. Summary 작성 -> Commit to (본인 브랜치) 클릭 
5. Push origin 클릭
6. current branch 클릭 -> main 브랜치 클릭
7. (메인에서) current branch 클릭 ->  Choose a branch to merge into ... 클릭 
8. 본인 브랜치 클릭 -> Create a merge commit 클릭
9. Push origin 클릭
10. 꼭!! 다시 본인 브랜치로 이동!

✅ 머지 했으면 했다고 카톡방에 알려주기!!
✅ 충돌 났는데 해결 못할 것 같으면 알려주기!!
✅ 동시에 같은 부분 수정하지 않기(동일 파일..동일 코드..날아갈 수 있음)
