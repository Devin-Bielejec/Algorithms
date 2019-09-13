import { readFileSync } from 'fs';

function getBestItems(file, limit) {
    const textByLine = readFileSync(file).toString().split("\n");

    const weightLimit = limit;

    let items = textByLine.map( item => item.replace(/\r/g, ""))
    items = items.filter( item => item !== "");
    items = items.map( item => item.split(' ').map( string => Number(string)));

    //Add an index to each array to show strength (3rd item/2nd item)
    //Also we are going to set each array to be an object, so we can use keys to better understand things below
    items = items.map( arr => {
        let newObj = {};
        newObj.index = arr[0];
        newObj.weight = arr[1];
        newObj.value = arr[2];
        newObj.strength = newObj.value/newObj.weight;
        return newObj;
    })

    console.log(items);

    ///Sort array of arrays in descending order of strength
    const sortedStore = items.sort((x, y) => {
        //Sort largest to smallest
        if (x.strength > y.strength) {
            return -1;
        } else if (x.strength == y.strength) {
            //If they have the same strength index 3
            //Then we want the item with a smaller weight 2
            if (x.weight < y.weight){
                return -1;
            } else {
                return 1;
            }
        } else {
            return 1;
        };
    })



    //We make a new array to add items to it (ADDING ITEMS TO OUR BAG)
    let bag = [];
    let totalWeight = 0;
    let totalValue = 0;

    for (let i = 0; i < sortedStore.length; i++) {
        //Add item to our BAG if it's under the weightLimit
        const currentNotBagItem = sortedStore[i];
        if (totalWeight + currentNotBagItem.weight <= weightLimit) {
            bag.push(currentNotBagItem);
            totalWeight += currentNotBagItem.weight;
            totalValue += currentNotBagItem.value;
        }
    }

    let notBag = sortedStore.filter( item => !bag.includes(item));
    console.log(notBag);

    //Average of the two weakest items in the bag
    let weakestAverage = (bag[bag.length-1].strength + bag[bag.length-2].strength)/(2);
    console.log(weakestAverage);

    let itemsToAdd = [];
    let itemsToReplace = [];

    for (let i = 0; i < notBag.length; i++){
        const currentNotBagItem = notBag[i];

        //One item that is notBag will never replace one item in bag, so we do weakest average to find the lowest average we're trying to replace with 1 item
        if (currentNotBagItem.strength > weakestAverage) {
            //We don't want items that have the same weight as currentNotBagItem
            //We want to look through these potentialReplacements in ascending order        
            const potentialReplacements = bag.filter( arr => arr.weight < currentNotBagItem.weight).reverse();

            //We are going to loop through potential replacements and keep track of weight and the items
            let weightCount = 0;
            let choiceItems = [];
            for (let j = 0; j < potentialReplacements.length; j++){
                
                weightCount += potentialReplacements[j].weight;
                if (weightCount > currentNotBagItem.weight){
                    continue;
                } else {
                    choiceItems.push(potentialReplacements[j]);

                    //Check if average of choiceItems is < than my currentNotBagItemStrength
                    let choicesAverage = choiceItems.reduce( (acc, cur) => acc.strength + cur.strength,{strength: 0})/(choiceItems.length);
                    if (choicesAverage < currentNotBagItem.strength){
                        //Now we replace our currentNotBagItem
                        itemsToAdd.push(currentNotBagItem);
                        itemsToReplace.push(choiceItems);

                        //Also set new weakest strength to current weakest strength of my item

                        //Find index of item before last item in choiceItems to obtain new second weakest item in array way above
                        let secondWeakestIndex = bag.indexOf(choiceItems[choiceItems.length-1])-1;
                        weakestAverage = (currentNotBagItem.strength + bag[secondWeakestIndex])/2;
                    }
                }
            }
        }
    }

    console.log(itemsToAdd)
    console.log(itemsToReplace)

    //Now we have to return the bag with the correct items
    for (let i = 0; i < itemsToReplace.length; i++){
        //Remove items
        console.log(bag.length);
        itemsToReplace[i].forEach( item => {
            bag.splice(bag.indexOf(item), 1);
        })
        console.log(bag.length)
        //Add items
        itemsToAdd.forEach((item) => bag.push(item))
    }
    console.log(bag);
    let finalWeight = 0;
    let finalValue = 0;
    let finalAnswers = [];
    for (let i = 0; i < bag.length; i++){
        console.log(bag[i])
        finalWeight += bag[i].weight;
        finalValue += bag[i].value;
        finalAnswers.push(bag[i].index);
    }
    console.log(finalWeight);
    console.log(finalValue);
    console.log(finalAnswers);

    return finalAnswers.sort();
}

console.log(getBestItems("./data/large1.txt", 100));
console.log(getBestItems("./data/small1.txt", 100));
console.log(getBestItems("./data/small2.txt", 100));
console.log(getBestItems("./data/small3.txt", 100));
console.log(getBestItems("./data/medium1.txt", 100));
console.log(getBestItems("./data/medium2.txt", 100));
console.log(getBestItems("./data/medium3.txt", 100));

