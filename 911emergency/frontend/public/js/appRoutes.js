angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

	$routeProvider

		// home page
		.when('/', {
			templateUrl: 'views/home.html',
			controller: 'MainController'
		})

		.when('/line', {
			templateUrl: 'views/line.html',
			controller: 'LineController'
		})

		.when('/bar', {
			templateUrl: 'views/bar.html',
			controller: 'BarController'	
		});

	$locationProvider.html5Mode(true);

}]);