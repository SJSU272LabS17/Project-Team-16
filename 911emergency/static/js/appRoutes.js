angular.module('appRoutes', [])
.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

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
		})

		.when('/home', {
			templateUrl: 'static/views/home_values.html',
			controller: 'TrendController'
		})

		.when('/small_b', {
			templateUrl: 'static/views/small_b.html',
			controller: 'TrendController'
		})

		.when('/overview', {
			templateUrl: 'static/views/overview.html',
			controller: 'OverviewController'
		})

		.when('/heat_map', {
			templateUrl: 'static/views/heat_map.html',
			controller: 'HeatMapController'
		})

		.when('/login', {
	      controller: 'loginController',
	      templateUrl: 'static/views/login.html',
	      controllerAs: 'vm'
	    })

    	.when('/register', {
	      controller: 'registerController',
	      templateUrl: 'static/views/register.html',
	      controllerAs: 'vm'
		  });

	$locationProvider.html5Mode(true);

}])
.run( function($rootScope, $location, LoginService) {

    // register listener to watch route changes
    $rootScope.$on( "$routeChangeStart", function(event, next, current) {
	 		if(next.templateUrl== "static/views/overview.html"){
				$location.path("/donut");
			}
			if ( LoginService.isValidUser() ||
      	next.templateUrl != "static/views/trend_comparison.html" ){

      }
			else {
        // no logged user, we should be going to #login
        if ( $location.path() == "/" || next.templateUrl == "views/login.html" ) {
          // already going to #login, no redirect needed
        } else {
          // not going to #login, we should redirect now
          $location.path( "/login" );
        }
      }
    });
 });
