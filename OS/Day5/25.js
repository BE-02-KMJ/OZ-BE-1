const fs = require("fs")

fs.readFile("number1.txt", "utf8", (err, data) => { // callback function
    if(err){
        console.log("파일을 읽는 도중 오류가 발생했습니다.", err)
        return;
    }
    console.log("파일 내용 :", data)
})

// write는 덮어쓰기 기능이 기본.
let content = "Four!"
fs.writeFile("number4.txt", content, (err) => {
    if(err){
        console.log("파일을 읽는 도중 오류가 발생했습니다.", err)
        return;
    }
    console.log("파일 쓰기가 완료되었습니다.")
})

// append는 파일의 마지막 부분에 이어쓰기. 파일이 없을 경우 새로 생성도 가능.
content = " It's will get better!!"
fs.appendFile("new_file.txt", content, (err) => {
    if(err){
        console.log("파일을 읽는 도중 오류가 발생했습니다.", err)
        return;
    }
    console.log("파일 생성 및 업데이트가 완료되었습니다.")
})