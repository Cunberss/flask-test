let currentSort = '';

function updateSort(sort) {
    currentSort = sort;
    fetchData();
}

function fetchDataMain() {
    const xhr = new XMLHttpRequest();
    let url = 'http://127.0.0.1:5000/api/get-data';
    if (currentSort) {
        url += `?sort=${currentSort}`;
    }

    xhr.open('GET', url, true);
    xhr.onload = function () {
        if (this.status === 200) {
            const data = JSON.parse(this.responseText);
            const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];
            tableBody.innerHTML = ''; // Очистка таблицы перед добавлением новых данных

            data.forEach(function (record) {
                const row = tableBody.insertRow();
                row.innerHTML = `<td>${record.id}</td><td>${record.cpu_percent}</td><td>${record.timestamp}</td>`;
            });
        }
    };
    xhr.send();
}


function fetchDataAggregation() {
    const xhr = new XMLHttpRequest();
    let url = 'http://127.0.0.1:5000/api/get-aggregation-data';

    xhr.open('GET', url, true);
    xhr.onload = function () {
        if (this.status === 200) {
            const aggregationData = JSON.parse(this.responseText);
            document.getElementById('min-cpu').textContent = aggregationData.min;
            document.getElementById('max-cpu').textContent = aggregationData.max;
            document.getElementById('avg-cpu').textContent = aggregationData.avg;
        }
    };
    xhr.send();
}

function fetchData() {
    fetchDataMain(); // Функция для получения основных данных
    fetchDataAggregation(); // Функция для получения агрегированных данных
}


// Вызов fetchData() каждые 10 секунд
setInterval(() => {
    fetchData();
}, 10000);

// Начальная загрузка данных
fetchData();