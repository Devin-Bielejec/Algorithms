import { readFileSync } from 'fs';
const textByLine = readFileSync('data/small1.txt').toString().split("\n");


const weightLimit = 100;



const removeR = textByLine.map( item => item.replace(/\r/g, ""))
const arrayByRow = removeR.filter( item => item !== "");

console.log(arrayByRow);

const arrayOfArrays = arrayByRow.map( item => item.split(' ').map( string => Number(string)));

console.log(arrayOfArrays);

//Add in Profit/Weight - where Profit is the 3rd value in each array and Weight is the 2nd value in each array

const addedValues = arrayOfArrays.map( arr => {
    arr.push(arr[2]/arr[1]);
    return arr;
})

console.log(addedValues);

const profitWeightRateIndex = addedValues[0].length-1

///Sort array of arrays by the last item in each array
const sortedArray = addedValues.sort((x, y) => y[profitWeightRateIndex] >= x[profitWeightRateIndex]);

console.log(sortedArray);


//Now that we