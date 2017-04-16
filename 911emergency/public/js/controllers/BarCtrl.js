angular.module('BarCtrl', []).controller('BarController', function($scope) {
	$scope.exampleData = 	
[
  {
    key: "Network In",
    color: "#51A351",
    values:
    [      
      { x : "EMS", y : 70127 },
      { x : "Fire", y : 21577 },
      { x : "Traffic",   y : 50656 }  
  ]}
  // },
  // {
    // key: "Network Out",
    // color: "#BD362F",
    // values:
    // [      
      // { x : "A", y : 60 },
      // { x : "B", y : 50 },
      // { x : "c",   y : 70 } 
    // ]
  // }
];
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

    d3.select("#barChart svg")
        .datum(exampleData())
        .transition().duration(350)
        .call(chart);

  return chart;
});
function exampleData() {
 return  [ 

        { 
          "label" : "Emergency Services" ,
          "value" : 70127
        } , 
        { 
          "label" : "Fire" , 
          "value" : 21577
        } , 
        { 
          "label" : "Traffic" , 
          "value" : 50656
        } 

  ]

}

$http.get("/emergency")
    .then(function(response) {
        $scope.data = response.data;
 });





});