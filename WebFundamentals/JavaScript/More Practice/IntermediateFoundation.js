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