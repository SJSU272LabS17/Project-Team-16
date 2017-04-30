angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

	$routeProvider

		// home page
		.when('/', {
			templateUrl: 'static/views/home.html',
			controller: 'MainController'
		})

		.when('/line', {
			templateUrl: 'static/views/line.html',
			controller: 'LineController'
		})

		.when('/bar', {
			templateUrl: 'static/views/bar.html',
			controller: 'BarController'
		});

	$locationProvider.html5Mode(true);

}]);
