// JavaScript to handle dropdown menu selection
document.addEventListener('DOMContentLoaded', function () {
    const dropdownButton = document.getElementById('dropdownButton');
    const dropdownMenu = document.getElementById('dropdownMenu');

    dropdownButton.addEventListener('click', function () {
        dropdownMenu.classList.toggle('hidden');
    });

    window.addEventListener('click', function (event) {
        if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.add('hidden');
        }
    });
});

// JavaScript to handle login/account dropdown menu
document.addEventListener('DOMContentLoaded', function () {
    const accountDropdownButton = document.getElementById('accountDropdownButton');
    const accountDropdownMenu = document.getElementById('accountDropdownMenu');

    accountDropdownButton.addEventListener('click', function () {
        accountDropdownMenu.classList.toggle('hidden');
    });

    window.addEventListener('click', function (event) {
        if (!accountDropdownButton.contains(event.target) && !accountDropdownMenu.contains(event.target)) {
            accountDropdownMenu.classList.add('hidden');
        }
    });
});

// JavaScript to handle image thumbnail click
document.querySelectorAll('.thumbnail').forEach(image => {
    image.addEventListener('click', function() {
        document.getElementById('mainImage').src = this.src;
    });
});
