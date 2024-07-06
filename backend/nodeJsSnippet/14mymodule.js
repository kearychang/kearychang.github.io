var fs = require('fs');
var path = require('path');

module.exports = function(dir, ext, callback) {
	extension = "." + ext;
	list = [];
	fs.readdir(dir, function(err, data) {
		if (err) {
			callback(err, []);
		} else {
			data.forEach(function(file) {
				if (file != undefined && path.extname(file) == extension) {
					list.push(file);
				}
			});
			callback(undefined, list);
		}
	});
};