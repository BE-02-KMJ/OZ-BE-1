function calculate(expression) {
  try {
    return eval(expression);
  } catch (error) {
    return "Error";
  }
}

const display = document.getElementById("display");
const buttons = document.querySelectorAll(".btn");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.id === "btnfinal") {
      // '=' 버튼 클릭 시 계산
      display.textContent = calculate(display.textContent);
    } else if (button.id === "btnclear") {
      // 'clear' 버튼 클릭 시 초기화
      display.textContent = "";
    } else {
      // 숫자 및 연산자 버튼 클릭 시
      display.textContent += button.textContent;
    }
  });
});