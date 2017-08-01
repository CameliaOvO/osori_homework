# 오소리 웹사이트 여름과제
* * *

 7월 초에 계획했던 대로 우린 4주 동안 스터디를 진행했어요!
 (Python+PyCharm, HTML, CSS, JavaScript+jQuery)

 각자의 사정으로 스터디 참여가 힘들었던 분들도 있고, 긴 여름 휴가 때 할 거리도 만들 겸 지금까지 스터디에서 한 내용들을 모두 모아서 간단한 과제로 준비했어요. 기한은 뭐... 딱히 정해진 것은 없지만 중간발표 있는 주 주말까지로 할까요? **(~8/13)** 그 뒤로는 프로젝트도 해야 하니까요. 어차피 프로젝트 하면서 다 하게 될거에요. :sweat_smile:

 그렇게 어마어마하게 어려운 것도 아니고 하찮은 제가 설명을 하는 것보다는 구글의 도움을 받아서 각자 할 수 있는 부분까지 해 보는 걸 추천할게요! 안 어려워요. 진짜에요. 최고잉여인 제가 만들었거든요(...)

 :octocat: **각각의 소과제를 끝낸 뒤에는 커밋을 잊지 말아주세요!** 아마 여름과제를 포기하지 않고 한다면 최소 10개 이상의 커밋이 나올 거 같아요. 각 주차 스터디에 참석하셨던 분들은 굳이 하실 필요 없이 모여서 만들었던 레포 그대로 깃헙에 올리시면 돼요!*

 맨바닥에서부터 짜는 건 비효율적이기도 하고 막막하니까 5월 5일의 결과물(!)을 리스폰해왔어요. 사실 거기서 한 것과 조금 다르긴 하지만 어린이날에 봤던 튜토리얼을 보면서 한다면 이해하는데 어렵지는 않을거에요.



* * *
과제를 수행하기 전
# Django 업데이트 1.11로 꼭 해주세요!!! (pip3 install -U django)


### 1주차 : Pycharm + Python
 다들 잘 쓰고있는 IDE가 있을테니 Pycharm 부분은 생략할게요! (설마 아직도 python을 vim으로 코딩하는 분이 있는건 아니죠?) 없다면 Pycharm이나 Sublime같은 것을 추천할게요. 저번 학기에 써봤는데 Atom도 쓸만하더라고요. ~~할 줄 아는것도 없는 주제에 IDE만 신나게 바꿔서 그래요~~

 1. index.html 연결하기
 template/board에 들어가면 index.html이 있어요. 딱 봐도 제일 첫페이지처럼 생겼죠? 지금은 시작하면 바로 test_board.html을 출력하는데 시작하면 index.html을 출력하도록 하고 test_board.html은 127.0.0.1:8000/test_board로 들어갔을 때 출력하도록 해주세요.

 2. 자기가 쓴 글만 수정 혹은 삭제할 수 있게 만들기
 지금은 로그인 사용자면 다른 사람이 쓴 글도 수정 혹은 삭제를 할 수 있어요. (여러분이 쓴 글을 제가 수정할 수 있다면 정상은 아니죠) 이제 user를 확인해서 자기가 쓴 글만 수정하고 삭제할 수 있도록 해주세요.

 3. 글 조회수 확인 구현하기
 board/models.py를 보면 Article모델에 view_count라는 속성이 있다는 것을 확인할 수 있어요. 말 그대로 조회수를 생각하고 만들어놓은 속성인데 아직 구현이 안 돼 있어요.글을 한 번 읽을 때마다 조회수가 1씩 증가하게 만들어 주세요.

