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
		});

	$locationProvider.html5Mode(true);

}]);
