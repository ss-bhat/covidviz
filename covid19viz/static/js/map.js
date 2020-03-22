$(document).ready(function(event){

   $.ajax({
    type: "GET",
    url: "/all_country_location",
    dataType: 'json',
    success: function(data){
        var geojson = data;
        var checkExist = setInterval(function() {
            if ($('#map').length) {

                mapboxgl.accessToken = "pk.eyJ1Ijoic3dhcm9vcGJoYXQxMjMiLCJhIjoiY2s4MmZleHZiMDUyMzNlcWtudWJxNHQ4byJ9.q_M3yDIf3UCUXD8jk8nelw";
                var map = new mapboxgl.Map({
                    container: 'map',
                    style: 'mapbox://styles/mapbox/light-v10',
                    center: [52.350140, -6.266155],
                    zoom: 1
                });

                map.on('load', function() {

                    map.addSource('countries', {
                         'type':'geojson',
                         'data':geojson
                    });
                    map.addLayer({
                        'id': 'example',
                        'type': 'circle',
                        'source': "countries",
                        'layout': {},
                        'paint': {
                            'circle-stroke-color': "#18607e",
                            'circle-stroke-width': 1,
                            // make circles larger as the user zooms from z12 to z22
                            'circle-color': '#18607e',
                            'circle-opacity': 0.6,
                            'circle-radius': {
                            'base': 10.75,
                            'stops': [[12, 10], [22, 180]]
                            }
                        }
                    });
                    // Disable scroll zoom
                    map.scrollZoom.disable();

                    // Add navigation control
                    map.addControl(new mapboxgl.NavigationControl())

                    // Full screen control
                    map.addControl(new mapboxgl.FullscreenControl())

                });
                clearInterval(checkExist);
                }
            }, 100);
            // check every 100ms
    }
});

});
