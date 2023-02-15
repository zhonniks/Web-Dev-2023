// 1
function sumsal(salaries) {

  let sum = 0;
  for (let salary of Object.values(salaries)) {
    sum += salary;
  }

  return sum;
}
let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

alert( sumsal(salaries) ); 
// 2
function count(obj) {
  return Object.keys(obj).length;
}
