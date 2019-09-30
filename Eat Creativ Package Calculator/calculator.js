// Import the spreadsheet with the product packing and box info

// Take in the number of product types / products

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
})

rl.question('Enter the number of products in the order: ', (answer) => {
	var numProductTypes = answer;
	console.log(numProductTypes);
	rl.close();
})


// var numProductTypes = 3;

// Take in the quantity of each product

// for (var i = 0; i < numProductTypes; i++){
// 	var x = prompt("Write a number")
// 	console.log(x)
// }

// Use product lookup table to determine the number of trays per product

// Calculate the total number of trays

// Use the box combo lookup table to determine the proper box combo and its estimated weight

// Output the box combo and the estimated weight