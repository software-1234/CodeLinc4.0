//Google API & Map-related client side code here
var map, GeoMarker;
var markers = [];
var centerPosition;
var defaultZoom;
var infowindow;


function initialize() {
	centerPosition = new google.maps.LatLng(36.072890, -79.791331)
	defaultZoom = 15;
	infowindow = new google.maps.InfoWindow();
	
	var mapOptions = {
	  zoom: defaultZoom,
	  center: centerPosition,
	  mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById('map_canvas'),
	    mapOptions);
		
	//add custom center button and bed button
	var centerControlDiv = document.createElement('div');
	var centerControl = new CenterControl(centerControlDiv, map);
	centerControlDiv.index = 1;
	map.controls[google.maps.ControlPosition.TOP_RIGHT].push(centerControlDiv);
	
	GeoMarker = new GeolocationMarker();
	GeoMarker.setCircleOptions({fillColor: '#808080'});

	// This function updates the blue dot location when the user's position changes
	google.maps.event.addListenerOnce(GeoMarker, 'position_changed', function() {
	  centerPosition = this.getPosition();
	  map.setCenter(centerPosition);
	  map.fitBounds(this.getBounds());
	});

	// If Google maps can't find user's location, display error message
	google.maps.event.addListener(GeoMarker, 'geolocation_error', function(e) {
	  alert('There was an error obtaining your position. Message: ' + e.message);
	});

	GeoMarker.setMap(map);	// Calling setMap(obj) actually puts the object on the map

	//These lines get bed coordinates from the server side, and render them to the map
	//These lines also add beds to table in bed_view and link them to their position marker
	//var serverURL = 'https://ediblecampusapi-dept-botanicalgarden.cloudapps.unc.edu/beds';
	var serverURL = 'http://localhost:5000/api/locations';
	$.ajax(serverURL, {
		type: 'GET',
		cache: false,
		headers: {
		
		},
		success: function(data, status, jqxhr) {
			//initilize variables
			markers = [];
			var mapZoom = 19;
			
			console.log(data);
			for (var i = 0; i < data.length; i++) {
				//render coordinates
				var name = data[i][0];
				var foodSystemElement = data[i][1];
				var typeOfResource = data[i][2];
				var website = data[i][3];
				var contactName = data[i][4];
				var email = data[i][5];
				var phone = data[i][6];
				var address = data[i][7];
				var city = data[i][8];
				var state = data[i][9];
				var zip = data[i][10];
				var provider = data[i][13];
				var comments = data[i][14];
				var ebt = data[i][15];
				console.log(name + ", " + typeOfResource);
				/*
				location = 
				
				var marker = new google.maps.Marker({
					id: "marker"+bedID,
					position: location,
					map: map,
					title: name
				});
				//add to marker list for referencing in click events
				markers.push(marker);

				//zoom into marker on click and open infoWindow
				google.maps.event.addListener(marker, 'click', function() {
					var num = this.id.substr(this.id.length -1);
					map.setZoom(mapZoom);
					map.panTo(this.getPosition());
					getInfoWindowEvent(marker, bedName, bedID, latitude, longitude);
				});
				/*
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
				*/
			}
		},
		error: function(jqxhr, status, data) {
			console.log(jqxhr.reponseText);
		}
	});
}


function getInfoWindowEvent(marker, bedName, bedID, latitude, longitude) {
    infowindow.close()
	infowindowContentString = '<div><p>'+ bedName +' Garden <br/><span id="link'+bedID+'" class="link">Open Information</span></p><a href="https://www.google.com/maps/?q='+latitude+','+longitude+'">Open in Google Maps</a></p><div>';
    $(document).off('click', '#link'+bedID);
    $(document).on('click', '#link'+bedID, function() {loadBed(bedID);});
    infowindow.setContent(infowindowContentString);
    infowindow.open(map, marker);
}

function CenterControl(controlDiv, map) {

	// Set CSS for the control border.
	var controlUI = document.createElement('div');
	controlUI.style.backgroundColor = '#fff';
	controlUI.style.border = '2px solid #fff';
	controlUI.style.borderRadius = '3px';
	controlUI.style.boxShadow = '0 1px 4px rgba(0,0,0,.3)';
	controlUI.style.cursor = 'pointer';
	controlUI.style.marginTop = '10px';
	controlUI.style.marginRight = '10px';
	controlUI.style.marginBottom = '22px';
	controlUI.style.textAlign = 'center';
	controlUI.title = 'Click to recenter the map';
	controlDiv.appendChild(controlUI);

	// Set CSS for the control interior.
	var controlText = document.createElement('div');
	controlText.style.color = 'rgb(25,25,25)';
	controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	controlText.style.fontSize = '11x';
	controlText.style.lineHeight = '25px';
	controlText.style.paddingLeft = '5px';
	controlText.style.paddingRight = '5px';
	controlText.innerHTML = 'Center Map';
	controlUI.appendChild(controlText);

	// Setup the click event listeners: simply set the map to Chicago.
	controlUI.addEventListener('click', function() {
		infowindow.close();
		map.panTo(centerPosition);
		map.setZoom(defaultZoom);
	});

}

$(document).ready(function () {
	google.maps.event.addDomListener(window, 'load', initialize);
	console.log("We made it to document ready functions");
	if(!navigator.geolocation) {
		alert('Your browser does not support geolocation');
	}
});