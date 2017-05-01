angular.module("MapCtrl", []).controller("MapController", function ($scope, $http) {

	$scope.yearlist = ['2016','2015'];

	    var cities = [
    {
  
        lat : 39.974950799999995,
        long : -75.2708694,
        value : '96',
        label : 'Emergency Count'
    },
    {
        lat : 39.9936176,
        long : -75.2467288,
        value : '101',
        label : 'Emergency Count'
    },
    {
       lat : 39.999803700000001,
        long : -75.22946800000001,
        value : '74',
        label : 'Emergency Count'
    },
    {
       lat : 39.9792542,
        long : -75.27134190000001,
        value : '66',
        label : 'Emergency Count'
    },
    {
        lat : 30.33359600000000,
        long : -95.5955947,
        value : '1',
        label : 'Emergency Count'
    }
];
	var bounds = new google.maps.LatLngBounds();
	var mapOptions = {
        zoom: 10,
        center: new google.maps.LatLng(39.974950799999995, -75.4999024)
    }

    $scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);

    $scope.markers = [];
    
    var infoWindow = new google.maps.InfoWindow();
    
    var createMarker = function (info){
        
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(info.lat, info.long),
            label: info.value
        });

        bounds.extend(marker.position);
        marker.content = '<div class="infoWindowContent">' + info.value + '</div>';

        //marker.showInfoWindow();

        map.fitBounds(bounds);

        var listener = google.maps.event.addListener(map, "idle", function () {
		    map.setZoom(20);
		    google.maps.event.removeListener(listener);
		});
        
        google.maps.event.addListener(marker, 'click', function(){
            infoWindow.setContent('<h2>' + marker.label + '</h2>' + marker.content);
            infoWindow.open($scope.map, marker);
        });
        
        $scope.markers.push(marker);
        
    }  
    
    for (i = 0; i < cities.length; i++){
        createMarker(cities[i]);
    }

    $scope.openInfoWindow = function(e, selectedMarker){
        e.preventDefault();
        google.maps.event.trigger(selectedMarker, 'click');
    }

    $scope.getMapData = function(){
    	$http.post('/google').then(function (response) {
    		console.log(response.data);
    	});
    }

});
