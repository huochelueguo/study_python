//普通函数定义
function f1() {
    console.log('hello world')
}
f1();
console.log('_____________');

//带参数的函数定义
function f2(a, b) {
    console.log(a+b)
}
f2(3, 4);    // 7
f2(1, 2, 3, 4, 5, 6);   // 如果参数多于函数需要的，则函数运行只会取需要的个数
console.log('_____________');

// 带返回值函数
function f3(a, b) {
    return a * b
}
var a = f3(222, 2);
console.log(a);
console.log('_____________');

// arguments
function add(a,b){
    console.log(a+b);
    console.log(arguments.length);
    console.log(arguments[0]);//arguments相当于将出传入的参数全部包含，这里取得就是第一个元素1
}
add(1,2);
console.log('_____________');

// 返回值为多个
function f4(a, b, c) {
    // return a+b;b-c
    return [a+b, b-c]
}
console.log(f4(2, 2, 2));   // [ 4, 0 ]
console.log(f4(2, 2, 2)[1]); // 0