/*
1. 견종 사진 42장 받기 https://dog.ceo/api/breeds/image/random/42
2. 견종 이름 받기 https://dog.ceo/api/breeds/list/all 
(key값으로 저장되어 있어 key값 읽는 걸로 코드 작성 필요.)
*/

// 요소 선택 및 배열 선언 -0
const apirandomDogs = "https://dog.ceo/api/breeds/image/random/42"
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all"
const request1 = new XMLHttpRequest()
const request2 = new XMLHttpRequest()
const request3 = new XMLHttpRequest()   // MORE 버튼을 위한 요소

const header = document.getElementById("header")
const main = document.getElementById("main")
const input = document.getElementById("filter-text")
const button = document.getElementById("filter-button")
const select = document.getElementById("filter-select")

const currentDog = []   // 현재 화면에 나와있는 강아지 사진들 배열 형태로 관리

// 부가 기능 버튼들 요소 선택 -5
const more = document.getElementById("more")
const tothetop = document.getElementById("tothetop")
const reset = document.getElementById("reset")


// forEach 코드 함수로 바꾸기 -4
/*
요소명.forEach(function(item){    
    const dogImgDiv = document.createElement("div")
    dogImgDiv.classList.add("flex-item")
    dogImgDiv.innerHTML = `<img src=${item}>`
    main.appendChild(dogImgDiv)
});
*/
function displayDogs(item){
    const dogImgDiv = document.createElement("div")
    dogImgDiv.classList.add("flex-item")
    dogImgDiv.innerHTML = `<img src=${item}>`
    main.appendChild(dogImgDiv)
}


// 처음 웹 페이지 열었을 때 실행될 동작 -1
window.addEventListener("load", function(){
    // 강아지 사진 서버에서 받아와 뿌리기.
    request1.open("get", apirandomDogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)  // 42개의 강아지 이미지 주소 JSON에서 객체로 받기.
        response.message.forEach(function(item){    // 받은 강아지 이미지 뿌리기
            currentDog.push(item)
            displayDogs(item)
        });
    })
    request1.send()

    // 견종 정보 뿌리기
    request2.open("get",apiAllBreeds)
    request2.addEventListener("load", function(){
        const response = JSON.parse(request2.response)
        Object.keys(response.message).forEach(function(item){   // 견종 정보 key값 읽기
            const option = document.createElement("option")
            option.textContent = item
            option.value = item
            select.appendChild(option)
        })
    })
    request2.send()
})

// Filter 버튼 누르면 입력창 값 토대로 필터링 작동 -2
button.addEventListener("click", function(){
    main.innerHTML = ""
    let filteredDogs = currentDog.filter(function(item){
        return item.indexOf(input.value) !== -1;
    })  // 문자열로된 견종 정보안에 input에 쓰여진 내용이 포함되어 있으면 filtering.

    input.value = ""    // Filter 버튼 클릭시 입력창 내용 사라지기
    // 사라진 입력창에 Filter 버튼 누르면 value 값이 0이 되어 전체 보이게 됨.

    // 필터링 된 자료들만 가지고 새로 구성
    filteredDogs.forEach(function(item){
        displayDogs(item)
    });
})

// Select 선택하면 선택값 견종만 보는 기능 작동 -3
select.addEventListener("change", function(){
    // 위와 동일 기능
    main.innerHTML = ""
    let filteredDogs = currentDog.filter(function(item){
        return item.indexOf(select.value) !== -1;
    })
    // select에서는 value로 0을 미리 넣어놨기 때문에 all 선택시 전체 보이게 됨.

    filteredDogs.forEach(function(item){
        displayDogs(item)
    });
})

// MORE 버튼 기능 작동 -6
more.addEventListener("click", function(){
    request3.open("get", apirandomDogs)
    request3.addEventListener("load", function(){   // 처음 사진 받기와 동일. 요소명 주의
        const response = JSON.parse(request3.response)
        response.message.forEach(function(item){
            currentDog.push(item)
            displayDogs(item)
        });
    })
    request3.send()
})

// TOP 버튼 기능 작동 -7
tothetop.addEventListener("click", function(){
    window.scrollTo({top: 0})
})

// (추가) Reset 버튼 기능 작동 -8
reset.addEventListener("click", function(){
    main.innerHTML = ""
    request1.open("get", apirandomDogs)
    request1.addEventListener("load", function(){
        currentDog = []
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){ 
            currentDog.push(item)
            displayDogs(item)
        });
    })
    request1.send()
})