angular.module('TrendCtrl', []).controller('TrendController', function($scope, $http) {
	
	
	$scope.yearlist = ['2016','2015'];

	$scope.categories = function(){
		$http.post('/category').then(function (response) {
			$scope.categoriesData = response.data;
		})
	}

	$scope.subcategories = function(){
		var data = {
			year : $scope.year,
			emergency_type : $scope.category
		}
		$http.post('/sub_category',JSON.stringify(data)).then(function (response) {
			$scope.subcategoriesData = response.data;
		})
	}

	$scope.getTrends = function(){
		var data = {
			year : $scope.year,
			emergency_type : $scope.category,
			sub_emergency_type : $scope.subcategory
		}

		$http.post('/emergency_trend',JSON.stringify(data)).then(function (response) {
			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100 }) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		       /* .tickValues(function(d){
		        	return d3.time.format('%b')(new Date(d))
		        })*/
		        .tickFormat(function(d) {
		            return d3.time.format('%b')(new Date(d))
		          });

		    /*chart.yAxis
		        .tickFormat(d3.format(',.1%'));*/

		    d3.select('#trendChart svg')
		        .datum($scope.exampleData)
		        .call(chart);

		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})
		
	}

	$scope.exampleData = function(){
		return [
  {
    "key": "Series 1",
    "values": [ [ 0 , 0] , [ 2 , -6.3382185140371] , [ 3 , -5.9507873460847] , [ 4 , -11.569146943813] , [ 5 , -5.4767332317425] , [ 6 , 0.50794682203014] , [ 7 , -5.5310285460542] , [ 8 , -5.7838296963382] , [ 9 , -7.3249341615649] , [ 10 , -6.7078630712489] , [ 11 , 0.44227126150934]]
  }
]
	}
	 
	

	  
	});



