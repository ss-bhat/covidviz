$(document).ready(function(event){

   $.ajax({
    type: "GET",
    url: "/assets/data/clean_countries.geojson",
    dataType: 'json',
    success: function(data){
        var geojson = data;
        var checkExist = setInterval(function() {
            if ($('#map').length) {

                mapboxgl.accessToken = "pk.eyJ1Ijoic3dhcm9vcGJoYXQxMjMiLCJhIjoiY2s4MmZleHZiMDUyMzNlcWtudWJxNHQ4byJ9.q_M3yDIf3UCUXD8jk8nelw";
                var map = new mapboxgl.Map({
                    container: 'map',
                    style: 'mapbox://styles/mapbox/light-v10',
                    center: [52.350140, 30.266155],
                    zoom: 1.2
                });

                var hoveredStateId = null;
                var previousClickedStateId = null;

                map.on('load', function() {

                    map.addSource('countries', {
                         'type':'geojson',
                         'data':geojson
                    });
                    map.addLayer({
                        'id': 'covid',
                        'type': 'fill',
                        'source': "countries",
                        'interactive': true,
                        'layout': {},
                        'paint': {
                            // Polygon color
                            'fill-color': [
                                'case',
                                ['boolean', ['feature-state', 'clicked'], false],
                                '#ffcc00',
                                '#18607e'
                            ],
                            'fill-opacity': [
                                'case',
                                ['boolean', ['feature-state', 'hover'], false],
                                1,
                                0.6
                            ]
                        }
                    });


                    // When the user moves their mouse over the state-fill layer, we'll update the
                    // feature state for the feature under the mouse.
                    map.on('mousemove', 'covid', function(e) {
                        if (e.features.length > 0) {
                            if (hoveredStateId) {
                                map.setFeatureState(
                                { source: 'countries', id: hoveredStateId },
                                { hover: false }
                                );
                            }
                            hoveredStateId = e.features[0].id;
                            map.setFeatureState(
                                { source: 'countries', id: hoveredStateId },
                                { hover: true }
                            );
                        }
                    });

                    // When the mouse leaves the state-fill layer, update the feature state of the
                    // previously hovered feature.
                    map.on('mouseleave', 'covid', function() {
                        if (hoveredStateId) {
                            map.setFeatureState(
                                { source: 'countries', id: hoveredStateId },
                                { hover: false }
                            );
                        }
                        hoveredStateId = null;
                    });

                    // Disable scroll zoom
                    map.scrollZoom.disable();

                    // Add navigation control
                    map.addControl(new mapboxgl.NavigationControl())

                    // Full screen control
                    map.addControl(new mapboxgl.FullscreenControl())


                    // Click event
                    map.on('click', function(e) {
                          var features = map.queryRenderedFeatures(e.point)
                          if (!features.length) {
                                return;
                          }
                          var feature = features[0];
                          var country = feature['properties']['ADMIN']
                          if (feature['source'] == "countries"){
                              // Click Event

                              if (previousClickedStateId){
                                map.setFeatureState(
                                    { source: 'countries', id: previousClickedStateId },
                                    { clicked: false }
                                );
                              }

                              previousClickedStateId = feature.id;
                              map.setFeatureState(
                                { source: 'countries', id: previousClickedStateId },
                                { clicked: true }
                            );

                          }

                        });

                });
                clearInterval(checkExist);
                }
            }, 100);
            // check every 100ms
    }
});

});
