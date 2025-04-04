
var express = require('express');
var app = express();
app.use(express.static(__dirname));
app.use(express.static(__dirname + '/autenticacao'));
app.use(express.static(__dirname + '/dashboard'));
app.use(express.static(__dirname + '/login'));
// app.use(express.static(__dirname + '/servicos'));
console.log('Listening on 8001');
app.listen(8001);

