//Google API & Map-related client side code here
var map, GeoMarker;
var markers = [];
console.log("We made it to this file");
function initialize() {
	var mapOptions = {
	  zoom: 16,
	  center: new google.maps.LatLng(35.912586, -79.051286),	//latlang = old well
	  mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById('map_canvas'),
	    mapOptions);

	GeoMarker = new GeolocationMarker();
	GeoMarker.setCircleOptions({fillColor: '#808080'});

	// This function updates the blue dot location when the user's position changes
	google.maps.event.addListenerOnce(GeoMarker, 'position_changed', function() {
	  map.setCenter(this.getPosition());
	  map.fitBounds(this.getBounds());
	});

	// If Google maps can't find user's location, display error message
	google.maps.event.addListener(GeoMarker, 'geolocation_error', function(e) {
	  alert('There was an error obtaining your position. Message: ' + e.message);
	});

	GeoMarker.setMap(map);	// Calling setMap(obj) actually puts the object on the map

	//These lines get bed coordinates from the server side, and render them to the map
	//These lines also add beds to table in bed_view and link them to their position marker
	var serverURL = 'https://ediblecampusapi-dept-botanicalgarden.cloudapps.unc.edu/beds';
	$.ajax(serverURL, {
		type: 'GET',
		cache: false,
		headers: {
			"Authorization": "Basic " + btoa('ecuser57:ecsecret18')
		},
		success: function(data, status, jqxhr) {
			//initilize variables
			$('#bed_view').empty();
			markers = [];
			var mapZoom = 19;
			var bedTable = $('<table></table>').attr('id', 'bed_table');
			
			
			for (var i = 0; i < data.length; i++) {
				//render coordinates
				var latitude = data[i].BedLatitude;
				var longitude = data[i].BedLongitude;
				var bedName = data[i].BedName;
				var location = new google.maps.LatLng(latitude, longitude);
				var marker = new google.maps.Marker({
					id: "marker"+i,
					position: location,
					map: map,
					title: bedName
				});
				markers.push(marker);
				google.maps.event.addListener(marker, 'click', function() {
					map.setZoom(mapZoom);
					map.panTo(this.getPosition());
				});
				console.log(bedName);
				//render table
				var bedRow =  $('<tr></tr>').text(bedName).data("num",i);
				bedTable.append(bedRow);
			}
			
			//connect table and markers
			bedTable.children("tr").each(function() {
				$(this).on(
					'click',
					function() {
						var num = $(this).data("num"); // Assuming you've given it a data attribute
						for (var i = 0; i < markers.length; i++) {
							if (markers[i].id=='marker'+num) {
								map.setCenter(markers[i].position);
								map.setZoom(mapZoom);
								break;
							}
						}
					}
				);
			});
		},
		error: function(jqxhr, status, data) {
			console.log(jqxhr.reponseText);
		}
	});
}

$(document).ready(function () {
	google.maps.event.addDomListener(window, 'load', initialize);
	console.log("We made it to document ready functions");
	if(!navigator.geolocation) {
		alert('Your browser does not support geolocation');
	}
});