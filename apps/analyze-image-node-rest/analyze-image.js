
'use strict';

let request;
try {
  request = require('request');
} catch (e) {
  console.error('Missing dependency: request. Run "npm install request dotenv" in this folder.');
  process.exit(1);
}

// Load environment variables from .env if available
try { require('dotenv').config(); } catch (e) {}

// Prefer generic COGNITIVE_*; fall back to COMPUTER_VISION_* for compatibility
let subscriptionKey = process.env.COGNITIVE_KEY || process.env.COMPUTER_VISION_SUBSCRIPTION_KEY;
let endpoint = process.env.COGNITIVE_ENDPOINT || process.env.COMPUTER_VISION_ENDPOINT;

if (!subscriptionKey || !endpoint) {
  console.error('Missing env vars. Set COGNITIVE_ENDPOINT and COGNITIVE_KEY (or COMPUTER_VISION_*).');
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
