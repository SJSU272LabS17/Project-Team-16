var app = angular.module("LoginCtrl", []);

app.controller("loginController", function ($scope, $http)
{

	$scope.postdata = function (yearlist) {
    var data = {
     year: yearlist
    }

    $http.post('/login', JSON.stringify(data)).then(function (response) {


    });

 }
  $scope.postdata('2017');
});
