let time = document.getElementById("time");
let startBtn = document.getElementById("start");
let stopBtn = document.getElementById("stop");
let resetBtn = document.getElementById("reset");
let startTime, updatedTime, difference, tInterval, running = false;
let savedTime;
let hours, minutes, seconds, milliseconds;

startBtn.addEventListener("click", start);
stopBtn.addEventListener("click", stop);
resetBtn.addEventListener("click", reset);

// start 버튼 누르면 작동하는 함수
function start() {
    if (!running) {
        startTime = new Date().getTime();
        tInterval = setInterval(getShowTime, 1);
        running = true;
    }
}

// stop 버튼 누르면 작동하는 함수
function stop() {
    if (running) {
        clearInterval(tInterval);
        savedTime = difference;
        running = false;
    }
}

// reset 버튼 누르면 작동하는 함수
function reset() {
    clearInterval(tInterval);
    running = false;
    savedTime = 0;
    time.textContent = "경과시간 00:00:00:00";
}

function getShowTime() {
    updatedTime = new Date().getTime();
    if (savedTime) {
        difference = updatedTime - startTime + savedTime;
    } else {
        difference = updatedTime - startTime;
    }

    hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    seconds = Math.floor((difference % (1000 * 60)) / 1000);
    milliseconds = Math.floor((difference % 1000) / 10);
    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    milliseconds = milliseconds < 10 ? "0" + milliseconds : milliseconds;
    time.textContent = "경과시간 " + hours + ":" + minutes + ":" + seconds + ":" + milliseconds;
}