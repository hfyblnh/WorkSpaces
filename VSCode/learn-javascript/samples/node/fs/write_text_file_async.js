'use strict'

console.log('>>> begin... >>>')

var fs = require('fs');

var data = 'Hello, Node.js';

fs.writeFile('output.txt', data, function(err) {
    if (err) {
        console.log(err);
    } else {
        console.log('Write OK!');
    }
});

console.log('>>> end. >>>')