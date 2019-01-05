---
layout: post
title:  "CoAP CoCoA"
date:   2018-04-30
excerpt: "Advanced congestion control for IoT protocol"
project: true
tag:
- frontend
- algorithm
comments: true
---    
    
<center>Make CoAP protocol more responsive to network conditions</center>

CoAP is an Internet application protocol for constrained nodes. The interaction model is similar to client/server model of HTTP with requests and responses. However, machine-to-machine interactions result in nodes acting in both client and server roles. In the network stack, CoAP rests on top of UDP. CoAP methods resemble HTTP method requests and responses.

When a Confirmable message (CON) is sent, it maintains an internal state for timeout and a counter. When timeout reaches 0 with no ACK, the counter is incremented and the Confirmable message (CON) is retransmitted with an increased timeout. This loops while the counter is less than MAX_RETRANSMIT. At this point, the sender gives up.

Contiki is an open source OS for IoT. It has its own implementation of CoAP. This [project](https://github.com/kearychang/CoAP-CoCoA) was to implement a variable backoff timer in ContikiOS. 

---

![Results]((https://raw.githubusercontent.com/kearychang/CoAP-CoCoA/master/img/results.jpg))

More indepth tutorial is on my [Readme](https://github.com/kearychang/CoAP-CoCoA/blob/master/README.md).