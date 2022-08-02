const FormData = require("form-data");
const fs = require("fs");
const https = require("https");
const args = process.argv.slice(2);
args[0];

var form = new FormData();
form.append('image', fs.createReadStream(`${args[0]}.jpg`)); // <-- 5.py 7번째 줄에서 넣은 chicken_10이 들어감

var headers = form.getHeaders();
headers['Authorization'] = 'Bearer 92a014b38acdc70cdb3e9cccb077e0623e5c5fef';
// 55770b5f110997309677e2afac255a3701b2c06f

const options = {
    hostname: 'api.logmeal.es',
    path: '/v2/image/segmentation/complete',
    method: 'POST',
    headers: headers,
};

const req = https.request(options, (res) =>{
    res.on('data', (d) => {
        process.stdout.write(d);
    });
});

form.pipe(req);