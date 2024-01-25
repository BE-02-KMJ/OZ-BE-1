// 요소 선택 및 배열 선언 -0
const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
let todoArr = [];

// 데이터 로컬 저장소에 저장하기 -5
function saveTodos(){
    const todoString = JSON.stringify(todoArr)
    localStorage.setItem('myTodos', todoString)
}

// 로컬 저장소에 저장된 데이터 가져오기 -6
function loadTodos(){
    const myTodos = localStorage.getItem('myTodos') 
    if(myTodos !== null) {
        todoArr = JSON.parse(myTodos)
        displayTodos()
    }
}

// 할 일 삭제 버튼 구현 -4
function handleTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
      return aTodo.todoId !== clickedId
    })
    displayTodos()
    saveTodos() // -5
}

// 할 일을 클릭 구현 -3
function handleTodoItemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){
        if(aTodo.todoId === clickedId){
            return {
                ...aTodo, todoDone: !aTodo.todoDone 
            } // 그 할 일의 id를 받아서 해당 class만 수정 기존 내용 가져오고 반대 내용 덮어쓰기. 
        } else {
            return aTodo
        }
    })
    displayTodos()
    saveTodos() // -5
  }

// 할 일 보여주기 -2
function displayTodos(){
    todoList.innerHTML = "" // 앞에 누적해서 추가하지 않도록 하기.
    todoArr.forEach(function(aTodo) {
      const todoItem = document.createElement('li')
      const todoDelBtn = document.createElement('span') // 삭제 버튼 생성.
      todoDelBtn.textContent = 'x'
      todoItem.textContent = aTodo.todoText
      todoItem.title = '클릭하면 완료!'
      todoDelBtn.title = '클릭하면 삭제x'
    
      // 완료되면 색 변하게 하는 기능을 위해 class 추가
      if(aTodo.todoDone){
        todoItem.classList.add("done")
      } else {
        todoItem.classList.add("yet")
      }
      // todoItem.classList.add(aTodo.todoDone ? 'done' : 'yet') 와 동일.

      todoItem.addEventListener('click', function(){    // -3
        handleTodoItemClick(aTodo.todoId)
      })
      todoDelBtn.addEventListener('click', function(){  // -4
        handleTodoDelBtnClick(aTodo.todoId)
      })
      
      todoItem.appendChild(todoDelBtn)
      todoList.appendChild(todoItem)
    });
}

// 할 일 추가하기 -1
todoForm.addEventListener('submit', function(e){
    e.preventDefault()  // 기존 기능 차단
    const toBeAdded = {
      todoText: todoForm.todo.value,
      todoId: new Date().getTime(), // 할 일에 대한 고유번호 부여.
      todoDone: false   // 미완료 상태
    }
    todoForm.todo.value = ""    // 할 일 적는 칸 추가 누른 후 비우기
    todoArr.push(toBeAdded) // 할 일 목록에 추가
    displayTodos()
    saveTodos()     // -5
})

loadTodos() // 시작할 때 한번만 데이터 가져오기. -6