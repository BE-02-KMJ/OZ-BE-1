let players = {
    boys : {
        Bergkamp : "striker"
    }
}   // 객체 2개, 참조 2개 상태

let persons = players   // reference count +1, garbage collection 참조 x

players = ["Son", "Park"]   // persons는 boys>Bergkamp 객체를 가리키는 유일한 변수, players는 새로운 배열 가리키는 상태

let human = persons.boys    // Bergkamp는 2개의 참조를 가지게 된다.

persons = "persons" // persons는 새로운 문자열 가리키는 상태

human = null    // human도 null로 참조 사라진 상태