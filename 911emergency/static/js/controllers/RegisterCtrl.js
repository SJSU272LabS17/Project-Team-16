var app = angular.module("RegisterCtrl", []);

app.controller("registerController", function ($scope, $http)
{

	$scope.postdata = function (yearlist) {
    var data = {
     year: yearlist
    }

    $http.post('/sign_up', JSON.stringify(data)).then(function (response) {


    });

 }
  $scope.postdata('2017');
});
