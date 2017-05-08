var app = angular.module("LoginCtrl", []);

app.controller("loginController", function ($scope, $http, LoginService, $location)
{
	$scope.login = function () {
	    LoginService.setUsername($scope.username);
	    LoginService.setPassword($scope.password);
	    var authenticatePromise = LoginService.authenticate();
	    authenticatePromise.then(function(res){
	    	if(res){
	          	$location.path( "/trend_comparison");
	    	}else{
	    		alert("Error Authenticating User");
	    	}
	    });
 	}


});
