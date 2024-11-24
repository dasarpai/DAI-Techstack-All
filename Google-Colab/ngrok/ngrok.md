# setting up ngrok 

https://dashboard.ngrok.com/cloud-edge/endpoints


## install ngrok 
choco install ngrok 

## update authtoken 
ngrok config add-authtoken 2jxx----

# launch a launch server
python -m http.server 89

# test server 
curl http://localhost:89

# create tunnel, this will create a public url.

ngrok http 89

# hello-world.js code 
node hello-world.js

#hello-world.js file code 
const http = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});



