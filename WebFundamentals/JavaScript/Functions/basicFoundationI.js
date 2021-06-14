/*

 Please work on the following challenges and upload your work in a single file.

    Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
    Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
    Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
    Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
    Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
    Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
    Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
    Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
    Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
    Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
    Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
    Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
    Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].


*/

/*

    Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

*/

function func1(){
    var result=[];
    for(var i=1; i<=255; i++){
        result[i-1]=i;
    }
    return result;
}

/*

Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

*/

function func2(){
    var result=0;
    for(var i=1; i<=1000; i++){
        result+=i;
    }
    return result;
}

/*

Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

*/

function func3(){
    var result=0;
    for(var i=1; i<=5000; i++){
        if(i%2===1){
            result+=i;
        }
    }
    return result;
}

/*

Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

*/

function func4(inputArray){
    var result=0;
    for(var i=0; i<inputArray.length; i++){
        result+=inputArray[i];
    }
    return result;
}

/*

Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

*/

function func5(inputArray){
    if(inputArray===[]){
        return 0;
    }
    var result=inputArray[0];
    for(var i=1; i<inputArray.length; i++){
        if(inputArray[i]>result){
            result=inputArray[i];
        }
    }
    return result;
}

/*

Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

*/

function func6(inputArray){
    var result=0;
    for(var i=0; i<inputArray.length; i++){
        result+=inputArray[i];
    }
    return result/inputArray.length;
}

/*

Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

*/

function func7(){
    var result=[];
    for(var i=1; i<=50; i++){
        if(i%2===1){
            result.push(i);
        }
    }
    return result;
}

/*

Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

*/

function func8(inputArray, y){
    var result=0;
    for(var i=0; i<inputArray.length; i++){
        if(inputArray[i]>y){
            result++;
        }
    }
    return result;
}

/*

Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

*/

function func9(inputArray){
    for(var i=0; i<inputArray.length; i++){
        inputArray[i]*=inputArray[i];
    }
    return inputArray;
}

/*

Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

*/

function func10(inputArray){
    for(var i=0; i<inputArray.length; i++){
        if(inputArray[i]<0){
            inputArray[i]=0;
        }
    }
    return inputArray;
}

/*

Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

*/

function func11(inputArray){
    if(inputArray===[]){
        return [];
    }
    var result=[inputArray[0],inputArray[0],inputArray[0]];
    for(var i=1; i<inputArray.length; i++){
        result[2]+=inputArray[i];
        if(inputArray[i]>result[0]){
            result[0]=inputArray[i];
        }
        if(inputArray[i]<result[1]) {
            result[1]=inputArray[i];
        }
    }
    result[2]/=inputArray.length;
    return result;
}

/*

Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

*/

function func12(inputArray){
    var temp=inputArray[0];
    inputArray[0]=inputArray[inputArray.length-1];
    inputArray[inputArray.length-1]=temp;
    return inputArray;
}

/*

Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

*/

function func13(inputArray){
    for(var i=0; i<inputArray.length; i++){
        if(inputArray[i]<0){
            inputArray[i]='Dojo';
        }
    }
    return inputArray;
}