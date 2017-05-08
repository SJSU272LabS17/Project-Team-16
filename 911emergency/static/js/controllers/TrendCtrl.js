
angular.module('TrendCtrl', []).controller('TrendController',
	function($scope, $http, $rootScope, LoginService, $location, $window) {

	$scope.year = '2016';
	$scope.postdata = function (year) {
		$scope.year = year;
	}

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

			var values = response.data;
			var xTicks = [];
			for (var i = 0 ; i < values.length; i++) {
				xTicks.push(values[i][0]);
			}

			var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]



			$scope.trendData =  [
			  {
			    "key": $scope.subcategory,
			    "values": response.data
			  }
			]

			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100}) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		        .tickValues(xTicks)
		        .tickFormat(function(d) {
		        	var date = new Date(d*1000);
		            return d3.time.format('%b')(date);
		         })
		  //       chart.xAxis.tickValues([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
				// .tickFormat(function(d){
				//     return days[d]
				// })
		        .axisLabel('Months');

		     chart.yAxis
        		.tickFormat(d3.format(',.1%'))
        		.axisLabel('Emergency Count');

		    d3.select('#trendChart svg')
		        .datum($scope.trendData)
		        .call(chart);

		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})

	}


	$scope.compareTrends = function(){

			var data = {
			year : $scope.year,
			emergency_type : $scope.category,
			sub_emergency_type1 : $scope.subcategory1,
			sub_emergency_type2 : $scope.subcategory2
		}
		// $http.defaults.headers.common['Authorization'] = 'Basic ' + Base64.encode(LoginService.username + ':' + LoginService.password);
		$http.post('/trend_comparison',JSON.stringify(data)).then(function (response) {

			var values = response.data;
			var xTicks = [];
			for (var i = 0 ; i < values.length; i++) {
				xTicks.push(values[i][0]);
			}
			$scope.trendCompData =  [
			  {
			    "key": response.data[0].label,
			    "values": response.data[0].value
			  },
			  {
			    "key": response.data[1].label,
			    "values": response.data[1].value
			  }
			]

			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100}) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		        .tickValues(  [ 1454195838, 1456874238, 1459379838, 1462058238, 1464650238, 1467328638, 1469920638, 1472599038, 1475277438, 1477869438, 1480547838,1483139838 ])
		        .tickFormat(function(d) {
		            return d3.time.format('%b')(new Date(d*1000))
		          })
		        .axisLabel('Months');

		      chart.yAxis
        		.tickFormat(d3.format(',.1%'))
        		.axisLabel('Emergency Count');

		      d3.select('#trendCompChart svg')
		        .datum($scope.trendCompData)
		        .call(chart);


		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})
	}

	$scope.compareHomeData = function(){


		$http.get('/h_value').then(function (response) {

			var values = response.data[0].value;
			var xTicks = [];
			for (var i = 0 ; i < values.length; i++) {
				xTicks.push(values[i][0]);
			}

			$scope.homeCompData =  [
			  {
			    "key": response.data[0].label,
			    "values": response.data[0].value
			  },
			  {
			    "key": response.data[1].label,
			    "values": response.data[1].value
			  }
			]

			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100}) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		        .tickValues( xTicks)
		        .axisLabel('Year');

		      chart.yAxis
        		.tickFormat(d3.format(',.1%'))
        		.axisLabel('Emergency Count');

		      d3.select('#homeValueChart svg')
		        .datum($scope.homeCompData)
		        .call(chart);


		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})
	}

	$scope.compareBusinessData = function(){


		$http.get('/small_b').then(function (response) {

			var values = response.data[0].value;
			var xTicks = [];
			for (var i = 0 ; i < values.length; i++) {
				xTicks.push(values[i][0]);
			}

			$scope.smallBData =  [
			  {
			    "key": response.data[0].label,
			    "values": response.data[0].value
			  },
			  {
			    "key": response.data[1].label,
			    "values": response.data[1].value
			  },
			  {
			    "key": response.data[2].label,
			    "values": response.data[2].value
			  },
			  {
			    "key": response.data[3].label,
			    "values": response.data[3].value
			  },
			  {
			    "key": response.data[4].label,
			    "values": response.data[4].value
			  }

			]

			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100}) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		        .tickValues( xTicks)
		        // .tickFormat(function(d) {
		        //     return new Date(d*1000).getFullYear();
		        //   })
		        .axisLabel('Year');

		      chart.yAxis
        		.tickFormat(d3.format(',.1%'))
        		.axisLabel('Emergency Count');

		      d3.select('#smallBChart svg')
		        .datum($scope.smallBData)
		        .call(chart);


		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})
	}

	// $rootScope.$on('$routeChangeStart', function (event) {
 //          console.log('route changed!!');
 //          if (!LoginService.isValidUser()) {
 //            console.log('DENY : Redirecting to Login');
 //            event.preventDefault();
 //           $window.addEventListener('$routeChangeStart', function(e) {
	// 	      $rootScope.$apply(function() {
	// 	        $location.path("/login");
	// 	        console.log($location.path());
	// 	    });
 //  			});
 //            //$location.path('/login').replace();
 //          }
 //          else {
 //            console.log('ALLOW');
 //          }
 //      });



	});
