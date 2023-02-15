"use strict"

let str = "Hello";

str.test = 5; // (*)

alert(str.test);

//******************

function two_num(){
    let a = prompt("","");
    let b = prompt("", "");
    return a+b;
}

alert(two_num());

//*******************

alert( Math.round(6.35 * 10) / 10); // 6.35 -> 63.5 -> 64(rounded) -> 6.4

//******************

function readNumber() {
    let num;

    do {
        num = prompt("Number please?", 0);
    } while ( !isFinite(num) );

    if (num === null || num === '') return null;

    return +num;
}

alert(`Read: ${readNumber()}`);

//********************

let i = 0;
while (i < 11) {
    i += 0.2;
    if (i > 9.8 && i < 10.2) alert( i );
}

//*********************

function random(min, max) {
    return min + Math.random() * (max - min);
}

alert( random(1, 5) );
alert( random(1, 5) );
alert( random(1, 5) );

//*******************

function randomInteger(min, max) {
    // here rand is from min to (max+1)
    let rand = min + Math.random() * (max + 1 - min);
    return Math.floor(rand);
}

alert( randomInteger(1, 3) );

//*********************
