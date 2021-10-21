console.log('Hello Wolrd')

const numbers = document.querySelector('.numbers').textContent;
const str = parseFloat(numbers).toFixed(1)

console.log(str)

document.numbers.innerText = str;
