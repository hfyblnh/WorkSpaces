'use strict';

var s = 'Hello';

function greet(name) {
    console.log(s + ',' + name + '!');
}

function hi(name) {
    console.log('Hi, ' + name + '!');
}

function goodbye(name) {
    console.log('Goodbye, ' + name + '!');
}

// 强烈建议使用module.exports = xxx的方式来输出模块变量
module.exports = {
    greet: greet,
    hi: hi,
    goodbye: goodbye,
}