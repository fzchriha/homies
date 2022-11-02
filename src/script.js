window.onload = () => {
    const rootElement = document.getElementById('root')
    const element = document.createElement('div')
    element.textContent = 'Hello Houses'
    element.className = 'container'
    rootElement.appendChild(element)
    document.querySelectorAll('.ng-star-inserted').forEach(item => {
        item.addEventListener('click', (e) => {
            document.querySelector('#NJ').forEach(state => {
                state.style.fill = "#2FAA9F";
            });
        });
    });
}