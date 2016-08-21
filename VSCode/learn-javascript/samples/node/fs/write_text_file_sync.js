'use strict'

console.log('>>> begin... >>>')

var fs = require('fs');

var data = 'Hello, Node.js';

try {
    fs.writeFileSync('output.txt', data)
    console.log('Write OK!');
} catch (error) {
    console.log(error);
}

console.log('>>> end. >>>')