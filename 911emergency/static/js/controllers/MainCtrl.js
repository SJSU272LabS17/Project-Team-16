angular.module('MainCtrl', []).controller('MainController', function($scope,$timeout, $q, $log,$location) {

	$scope.tagline = 'To the moon and back!';

	$scope.overView = function () {
		$location.path("/overview");
	}


	var self = this;

	self.simulateQuery = false;
	self.isDisabled    = false;


	// self.querySearch   = self.querySearch;
	// self.selectedItemChange = self.selectedItemChange;
	// self.searchTextChange   = self.searchTextChange;

	//self.newState = self.newState;

	$scope.newState = function (state) {
		alert("Sorry! You'll need to create a Constitution for " + state + " first!");
	}

	// ******************************
	// Internal methods
	// ******************************

	/**
	 * Search for states... use $timeout to simulate
	 * remote dataservice call.
	 */
	$scope.querySearch = function  (query) {
		var results = query ? self.states().filter( self.createFilterFor(query) ) : self.states(),
				deferred;
		if (self.simulateQuery) {
			deferred = $q.defer();
			$timeout(function () { deferred.resolve( results ); }, Math.random() * 1000, false);
			return deferred.promise;
		} else {
			return results;
		}
	}

	$scope.searchTextChange = function (text) {
		$log.info('Text changed to ' + text);
	}

	$scope.selectedItemChange = function (item) {
		$log.info('Item changed to ' + JSON.stringify(item));
		$location.path("/overview");
	}

	/**
	 * Build `states` list of key/value pairs
	 */
	self.loadAll = function () {
		var allStates = 'Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware,\
						Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana,\
						Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana,\
						Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina,\
						North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina,\
						South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia,\
						Wisconsin, Wyoming';

		return allStates.split(/, +/g).map( function (state) {
			return {
				value: state.toLowerCase(),
				display: state
			};
		});
	}

	// list of `state` value/display objects
	self.states        = self.loadAll;

	/**
	 * Create filter function for a query string
	 */
	self.createFilterFor = function (query) {
		var lowercaseQuery = angular.lowercase(query);

		return function filterFn(state) {
			return (state.value.indexOf(lowercaseQuery) === 0);
		};

	}


});
