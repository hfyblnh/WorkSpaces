'use strict'

console.log('>>> begin... >>>')

var fs = require('fs');

try {
    var data = fs.readFileSync('sample.txt', 'utf-8');
    console.log(data);
} catch (err) {
    console.log(err);
}

console.log('>>> end. >>>')