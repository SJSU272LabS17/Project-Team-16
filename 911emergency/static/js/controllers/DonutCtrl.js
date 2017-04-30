var app = angular.module("DonutCtrl", []);

app.controller("DonutController", function ($scope, $http) {

	$scope.yearlist = ['2016','2015'];
	$scope.postdata = function (yearlist) {
	var data = {
	 year: yearlist
	}

	$http.post('/emergency', JSON.stringify(data)).then(function (response) {


	nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true)     //Display pie labels
      .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
 //Configure what type of data to show in the label. Can be "key", "value" or "percent"
      .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
      .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
      ;

    d3.select("#donutChart svg")
        .datum(response.data)
        .transition().duration(350)
        .call(chart);

  return chart;
});



});

}

});
