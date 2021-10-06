// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

'use strict';

let https = require('https');
const subscription_key = "";
const endpoint = "";
const path = '/text/analytics/v2.1/sentiment'
const { ActivityHandler, MessageFactory } = require('botbuilder');

class EchoBot extends ActivityHandler {
    constructor() {
        super();
        // See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
        this.onMessage(async (context, next) => {

            let documents = {
                'documents': [
                    { 'id': '1', 'language': 'en', 'text': context.activity.text },
                ]
            };


            let body = JSON.stringify(documents);

            let request_params = {
                method: 'POST',
                hostname: (new URL(endpoint)).hostname,
                path: path,
                headers: {
                    'Ocp-Apim-Subscription-Key': subscription_key,
                }
            };

            let response = await makeRequest(request_params, body);

            const reply = (
                response.documents[0].score > 0.8 ? 'You sound happy! I\'m glad to hear that!' :
                response.documents[0].score > 0.2 ? 'Sounds like a pretty good day so far.' :
                'You don\'t sound very happy. Sorry to hear that!'
            );
            await context.sendActivity(MessageFactory.text(reply, reply));
            // By calling next() you ensure that the next BotHandler is run.
            await next();
            });

        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            const welcomeText = 'Hi! How is your day going?';
            for (let cnt = 0; cnt < membersAdded.length; ++cnt) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(MessageFactory.text(welcomeText, welcomeText));
                }
            }
            // By calling next() you ensure that the next BotHandler is run.
            await next();
        });
    }
}

function makeRequest(options, data) {
    return new Promise((resolve, reject) => {
      const req = https.request(options, (res) => {
        res.setEncoding('utf8');
        let responseBody = '';

        res.on('data', (chunk) => {
          responseBody += chunk;
        });

        res.on('end', () => {
          resolve(JSON.parse(responseBody));
        });
      });

      req.on('error', (err) => {
        reject(err);
      });

      req.write(data)
      req.end();
    });
  }

module.exports.EchoBot = EchoBot;