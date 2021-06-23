function sigma(num){
    if(num<0){
        console.log("parameter cannot be negative");
        return("error");
    }
    var output=0;
    for(var i=num; i>0; i--){
        output+=i;
    }
    return output;
}

function factorial(num){
    if(num<0){
        console.log("parameter cannot be negative");
        return("error");
    }
    var output=1;
    for(var i=num; i>0; i--){
        output*=i;
    }
    return output;
}

function fib(num){
    if(num<0){
        console.log("parameter cannot be negative");
        return("error");
    }
    if(num<2){
        return(num);
    }
    return fib(num-2)+fib(num-1);
}

function secondToLast(array){
    if(array.length<2){
        console.log("array is too short");
        return("error");
    }
    return array[array.length-2];
}

function nthToLast(array, n){
    if(array.length<n){
        console.log("array is too short");
        return("error");
    }
    return array[array.length-n];
}

function secondLargest(array){
    if(array.length<2){
        console.log("array is too short");
        return("error");
    }
    var largest=0;
    var secondLargest=0;

    for(var i=1;i<array.length;i++){
        if(array[i]>largest){
            secondLargest=largest;
            largest=array[i];
        }
        else{
            if(array[i]>secondLargest){
                secondLargest=array[i];
            }
        }
    }
    return secondLargest;
}

function double(array){
    var output=[];
    for(var i=0;i<array.length;i++){
        output.push(array[i]);
        output.push(array[i]);
    }
    return output;
}
