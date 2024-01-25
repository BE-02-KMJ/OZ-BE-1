const todaySpan = document.querySelector("#today")
const numbersDiv = document.querySelector('.numbers')
const drawButton = document.querySelector('#draw')
const resetButton = document.querySelector('#reset')

let lottoNumbers = []
const colors = ['gold', 'blue', 'red', 'gray', 'green']

function paintNumber(number){
    const eachNumDiv = document.createElement('div')
    eachNumDiv.classList.add('eachnum')
    eachNumDiv.textContent = number
    numbersDiv.appendChild(eachNumDiv)
    let colorIndex = Math.floor(number / 10)
    eachNumDiv.style.backgroundColor = colors[colorIndex]
}

drawButton.addEventListener("click", function(){
    // 추첨 번호 다시 눌러도 다른 번호들로 추첨될 수 있도록 함.
    lottoNumbers = [];
    numbersDiv.innerHTML = ""
    
    while(lottoNumbers.length < 6){ // 6개만 뽑을 거다.
        let rn = Math.floor(Math.random() * 45) + 1

        if(lottoNumbers.indexOf(rn) === -1){    // 같은 번호 추첨 안되게 뽑을 거다.
          lottoNumbers.push(rn)
          paintNumber(rn)
        }
    }
})

resetButton.addEventListener('click', function(){
    lottoNumbers.splice(0, 6)
    numbersDiv.innerHTML = ""
})

// 로또 번호 추첨 앞에 날짜 추가
const today = new Date()

let year = today.getFullYear()
let month = today.getMonth() + 1
let date = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `