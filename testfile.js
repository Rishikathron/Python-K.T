const arr = [1,2,3,4,5]

for(let i = 0;i<arr.length;i++){
    console.log(typeof(i),arr[i]);
}

for(let i in arr){
    console.log(typeof(i),arr[i])
}