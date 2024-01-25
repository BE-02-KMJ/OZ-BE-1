function darkMode() {
    var body = document.body;
    body.classList.toggle("dark-mode");
}

function getCurrentDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `업데이트 날짜: (${year}-${month}-${day})`;
}
// span 업데이트 함수
function updateDate() {
const updateDateSpan = document.querySelector('.updateDate');
updateDateSpan.textContent = getCurrentDate();
}
// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function () {
updateDate(); // 초기에 한 번 업데이트
});

// 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
// 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리르 작성해 볼 수 있음
let data = [
    { checkbox: '', category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { checkbox: '', category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { checkbox: '', category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { checkbox: '', category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    // ...
];

let dataTable = document.getElementById('data-table');

data.forEach((item) => {
    const row = dataTable.insertRow();
    row.insertCell(0).innerHTML = `<td><input type="checkbox" name="check"></td>`;
    row.insertCell(1).innerHTML = item.category;
    row.insertCell(2).innerHTML = item.brand;
    row.insertCell(3).innerHTML = item.product;
    row.insertCell(4).innerHTML = item.price;
});

document.addEventListener("DOMContentLoaded", function() {
    var chkAll = document.getElementById("chkAll");
    var checkboxes = document.getElementsByName("check");
  
    chkAll.addEventListener("click", function() {
      checkboxes.forEach(function(checkbox) {
        checkbox.checked = chkAll.checked;
      });
    });
  
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener("click", function() {
        if (document.querySelectorAll('input[name="check"]:checked').length === checkboxes.length) {
          chkAll.checked = true;
        } else {
          chkAll.checked = false;
        }
      });
    });
  });