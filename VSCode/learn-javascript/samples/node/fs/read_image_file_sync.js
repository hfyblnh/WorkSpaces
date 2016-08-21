'use strict'

console.log('>>> begin... >>>')

var fs = require('fs');

try {
    var data = fs.readFileSync('sample.jpg');
    console.log(data);
    console.log(data.length + ' bytes');
} catch (err) {
    console.log(err);
}

console.log('>>> end. >>>')