// 数值类型
var a = 5;
var b = 11.1;
console.log(typeof a);
console.log(typeof b);
console.log(typeof NaN);
console.log(parseInt(b));   // 11
console.log(parseFloat(a)); // 5
console.log(parseInt('123vffff'));   //123
console.log(parseInt('aaa1222'));   //NaN


//字符类型
var c = '单引号字符串';
var d = "双引号字符串";
var e = `多行内容字符串粉色的方式]
    发飞机上开飞机失联就哭了`;
console.log(c);
console.log(d);
console.log(e);
var name = 'zhang';
var age = 20;
var all = `my name is ${name}, age is ${age} `;  //自动去找对应的值，如果没有就会报错
console.log(all);       //my name is zhang, age is 20
console.log(c+d);    //单引号字符串双引号字符串

//布尔值
var t = true;
var f = false;
console.log(typeof t);//boolean
console.log(typeof f);//boolean