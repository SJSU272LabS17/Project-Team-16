angular.module("MapCtrl", []).controller("MapController", function ($scope, $http) {


// 	$scope.postdata = function (year) {
// 	$scope.year = year;
// }


    $scope.openInfoWindow = function(e, selectedMarker){
        e.preventDefault();
        google.maps.event.trigger(selectedMarker, 'click');
    }

    $scope.getMapData = function(year1){
        var data = {
            year : year1
        }
					$scope.year = year1;
    	$http.post('/google', JSON.stringify(data)).then(function (response) {
            var data = response.data;
    		console.log(response.data.length);
            var mapOptions = {
                zoom: 10,
                center: new google.maps.LatLng(40.063168, -75.149746),
                mapTypeId: google.maps.MapTypeId.ROADMAP
            }

            $scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);
            var mcOptions = {gridSize: 50, maxZoom: 10, imagePath: 'https://cdn.rawgit.com/googlemaps/js-marker-clusterer/gh-pages/images/m'};

            $scope.markers = [];

            var infoWindow = new google.maps.InfoWindow();

            var createMarker = function (info){

                var marker = new google.maps.Marker({
                    map: $scope.map,
                    position: new google.maps.LatLng(info[0], info[1]),
                    // label: info.value,
                    //title : info.label
                });

                marker.content = '<div class="infoWindowContent">' + '<h2>' + info[2] + '<h2>' + '</div>';


          //       var listener = google.maps.event.addListener(map, "idle", function () {
                //     map.setZoom(10);
                //     google.maps.event.removeListener(listener);
                // });

                google.maps.event.addListener(marker, 'click', function(){
                    infoWindow.setContent(marker.content);
                    infoWindow.open($scope.map, marker);
                });

                $scope.markers.push(marker);

            }

            for (i = 0; i < 7000; i++){
                createMarker(data[i]);
            }

            var mc = new MarkerClusterer($scope.map, $scope.markers, mcOptions);

    	});
    }

		$scope.getMapData('2017');

});
