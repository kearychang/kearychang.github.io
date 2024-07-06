//This script visits various paths belonging to a domain to test disabling of header/nav and prompts user between URLs
//Entities were taken from ensembleUI/.../TR1LaunchUIParser.java from SVN Core 9.6.x & record not included

var url = "http://192.168.221.180:8111/t1-cp-ops/#LUI";

var entities = [
    "customer", "view", "network", "location", "networkElement", "provider", "elementManager", 
    "vlan.generator", "vpls.vpn.id.generator", "vpws.vc.id.generator", "ipaddress.generator",
    "facility", "path", "etherlink", "iplink", "connection", "eline", "elan", "etree", "ipvpn",
    "process", "cm_serviceorder", "cm_contact", "cm_requestgroup", "cm_ticket", "cfservice"
]

var testEntities = [
    "network.2fibupsr", "network.2fibblsr", "network.dwdm", "network.sncp", "network.2fibmsspr",
    "network.4fibmspr", "network.bgp", "network.linear", "network.protectedlinear", "network.ethernet",
    "network.ospf", "network.isis", "domain", "schedulerDefinition", "cfservice"
];

var operations = ["search", "open", "create"];

for (op in operations) {
    for (e in entities) {
        let newUrl = url + operations[op];
        switch (operations[op]) {
            case ("search"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f";
                break;
            case ("open"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f/1";
                break;
            case ("create"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f";
                break;
            default:
        }
        window.location.href = newUrl;
        console.log(newUrl);
        alert(url);
    }
    for (e in testEntities) {
        let newUrl = url + operations[op];
        switch (operations[op]) {
            case ("search"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f";
                break;
            case ("open"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f/1";
                break;
            case ("create"):
                newUrl = newUrl + "/" + entities[e] + "/.nav=f/.hdr=f";
                break;
            default:
        }
        window.location.href = newUrl;
        console.log(newUrl);
        alert(url);
    }
}