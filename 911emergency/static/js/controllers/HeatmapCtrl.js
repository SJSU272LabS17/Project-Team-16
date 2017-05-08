var app = angular.module("HeatmapCtrl", []);

app.controller("HeatMapController", function ($scope, $http) {

	$scope.postdata = function (yearlist) {
	var data = {
	 year: yearlist
	}

	$http.post('/heat_map', JSON.stringify(data)).then(function (response) {
  var data1 = [
	{
		x: ['0:00', '1:00', '2:00', '3:00', '4:00','5:00', '6:00', '7:00', '8:00', '9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00' ],
		y: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December'],
		z: [response.data[0],response.data[1],response.data[2],response.data[3],response.data[4],response.data[5],response.data[6],response.data[7],response.data[8],response.data[9],response.data[10],response.data[11]],
	colorscale: [
		['0.0', 'rgb(49,54,149)'],
		['0.111111111111', 'rgb(69,117,180)'],
		['0.222222222222', 'rgb(116,173,209)'],
		['0.333333333333', 'rgb(171,217,233)'],
		['0.444444444444', 'rgb(224,243,248)'],
		['0.555555555556', 'rgb(254,224,144)'],
		['0.666666666667', 'rgb(253,174,97)'],
		['0.777777777778', 'rgb(244,109,67)'],
		['0.888888888889', 'rgb(215,48,39)'],
		['1.0', 'rgb(165,0,38)']
	],
		type: 'heatmap'
	}
];

Plotly.newPlot('myDiv', data1);
});
}
$scope.postdata('2016');
});
