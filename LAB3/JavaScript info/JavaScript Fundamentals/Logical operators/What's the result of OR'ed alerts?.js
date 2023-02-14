alert( alert(1) || 2 || alert(3) ); // 1 and 2 
// Solution : alert in boolean form undefined ,so it is falsy , our or goes on till 2 ( because it is first truthy value)
