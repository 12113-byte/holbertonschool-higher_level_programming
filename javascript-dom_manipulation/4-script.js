const unsortedList = document.querySelector('ul');

unsortedList.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.innerHTML = 'Item';
    unsortedList.appendChild(newItem);
})
