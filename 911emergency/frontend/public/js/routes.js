var express = require('express');
var router = express.Router();
var path = require('path');
var usage = require('os-usage');
var monitor = require("js-network-monitor");
var os = require('os');


router.get('/memory', function(req, res, next){
	var freemem = os.freemem();
	var totalmem = os.totalmem();
	var memused = Math.round((totalmem - freemem)/(1024 * 1024) * 100) / 100;
	console.log(memused);
	var json = [];
	var counter = 0;
	var item = {};
	var values = {};
	values["x"] = 1000;
	values["y"] = memused;
	item["values"] = values;
	item["key"] = "memory";
	item["color"] = '#f9b800';
	json.push(item);
	res.send(JSON.stringify(json));
});

router.get('/cpu', function(req, res, next){
	var cpus = os.cpus();	
	for(var i = 0, len = cpus.length; i < len; i++) {
		var cpu = cpus[i], total = 0, processTotal = 0, strPercent = '';
		for(type in cpu.times){
			total += cpu.times[type];
		}

		for(type in cpu.times){
			var percent = Math.round(100 * cpu.times[type] / total);
			strPercent += percent + '%|';
		}
		res.send(JSON.stringify(strPercent));
	}
});

router.get('/networkInOut', function(req, res, next){
	monitor.start();
	monitor.on('start'), function(data){
		res.send(JSON.stringify(data));
	}
		
});

module.exports = router;
