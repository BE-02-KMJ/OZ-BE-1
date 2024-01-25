const form = document.getElementById("form")

// 제출 이벤트를 받는다. → 이벤트 핸들링
form.addEventListener("submit", function(e){
    e.preventDefault(); // 제출 눌렀을시 새로고침 되는 것 삭제.

    // 제출된 입력 값들을 참조한다.
    let userId = e.target.id.value
    let userPw1 = e.target.pw1.value
    let userPw2 = e.target.pw2.value
    let userName = e.target.name.value
    let userPhone = e.target.phone.value
    let userPosition = e.target.position.value
    let userGender = e.target.gender.value
    let userEmail = e.target.email.value
    let userIntro = e.target.intro.value

    console.log(userId)
    console.log(userPw1)
    console.log(userPw2)
    console.log(userName)
    console.log(userPhone)
    console.log(userPosition)
    console.log(userGender)
    console.log(userEmail)
    console.log(userIntro)

    // 입력값에 문제가 있는 경우 이를 감지한다.
    // 1. 아이디가 짧은 경우
    // 2. 비밀번호와 비밀번호 확인이 일치하지 않는 경우
    if(userId.length < 6){
        alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
        return;
    }

    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return;
    }

    // 가입 환영 인사를 제공한다.
    document.body.innerHTML = ""    // 아예 새로운 html 코드를 대입하겠다. (빈페이지)
    document.write(`<p>${userId}님 환영합니다.</p>`)
    document.write(`<p>※ 회원 가입 시 입력하신 내역은 다음과 같습니다.</p>`)
    document.write(`<p> ⊙ 아이디 : ${userId}</p>`)
    document.write(`<p> ⊙ 이름 : ${userName}</p>`)
    document.write(`<p> ⊙ 전화번호 : ${userPhone}</p>`)
    document.write(`<p> ⊙ 원하는 직무 : ${userPosition}</p>`)
})