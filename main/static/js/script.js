function toggleMenu() {
    let menuList = document.getElementById("menu-list");

    console.log("Menu button clicked!");

    if (menuList.style.maxHeight === "0px" || menuList.style.maxHeight === "") {
        console.log("Opening menu");
        menuList.style.maxHeight = menuList.scrollHeight + "px";
    } else {
        console.log("Closing menu");
        menuList.style.maxHeight = "0px";
    }
}

window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});


document.addEventListener('DOMContentLoaded', () => {
    const interestItems = document.querySelectorAll('.interest-item');

    interestItems.forEach(item => {
        item.addEventListener('click', () => {
            const checkbox = document.getElementById('interest-' + item.getAttribute('data-id'));
            checkbox.checked = !checkbox.checked; // Переключаем состояние чекбокса

            item.classList.toggle('selected'); // Обновляем визуальный стиль
        });
    });
});




document.getElementById('id_image').addEventListener('change', function() {
    var button = document.getElementById('file-button');
    var fileName = this.files.length > 0 ? this.files[0].name : '';
    if (fileName) {
        button.textContent = 'Изображение выбрано: ' + fileName;
    } else {
        button.textContent = 'Сначала выберите файл';
    }
});


