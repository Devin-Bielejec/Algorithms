import { readFileSync } from 'fs';
const textByLine = readFileSync('data/large1.txt').toString().split("\n");


const weightLimit = 100;

const removeR = textByLine.map( item => item.replace(/\r/g, ""))
const arrayByRow = removeR.filter( item => item !== "");
const arrayOfArrays = arrayByRow.map( item => item.split(' ').map( string => Number(string)));

//Add in Profit/Weight - where Profit is the 3rd value in each array and Weight is the 2nd value in each array

const addedValues = arrayOfArrays.map( arr => {
    arr.push(arr[2]/arr[1]);
    return arr;
})

///Sort array of arrays by the last item in each array
const sortedArray = addedValues.sort((x, y) => {
    //Sort largest to smallest profitWeightRate
    if (x[3] > y[3]) {
        return -1;
    } else if (x[3] == y[3]) {
        //If they have the same profit rate, then make the one that is less weight be higher in the array
        if (x[2] < y[2]){
            return -1;
        } else {
            return 1;
        }
    } else {
        return 1;
    };
})



//Now we are going to make a new array, so that we can add items to it, add to the total weight, and add to the total value
const itemsSelected = [];
let totalWeight = 0;
let totalValue = 0;

for (let i = 0; i < sortedArray.length; i++) {
    sortedArray[i][0] === 987 ? console.log(`HERE ${sortedArray[i]}`) : null;
    if (totalWeight + sortedArray[i][1] <= weightLimit) {
        console.log(`Total weight currently is ${totalWeight}`)
        //Added the item number to the array as long as the weight of the item plus the total weight is less than or equal to 100
        console.log(`Current item is ${sortedArray[i]}`)
        itemsSelected.push(sortedArray[i][0])
        totalWeight += sortedArray[i][1]
        totalValue += sortedArray[i][2]
    }
}


// Maybe I loop through my list and check to see if any two items are less than 1 single item on original
// this would take care of rare cases where an item of 2 is worth more than two items etc
for (let i = 0:)


console.log(totalWeight);
console.log(totalValue);




///Testing to make sure final answer is actually correct
let w = 0;
for (let i = 0; i < answerArray.length; i++){
    //each item is index 1 higher
    console.log(answerArray[i]-1)
    w += arrayOfArrays[answerArray[i]-1][1];
}

// //Finidng the different value
// answerArray.forEach( item => !itemsSelected.includes(item) ? console.log(item) : null );
// itemsSelected.forEach( item => !answerArray.includes(item) ? console.log(item) : null);


///I have 329 and 700 - answer has 987












// 987 2 27 = 13.5
// 329 1 15 = 15
// 700 1 11 = 11


// 1 3000 30 = 100
// 2 2000 20 = 100
// 3 1500 15 = 100

/* 

Maybe I loop through my list and check to see if any two items are less than 1 single item on original

this would take care of rare cases where an item of 2 is worth more than two items etc



*/