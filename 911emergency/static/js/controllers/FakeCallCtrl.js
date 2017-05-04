var app = angular.module("FakeCallCtrl", []);

app.controller("FakeCallController", function ($scope, $http) {

  $http.get('/expenditure').then(function (response) {


  $scope.fakeCallData =  
[
  {
    key: "Fake Call Expenditure",
    color: "#BD362F",
    values:
    [      
      { x : "2015", y : 463005 },
      { x : "2016", y : 839475 }
    ]
  },
  {
    key: "Total Expenditure",
    color: "#51A351",
    values:
    [      
      { x : "2015", y : 1029868 },
      { x : "2016", y : 2035999 } 
    ]
  }
];
  nv.addGraph(function() {
    var chart = nv.models.multiBarChart()
      //.transitionDuration(350)
      .reduceXTicks(false)   //If 'false', every single x-axis tick label will be rendered.
      .rotateLabels(0)      //Angle to rotate x-axis labels.
      .showControls(true)   //Allow user to switch between 'Grouped' and 'Stacked' mode.
      .groupSpacing(0.1)    //Distance between each group of bars.


  

    chart.xAxis
        .tickValues([2015, 2016])
        .tickFormat(function(d) {
           return d;
         })
        .axisLabel('Fake Call Expenditure vs Total Expenditure');

    chart.yAxis
        .ticks(5)
        .tickFormat(function(d) { return "$" + d/100000 + " M"; })
        .axisLabel('Cost in Million Dollars');

    d3.select('#expChart svg')
        .datum($scope.fakeCallData)
        .call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
});


});

});
