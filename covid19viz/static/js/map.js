$(document).ready(function(event){
$.ajax({
   type: "GET",
   url: "/api/v1/action/get_dash_ui_config",
   dataType: 'json',
   success: function(data){

   var config = data['result'];

   $.ajax({
    type: "GET",
    url: "/data/polygon.geojson",
    cache: false,
    dataType: 'json',
    success: function(data){

        // Marker and polygon layer data
        var polygon_layer = data['polygon_layer'];
        var marker_layer = data['marker_layer'];

        var polygon_layer_layout = {
                        'id': 'covid',
                        'type': 'fill',
                        'source': config['dash.ui.map_source'],
                        'interactive': true,
                        'layout': {},
                        'paint': {
                            // Polygon color
                            'fill-color': [
                                'case',
                                ['boolean', ['feature-state', 'clicked'], false],
                                config['dash.ui.map_polygon_click'],
                                config['dash.ui.map_polygon_color']
                            ],
                            'fill-opacity': [
                                'case',
                                ['boolean', ['feature-state', 'hover'], false],
                                1,
                                0.6
                            ]
                        }
                    };

        var marker_layer_layout = {
                        'id': 'covid2',
                        'type': 'circle',
                        'source': config['dash.ui.marker_source'],
                        'paint': {
                            // make circles larger as the user zooms from z12 to z22
                            'circle-radius': {
                            'base': 1.75,
                            'stops': [[12, 16], [22, 180]]
                        },
                        // color circles by ethnicity, using a match expression
                        // https://docs.mapbox.com/mapbox-gl-js/style-spec/#expressions-match
                        'circle-color': config['dash.ui.marker_color'],
                        'circle-opacity': 0.6,
                        'circle-stroke-color': config['dash.ui.circle_stroke_color'],
                        'circle-stroke-width': 0.3
                        }
                    };

        var zoomThreshold = 2;


        var checkExist = setInterval(function() {
            if ($(config['dash.ui.map_div_id']).length) {

                mapboxgl.accessToken = "pk.eyJ1Ijoic3dhcm9vcGJoYXQxMjMiLCJhIjoiY2s4MmZleHZiMDUyMzNlcWtudWJxNHQ4byJ9.q_M3yDIf3UCUXD8jk8nelw";
                var map = new mapboxgl.Map({
                    container: 'map',
                    style: 'mapbox://styles/mapbox/light-v10',
                    center: [52.350140, 30.266155],
                    zoom: 1.2
                });

                // Add pop up
                var popup = new mapboxgl.Popup({
                    closeButton: false,
                    closeOnClick: false
                    });

                // Disable scroll zoom
                map.scrollZoom.disable();

                // Add navigation control
                map.addControl(new mapboxgl.NavigationControl())

                // Full screen control
                map.addControl(new mapboxgl.FullscreenControl())


                // Map


                var hoveredStateId = null;
                var previousClickedStateId = null;

                map.on('load', function() {

                    // Add polygon data
                    map.addSource(config['dash.ui.map_source'], {
                         'type':'geojson',
                         'data':polygon_layer
                    });

                    // Add marker data
                     map.addSource(config['dash.ui.marker_source'], {
                                 'type':'geojson',
                                 'data':marker_layer
                            });

                    // Polygon layer as default
                    map.addLayer(polygon_layer_layout);


                    // When the user moves their mouse over the state-fill layer, we'll update the
                    // feature state for the feature under the mouse.

                    // On click for layer covid
                    map.on('mousemove', 'covid', function(e) {
                        if (e.features.length > 0) {
                            if (hoveredStateId) {
                                map.setFeatureState(
                                { source: config['dash.ui.map_source'], id: hoveredStateId },
                                { hover: false }
                                );
                            }
                            hoveredStateId = e.features[0].id;
                            map.setFeatureState(
                                { source: config['dash.ui.map_source'], id: hoveredStateId },
                                { hover: true }
                            );
                        }

                        // Add pop up on hover
                        var feature = e.features[0]
                        popup.setLngLat(e.lngLat).setHTML(feature.properties.html).addTo(map);

                    });

                    //On mouse move and mouse leave for layer covid2
                    map.on('mousemove', 'covid2', function(e) {

                        // Add pop up on hover
                        var feature = e.features[0]
                        popup.setLngLat(e.lngLat).setHTML(feature.properties.html).addTo(map);

                    });

                     map.on('mouseleave', 'covid2', function() {
                        popup.remove();
                     });

                    // When the mouse leaves the state-fill layer, update the feature state of the
                    // previously hovered feature.
                    map.on('mouseleave', 'covid', function() {
                        if (hoveredStateId) {
                            map.setFeatureState(
                                { source: config['dash.ui.map_source'], id: hoveredStateId },
                                { hover: false }
                            );
                        }
                        hoveredStateId = null;
                        // Remove pop up on mouse leave
                        popup.remove();
                    });


                    // Click event
                    map.on('click', function(e) {
                          var features = map.queryRenderedFeatures(e.point)
                          if (!features.length) {
                                return;
                          }
                          var feature = features[0];
                          var country = feature['properties']['ADMIN']
                          if (feature['source'] == config['dash.ui.map_source']){

                            // Remove pop up
                            popup.remove();
                            // Add data and layer to map
                            map.setView(e.lngLat, map.setZoom(zoomThreshold+0.1));
                            //map.addLayer(marker_layer_layout);
                            //map.removeLayer('covid');

                          }

                        });


                    // Zoom in and zoom out toggle layer based on zoom threshold
                    map.on('zoom', function() {
                        console.log(map.getLayer('covid'))
                        console.log(map.getZoom())
                        if (map.getZoom() > zoomThreshold){
                            if (map.getLayer('covid')){
                                map.removeLayer('covid');
                                map.addLayer(marker_layer_layout);
                            }
                        }

                        if (map.getZoom() < zoomThreshold){
                            if (map.getLayer('covid2')){
                                map.removeLayer('covid2');
                                map.addLayer(polygon_layer_layout);
                            }
                        }
                       });

                });
                clearInterval(checkExist);
                }
            }, 100);
            // check every 100ms
    }
  });
  }
 });
});
