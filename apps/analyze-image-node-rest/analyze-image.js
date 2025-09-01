
'use strict';

let request;
try {
  request = require('request');
} catch (e) {
  console.error('Missing dependency: request. Run "npm install request dotenv" in this folder.');
  process.exit(1);
}

// Load from environment variables - no .env file needed
let subscriptionKey = process.env.AZURE_COMPUTER_VISION_KEY || process.env.AZURE_AI_SERVICES_KEY;
let endpoint = process.env.AZURE_COMPUTER_VISION_ENDPOINT || process.env.AZURE_AI_SERVICES_ENDPOINT;

if (!subscriptionKey || !endpoint) {
  console.error('❌ Error: Missing required environment variables!');
  console.error('Please set the following environment variables:');
  console.error('  - AZURE_COMPUTER_VISION_KEY (or AZURE_AI_SERVICES_KEY)');
  console.error('  - AZURE_COMPUTER_VISION_ENDPOINT (or AZURE_AI_SERVICES_ENDPOINT)');
  console.error('\nRefer to tim-env.txt for setup instructions.');
  process.exit(1);
}

var uriBase = endpoint + 'vision/v3.1/analyze';

const imageUrl = 'https://upload.wikimedia.org/wikipedia/commons/3/3c/Shaki_waterfall.jpg';

// Request parameters.
const params = {
    'visualFeatures': 'Categories,Description,Color',
    'details': '',
    'language': 'en'
};

const options = {
    uri: uriBase,
    qs: params,
    body: '{"url": ' + '"' + imageUrl + '"}',
    headers: {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key' : subscriptionKey
    }
};

request.post(options, (error, response, body) => {
  if (error) {
    console.log('Error: ', error);
    return;
  }
  let jsonResponse = JSON.stringify(JSON.parse(body), null, '  ');
  console.log('JSON Response\n');
  console.log(jsonResponse);
});
