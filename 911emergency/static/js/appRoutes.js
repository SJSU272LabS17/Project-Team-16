angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

	$routeProvider

		// home page
		.when('/', {
			templateUrl: 'static/views/home.html',
			controller: 'MainController'
		})

		.when('/trend', {
			templateUrl: 'static/views/trend.html',
			controller: 'TrendController'
		})

		.when('/donut', {
			templateUrl: 'static/views/donut.html',
			controller: 'DonutController'
		})

		.when('/trend_comparison', {
			templateUrl: 'static/views/trend_comparison.html',
			controller: 'TrendController'
		})

		.when('/map', {
			templateUrl: 'static/views/map.html',
			controller: 'MapController'
		})

		.when('/fake', {
			templateUrl: 'static/views/fake.html',
			controller: 'FakeCallController'
		});

	$locationProvider.html5Mode(true);

}]);
