'use strict'

// read text from 'sample.txt'

console.log('>>> begin... >>>')

var fs = require('fs');

//Node.js标准的回调函数：第一个参数代表错误信息，第二个参数代表结果
fs.readFile('sample.txt', 'utf-8', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});

console.log('>>> end. >>>')
