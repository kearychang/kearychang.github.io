const { WorkerPool } = require('./workerpool.js');
const { isMainThread, parentPort } = require('worker_threads');

function doSomething(ch) {
    ch.port1.postMessage("HI");
}

if (isMainThread) {
    const wp = new WorkerPool(2, '15worker.js', true);
    var ch = wp.getChannel();
    let finished = 0;
    for (let i = 0; i < 5; i++) {
        wp.runTask(doSomething(ch), (err, result) => {
            console.log(i, err, result);
            if (++finished === 5)
                wp.close();
        });
    }
    ch.port2.on('message', (message) => {
        console.log(message);
    });
} else {
    parentPort.on('message', (task) => {
        console.log("PARENT");
        parentPort.postMessage(task);
    });
}
