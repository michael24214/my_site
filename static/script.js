document.addEventListener('DOMContentLoaded', function() {
    // Пример для анимации при клике на кнопку
    const buttons = document.querySelectorAll('.skill__button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Добавляем анимацию, чтобы указать, что кнопка была нажата
            button.classList.add('clicked');
            setTimeout(() => {
                button.classList.remove('clicked');
            }, 300);
        });
    });

    // Можно добавить другие интерактивные элементы, если нужно
});
