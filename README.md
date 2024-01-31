# 20팀 Cheers (임수경, 변규탁)

### 🥂 칵테일 레시피와 상품소개하는 서비스

#### 웹 프레임워크 Django와 HTML/CSS/JS를 활용한 콘텐츠 기반 커뮤니티 웹 플랫폼 개발

* 프로젝트 기간 : 2022-11-16 ~ 2022-11-21

---

### 1. ERD
![image](https://github.com/oiosu/Cheers/assets/99783474/e58542b0-f7f0-4458-90b5-1b4ee416f77d)


### 2. Figma
![image](https://github.com/oiosu/Cheers/assets/99783474/3f2ff4a7-b450-4d9c-a572-8de2bba6fc6b)


### 3. 상품 디테일 페이지 
![image](https://github.com/oiosu/Cheers/assets/99783474/5922f759-cd8a-41aa-9abb-095fa360c528)


### 4. 칵테일 레시피 디테일 페이지 
![image](https://github.com/oiosu/Cheers/assets/99783474/a0009e8b-82a7-429e-9b5b-795606c51898)


### 5. 사용자들을 위한 칵테일 레시피 디테일 페이지 
![image](https://github.com/oiosu/Cheers/assets/99783474/89d7ec76-9046-4653-a715-c0babdc1aa0c)

---

### ⭐ 프론트엔드 구현 JavaScript

1. **위, 아래 스크롤 시 일정 값 이상 보다 커지면 요소를 화면에서 사라지도록 하기** 
- window : 브라우저에 나타나나는 하나의 탭을 의미한다.
- window 객체는 브라우저가 가지고 있는 여러가지 명령들을 가지고 있다.
- `addEventListener(scoroll, 함수)`
    - `addEventListener`라는 메소드는 첫번째 이벤트 scroll이 되면 두번째 익명의 함수를 실행하라는 뜻이다.
- `lodash.js` 활용하기
    - `lodash`가 지원하는 메소드 중 `_.throttle메소드`를 활용하여 스크롤시 일정 시간에 한번씩만 실행되도록 제한을 걸어두기 위해 사용한다.
    - `_.throttle`는 특히 스크롤 작업을 할 때 굉장히 많이 사용되는 기능 중에 하나이다.
    - `_.throttle`(우리가 사용하고자 하는 함수, 그 함수가 몇초로 실행하면 되는지 시간을 적어준다(밀리세컨드 단위로!)
- 스크롤시 부드럽게 사라지고 나타날 수 있도록 `GSAP`를 활용했다.
- `gsap`이라는 자바스크립트 애니메이션을 처리해주는 라이브러리에서 to 라는 메소드를 통해 요소와 지속시간, 여러가지 옵션을 명시합니다. 그 옵션 중에는 css 속성과 값을 입력할 수 있다.

2. **하나씩 시간차에 나타날 수 있도록 하기** 
- document 객체에 `querySelectorAll`이라는 메소드 실행
- `fadeELs.forEach` : HTML 부분에서 찾은 fade-in 요소들의 갯수만큼 `forEach메소드`에 인수로 적은 함수를 실행할 수 있도록 한다.
- `GSAP` 활용하여 지속시간을 설정했다.
- 순차적으로 나타나기 delay : 지연시간을 활용 > (index + 1) * .7 : 곱해주기


---

### 반복되는 수정작업, 결국 사용자들에게 어떤 서비스인지 보여주기 위한 노력/요구사항 정리 
![image](https://github.com/oiosu/Cheers/assets/99783474/a4aa5f81-8f80-4caa-a47f-8eaa59ce4855)

![image](https://github.com/oiosu/Cheers/assets/99783474/8b86dec7-10db-4ac4-936d-071eddfde441)

![image](https://github.com/oiosu/Cheers/assets/99783474/342c25ae-4b7c-4a8e-9dab-e159c1282f15)

![image](https://github.com/oiosu/Cheers/assets/99783474/69ebc14b-58bf-4955-a6f2-0f286942af20)


---

### 좋은 점만 가져올 수 있도록!

> 벤치마킹하면서 분석한 것들

![image](https://github.com/oiosu/Cheers/assets/99783474/aa607684-9f99-4ab8-9bf5-c5e76ec1d880)

![image](https://github.com/oiosu/Cheers/assets/99783474/1df5e62f-1bed-45a0-a842-b13e823670e0)


---

### 오픈 그래프 카드와 트위터 카드 

![image](https://github.com/oiosu/Cheers/assets/99783474/17bfab0d-97fe-41d1-a6b6-ca4c9c46304e)


##### * 오픈그래프 프로토콜 : 어떠한 인터넷 웹 사이트의 HTML  문서에서 head -> meta 태그 중 "og:XXX"가 있는 태그들을 찾아내어 보여주는 프로토콜이다.

##### ◾ 특징 : 만약 웹 사이트가 오픈 그래프 프로토콜을 지원한다면, 웹 사이트에 들어가기도 저에 뭐하는 사이트인지 알 수 있다. 


---

### Share 

해당 SHARE 할 수 있는 소셜을 아이콘으로 배치를 해왔다면, 쉽게 할 수 있는 방법으로 이번 프로젝트때 활용 할 수 있었습니다.  사이트를 통해 모양과 소셜 종류를 직접 선택할 수 있습니다. 
![image](https://github.com/oiosu/Cheers/assets/99783474/41693c45-4ab7-4a9c-bcfd-b91e4d11fe8c)


---

### UI/UX 어렵게 느껴질 때는 ‘토픽’을 활용하여 사용자들의 보기에 편한 동그라미 형태를 결정함 

![image](https://github.com/oiosu/Cheers/assets/99783474/13ace397-f31b-452c-8dd9-e97bed7ebfd0)

![image](https://github.com/oiosu/Cheers/assets/99783474/49d9826f-0639-48a0-b619-c75e09dc3162)




