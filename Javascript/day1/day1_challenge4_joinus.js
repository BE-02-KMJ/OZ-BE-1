document.getElementById('form').onsubmit = function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email')
    const pw = document.getElementById('pw_check')
    const name = document.getElementById('name')
    const number = document.getElementById('phone1','phone2','phone3')
    const region = document.getElementById('region')
    const sex = document.getElementsByClassName('sex')

    console.log(email.value)
    console.log(pw.value)
    console.log(name.value)
    console.log(number.value)
    console.log(region.value)
    console.log(sex.value)

    alert(`${name}님 가입을 환영합니다~!`)
}