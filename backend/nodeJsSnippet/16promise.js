var https = require('https');

async function getSite(site) {
  var b = await new Promise((resolve, reject) => {
    let body = '';
    https.get(site, (res) => {
      res.on('data', (chunk) => {
          body += chunk.toString();
      });

      //escape URL and regex match domain, then append to crawlList
      res.on('end', () => {
        resolve(body);
      });

      res.on('error', (err) => {
        reject(err);
      });
    });
  });
  console.log(b);
}

async function timer(time) {
  var b = await new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('foo');
    }, time);
  });
  console.log(b);
}

// timer(2000);
getSite("https://www.google.ca");