### 2주차 : HTML
 아마 1주차에 이어 가장 쉬운 부분이에요. HTML과 함께 Django의 템플릿을 어떻게 쓰는가도 **조금** 들어있어요. 어렵지 않게 해결할 수 있을거에요.

 1. test_board를 테이블 형태로 고치기
 지금은 우리가 생각하는 '게시판'스러운 형태라기에는 조금 그렇죠? 우리가 평소 공지사항 게시판에서 보는 것처럼 [글번호, 제목, 작성일자, 조회수, 덧글 수]를 한 row에 표현하는 테이블로 만들어주세요. 예시라면 [이곳](http://cs.hanyang.ac.kr/board/info_board.php)이 좋은 예시가 되겠죠?
 ![테이블 예시 이미지](/img/board.PNG)
꼭 이렇게 정확하게 할 필요는 없어요! 이건 그냥 예시에요! CSS는 다음 과제에서 쓸 거에요!

 2. 게시판 페이징 구현
 지금 형태의 게시판에 100개가 넘는 게시글이 올라온다면 어떤 일이 벌어질까요? 스크롤이 상당히 끔찍하겠죠? 게시판 페이징을 구현해 봐요. 다행히도 django에는 pagination을 위한 class가 있어요. [참고](https://docs.djangoproject.com/en/1.11/topics/pagination/)

 3. article_detail을 수정하기
 게시판을 테이블 형식으로 바꿨는데 글 내용 페이지가 그대로니까 약간 어색하죠? article_detail도 수정해봐요. 일단 테이블 형태로 바꿔봐야겠죠?
![게시판 예시 이미지](/img/detail.PNG)
마찬가지로 이것도 예시! (이전글 다음글이 추가됐죠?) CSS는 다음 과제에서 고칠 거에요.
그리고 댓글을 입력하려다 보면 알텐데 댓글을 입력하는 것도 새로운 창으로 이동해서 입력하게 되어있어요. 이걸 article_detail.html 내에서 해결하도록 바꿔봐요!

### 3주차 : CSS 
우린 디자이너가 아니에요... 하지만 그래도 사람다운 디자인은 만들어야겠죠?
1. 상단 네비게이션 메뉴를 가로로 만들기
 지금은 상단 네비게이션 메뉴가 세로로 서 있어요! (동아리 소개, 프로젝트 팀 내역, 게시판, 사진첩) 이거요. 이걸 가로로 눕혀봐요! 아마 이게 가장 쉬울거에요.

2. test_board 페이지를 3분할 페이지로
 우리는 게시판이 네 종류가 있을 거에요. 자유게시판, 공지게시판, Q&A 게시판, 정보게시판. 지금은 이 메뉴들이 글이나 게시판의 위에 있어요. 이걸 게시판 혹은 글의 왼쪽으로 옮겨주세요! float을 이용하면 간단할 거에요. 마찬가지로 위의 동문열, 로그인 로그아웃, 아래의 카피라이트 같은것도 적절한 위치로 옮겨주세요. 아! 카피라이트는 페이지의 아래 가운데에 보이게 해주세요!

3. article_table과 article_detail을 꾸미기
 자 여러분의 미적 감각을 시험해 볼 차례에요! 위에 예시 이미지들 보면 예...쁘지는 않지만 그래도 깔끔하지 않나요? 저런 식으로 만들어 봐요! 더 예쁘게 만들 자신이 있다 하면 하고싶은대로 꾸며봐요! 아마 오소리 웹사이트 팀의 수석디자이너가 되지 않을까요? :satisfied:

### 4주차 : javascript+jQuery
1. 상단 네비게이션 메뉴를 드롭다운으로 바꾸기
상단 네비게이션 메뉴를 드롭다운 메뉴로 바꿔봐요! 더 추가되어야 할 부분은 프로젝트 팀 내역의 하단 메뉴로 [진행중인 프로젝트, 완료된 프로젝트], 게시판의 하위 메뉴로 [공지게시판, 자유게시판, 정보게시판, Q&A게시판]을 추가해 주세요. 아 드롭다운 메뉴는 다들 아시죠? [이거에요](https://www.google.co.kr/search?q=drop+down+navigation+bar&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjsyI62s6vVAhUE2mMKHWLlDjcQ_AUICigB&biw=1150&bih=861&dpr=1.1)
 먼저 했던 팀원분이 jQuery를 쓰는 것을 강력하게 추천했어요!

2. 동문열 옆의 현재 시간이 제대로 작동하게 만들기
동문열 옆에 왜 있는지 모르겠던 현재시간! 오전 00:00:00이라고 하는 저걸 저거 진짜 현재시간을 보여주도록 만들어주세요! 새로고침하지 않아도 시간이 계속 움직여야 돼요!

3. index.html에 이미지 슬라이드 추가하기
Django에서 홈페이지에 이미지를 추가하는 건 아직 안해봤죠?? 
완성 예시는 <a href="http://cs.hanyang.ac.kr" target="_blank">cs.hanyang.ac.kr</a>의 슬라이드를 참고해주세요!