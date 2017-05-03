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

var locations = [
        {lat: -31.563910, lng: 147.154312},
        {lat: -33.718234, lng: 150.363181},
        {lat: -33.727111, lng: 150.371124},
        {lat: -33.848588, lng: 151.209834},
        {lat: -33.851702, lng: 151.216968},
        {lat: -34.671264, lng: 150.863657},
        {lat: -35.304724, lng: 148.662905},
        {lat: -36.817685, lng: 175.699196},
        {lat: -36.828611, lng: 175.790222},
        {lat: -37.750000, lng: 145.116667},
        {lat: -37.759859, lng: 145.128708},
        {lat: -37.765015, lng: 145.133858},
        {lat: -37.770104, lng: 145.143299},
        {lat: -37.773700, lng: 145.145187},
        {lat: -37.774785, lng: 145.137978},
        {lat: -37.819616, lng: 144.968119},
        {lat: -38.330766, lng: 144.695692},
        {lat: -39.927193, lng: 175.053218},
        {lat: -41.330162, lng: 174.865694},
        {lat: -42.734358, lng: 147.439506},
        {lat: -42.734358, lng: 147.501315},
        {lat: -42.735258, lng: 147.438000},
        {lat: -43.999792, lng: 170.463352}
      ];

	var imageBounds = {
         north: 39.945713,
         south: 39.822263,
         east:  -75.679667,
         west:  -75.881887
      };


	var mapOptions = {
        zoom: 10,
        center: new google.maps.LatLng(40.063168, -75.149746),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    $scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);
    var mcOptions = {gridSize: 50, maxZoom: 15, imagePath: 'https://cdn.rawgit.com/googlemaps/js-marker-clusterer/gh-pages/images/m'};
    
    $scope.markers = [];
    
    var infoWindow = new google.maps.InfoWindow();
    
    var createMarker = function (info){
        
        var marker = new google.maps.Marker({
            map: $scope.map,
            position: new google.maps.LatLng(info.lat, info.long),
            label: info.value,
            title : info.label
        });

        marker.content = '<div class="infoWindowContent">' + info.value + '</div>';


        var listener = google.maps.event.addListener(map, "idle", function () {
		    map.setZoom(10);
		    google.maps.event.removeListener(listener);
		});
        
        google.maps.event.addListener(marker, 'click', function(){
            infoWindow.setContent('<h2>' + marker.title + '</h2>' + marker.content);
            infoWindow.open($scope.map, marker);
        });
        
        $scope.markers.push(marker);
        
    }  
    
    for (i = 0; i < cities.length; i++){
        createMarker(cities[i]);
    }

    var mc = new MarkerClusterer(map, $scope.markers, mcOptions);

    $scope.openInfoWindow = function(e, selectedMarker){
        e.preventDefault();
        google.maps.event.trigger(selectedMarker, 'click');
    }

    /*$scope.getMapData = function(){
    	$http.post('/google').then(function (response) {
    		console.log(response.data);
    	});
    }*/

});
