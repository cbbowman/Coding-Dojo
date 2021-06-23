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

console.log(fib(5));