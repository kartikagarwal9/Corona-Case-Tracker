<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS=false; L_NO_TOUCH=false; L_DISABLE_3D=false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
    <meta name="viewport" content="width=device-width,
        initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <style>#map_750562447c2149d7a0fc2231ddd22c4c {
        position: relative;
        width: 800.0px;
        height: 500.0px;
        left: 8.0%;
        top: 2.0%;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-minimap/3.6.1/Control.MiniMap.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet-minimap/3.6.1/Control.MiniMap.css"/>
    
                <style>
                    #scroll_zoom_toggler_f468508ad57d4d2790ff982b18fcc670 {
                        position:absolute;
                        width:35px;
                        bottom:10px;
                        height:35px;
                        left:10px;
                        background-color:#fff;
                        text-align:center;
                        line-height:35px;
                        vertical-align: middle;
                        }
                </style>
            
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.fullscreen/1.4.2/Control.FullScreen.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.fullscreen/1.4.2/Control.FullScreen.min.css"/>
</head>
<body>    
    
        <h2 align="center" style="font-size:20px"><b>Coronavirus Total Confirmed Cases in World</b></h2>
        <h4 align="center" style="font-size:16px"><i>Created by</i> KARTIK AGARWAL</h4>
        <h4 align="center" style="font-size:16px"><i>Powered by</i>
            <a href="https://www.whitehatjr.com/">WhiteHat Jr</a>
        </h4>
             
    
    <div class="folium-map" id="map_750562447c2149d7a0fc2231ddd22c4c" ></div>
    
            <img id="scroll_zoom_toggler_f468508ad57d4d2790ff982b18fcc670" alt="scroll"
                 src="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/png/512/arrow-move.png"
                 style="z-index: 999999"
                 onclick="map_750562447c2149d7a0fc2231ddd22c4c.toggleScroll()">
            </img>
            
</body>
<script>    
    
    
        var bounds = null;
    

    var map_750562447c2149d7a0fc2231ddd22c4c = L.map(
        'map_750562447c2149d7a0fc2231ddd22c4c', {
        center: [0, 0],
        zoom: 4,
        maxBounds: bounds,
        layers: [],
        worldCopyJump: false,
        crs: L.CRS.EPSG3857,
        zoomControl: true,
        });


    
    var tile_layer_8bdfa9b7af3b4851a8eef436a3f4b3e3 = L.tileLayer(
        'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
        {
        "attribution": null,
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
}).addTo(map_750562447c2149d7a0fc2231ddd22c4c);
    

        var tile_layer_99ba2f307b774ac9b9c9abe75a52cb1e = L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
        "attribution": null,
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
} );

        var mini_map_391c790f464f4b52aef9207a8a0b5100 = new L.Control.MiniMap( tile_layer_99ba2f307b774ac9b9c9abe75a52cb1e,
         {
  "autoToggleDisplay": false,
  "centerFixed": false,
  "collapsedHeight": 25,
  "collapsedWidth": 25,
  "height": 150,
  "minimized": false,
  "position": "bottomright",
  "toggleDisplay": true,
  "width": 150,
  "zoomAnimation": false,
  "zoomLevelFixed": null,
  "zoomLevelOffset": -5
});
        map_750562447c2149d7a0fc2231ddd22c4c.addControl(mini_map_391c790f464f4b52aef9207a8a0b5100);

        
    
                    map_750562447c2149d7a0fc2231ddd22c4c.scrollEnabled = true;

                    map_750562447c2149d7a0fc2231ddd22c4c.toggleScroll = function() {
                        if (this.scrollEnabled) {
                            this.scrollEnabled = false;
                            this.scrollWheelZoom.disable();
                            }
                        else {
                            this.scrollEnabled = true;
                            this.scrollWheelZoom.enable();
                            }
                        };

                    map_750562447c2149d7a0fc2231ddd22c4c.toggleScroll();
            
    
            L.control.fullscreen({
                position: 'topright',
                title: 'Full Screen',
                titleCancel: 'Exit Full Screen',
                forceSeparateButton: false,
                }).addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            map_750562447c2149d7a0fc2231ddd22c4c.on('enterFullscreen', function(){
                console.log('entered fullscreen');
            });

        
    

            var circle_5d908d1a81304bf69d41dabb4b8eb2dd = L.circle(
                [33.93911, 67.709953],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 19035.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_96703f0e5889458b94b08f8774275217 = L.popup({maxWidth: '100%'
            
            });

            
                var html_15db59917ba5446ea9b946e1a4172996 = $(`<div id="html_15db59917ba5446ea9b946e1a4172996" style="width: 100.0%; height: 100.0%;">Afghanistan  38070  on 8/25/20</div>`)[0];
                popup_96703f0e5889458b94b08f8774275217.setContent(html_15db59917ba5446ea9b946e1a4172996);
            

            circle_5d908d1a81304bf69d41dabb4b8eb2dd.bindPopup(popup_96703f0e5889458b94b08f8774275217)
            ;

            
        
    

            var circle_b3d0216996514efeb8f542ba9518ff97 = L.circle(
                [41.1533, 20.1683],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4379.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_75b5c00f88264138b820b77938eb90df = L.popup({maxWidth: '100%'
            
            });

            
                var html_934b4b9736004cc0bf77f3b91939fa87 = $(`<div id="html_934b4b9736004cc0bf77f3b91939fa87" style="width: 100.0%; height: 100.0%;">Albania  8759  on 8/25/20</div>`)[0];
                popup_75b5c00f88264138b820b77938eb90df.setContent(html_934b4b9736004cc0bf77f3b91939fa87);
            

            circle_b3d0216996514efeb8f542ba9518ff97.bindPopup(popup_75b5c00f88264138b820b77938eb90df)
            ;

            
        
    

            var circle_0a4b707062e2447590bf2a9d040fdd76 = L.circle(
                [28.0339, 1.6596],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 21114.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_835b477610ff49a390dd9717991ab0bf = L.popup({maxWidth: '100%'
            
            });

            
                var html_fdb1dbc02f4a478584c9dfcde5143d12 = $(`<div id="html_fdb1dbc02f4a478584c9dfcde5143d12" style="width: 100.0%; height: 100.0%;">Algeria  42228  on 8/25/20</div>`)[0];
                popup_835b477610ff49a390dd9717991ab0bf.setContent(html_fdb1dbc02f4a478584c9dfcde5143d12);
            

            circle_0a4b707062e2447590bf2a9d040fdd76.bindPopup(popup_835b477610ff49a390dd9717991ab0bf)
            ;

            
        
    

            var circle_59aa647264614febab71ba33a96fe536 = L.circle(
                [42.5063, 1.5218],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 530.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2b42e38e822445e392bdea43766aed3b = L.popup({maxWidth: '100%'
            
            });

            
                var html_880f9b36279d4d819895743a15aaa0e4 = $(`<div id="html_880f9b36279d4d819895743a15aaa0e4" style="width: 100.0%; height: 100.0%;">Andorra  1060  on 8/25/20</div>`)[0];
                popup_2b42e38e822445e392bdea43766aed3b.setContent(html_880f9b36279d4d819895743a15aaa0e4);
            

            circle_59aa647264614febab71ba33a96fe536.bindPopup(popup_2b42e38e822445e392bdea43766aed3b)
            ;

            
        
    

            var circle_cb82364d5f5e4592bc18eaf61d3d2776 = L.circle(
                [-11.2027, 17.8739],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1141.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_07bd284c68824f978b76f6ec035c3830 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bb6b802457a64ae0a42f5e5de26d788c = $(`<div id="html_bb6b802457a64ae0a42f5e5de26d788c" style="width: 100.0%; height: 100.0%;">Angola  2283  on 8/25/20</div>`)[0];
                popup_07bd284c68824f978b76f6ec035c3830.setContent(html_bb6b802457a64ae0a42f5e5de26d788c);
            

            circle_cb82364d5f5e4592bc18eaf61d3d2776.bindPopup(popup_07bd284c68824f978b76f6ec035c3830)
            ;

            
        
    

            var circle_8cdbe91f002343178c048029e0a9adf7 = L.circle(
                [17.0608, -61.7964],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 47.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_68119e75458f4057b348d5211387ebc9 = L.popup({maxWidth: '100%'
            
            });

            
                var html_6eacb3f98b254430a8170f286612ce29 = $(`<div id="html_6eacb3f98b254430a8170f286612ce29" style="width: 100.0%; height: 100.0%;">Antigua and Barbuda  94  on 8/25/20</div>`)[0];
                popup_68119e75458f4057b348d5211387ebc9.setContent(html_6eacb3f98b254430a8170f286612ce29);
            

            circle_8cdbe91f002343178c048029e0a9adf7.bindPopup(popup_68119e75458f4057b348d5211387ebc9)
            ;

            
        
    

            var circle_d30d3fdd3ae34b81809642c562b21031 = L.circle(
                [-38.4161, -63.6167],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 179819.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ad504ae02f1b4d5da5c6df8bfd35aa5a = L.popup({maxWidth: '100%'
            
            });

            
                var html_e68406d246c840b1954f68be3264b8a9 = $(`<div id="html_e68406d246c840b1954f68be3264b8a9" style="width: 100.0%; height: 100.0%;">Argentina  359638  on 8/25/20</div>`)[0];
                popup_ad504ae02f1b4d5da5c6df8bfd35aa5a.setContent(html_e68406d246c840b1954f68be3264b8a9);
            

            circle_d30d3fdd3ae34b81809642c562b21031.bindPopup(popup_ad504ae02f1b4d5da5c6df8bfd35aa5a)
            ;

            
        
    

            var circle_fee0c122688b4ba8aa7147cad47018f0 = L.circle(
                [40.0691, 45.0382],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 21468.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a19437ebe8544a27a48572a29caf6558 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ff04b5fef91e437a8a952393aab4acc7 = $(`<div id="html_ff04b5fef91e437a8a952393aab4acc7" style="width: 100.0%; height: 100.0%;">Armenia  42936  on 8/25/20</div>`)[0];
                popup_a19437ebe8544a27a48572a29caf6558.setContent(html_ff04b5fef91e437a8a952393aab4acc7);
            

            circle_fee0c122688b4ba8aa7147cad47018f0.bindPopup(popup_a19437ebe8544a27a48572a29caf6558)
            ;

            
        
    

            var circle_9a3fac6bb7724e13aee0eeef9d2d1ffd = L.circle(
                [-256.85020000000003, 1130.8438999999998],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 12602.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_6b5771e9e2a14074810b696d1e46a7a0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d72c51d5a91c496ba5f4faf07aeeec63 = $(`<div id="html_d72c51d5a91c496ba5f4faf07aeeec63" style="width: 100.0%; height: 100.0%;">Australia  25204  on 8/25/20</div>`)[0];
                popup_6b5771e9e2a14074810b696d1e46a7a0.setContent(html_d72c51d5a91c496ba5f4faf07aeeec63);
            

            circle_9a3fac6bb7724e13aee0eeef9d2d1ffd.bindPopup(popup_6b5771e9e2a14074810b696d1e46a7a0)
            ;

            
        
    

            var circle_6237d8f7321949708dca5fdccd7d0ee4 = L.circle(
                [47.5162, 14.5501],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 12853.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cb8423c5a6d74d90bd36f66df48e9230 = L.popup({maxWidth: '100%'
            
            });

            
                var html_e31350abd3164664bd4efada70f2b0d6 = $(`<div id="html_e31350abd3164664bd4efada70f2b0d6" style="width: 100.0%; height: 100.0%;">Austria  25706  on 8/25/20</div>`)[0];
                popup_cb8423c5a6d74d90bd36f66df48e9230.setContent(html_e31350abd3164664bd4efada70f2b0d6);
            

            circle_6237d8f7321949708dca5fdccd7d0ee4.bindPopup(popup_cb8423c5a6d74d90bd36f66df48e9230)
            ;

            
        
    

            var circle_e21be324cefe4ce68094920d302fbb04 = L.circle(
                [40.1431, 47.5769],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 17779.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b5e2fda44181479294055d07c3967ced = L.popup({maxWidth: '100%'
            
            });

            
                var html_d092e441d70d4e208ee16b11fea2aaa5 = $(`<div id="html_d092e441d70d4e208ee16b11fea2aaa5" style="width: 100.0%; height: 100.0%;">Azerbaijan  35559  on 8/25/20</div>`)[0];
                popup_b5e2fda44181479294055d07c3967ced.setContent(html_d092e441d70d4e208ee16b11fea2aaa5);
            

            circle_e21be324cefe4ce68094920d302fbb04.bindPopup(popup_b5e2fda44181479294055d07c3967ced)
            ;

            
        
    

            var circle_d64c5e34f50e45fcbb720f7713852ded = L.circle(
                [25.025885, -78.035889],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 882.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cb55915337f343f08cecbe81f221a928 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bdc4694f618e4009b5560a4e6fca8fbb = $(`<div id="html_bdc4694f618e4009b5560a4e6fca8fbb" style="width: 100.0%; height: 100.0%;">Bahamas  1765  on 8/25/20</div>`)[0];
                popup_cb55915337f343f08cecbe81f221a928.setContent(html_bdc4694f618e4009b5560a4e6fca8fbb);
            

            circle_d64c5e34f50e45fcbb720f7713852ded.bindPopup(popup_cb55915337f343f08cecbe81f221a928)
            ;

            
        
    

            var circle_78c43dad180b405e8fe1345d5485eb1c = L.circle(
                [26.0275, 50.55],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 25038.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_bcc7d027dc8f4f2bae41306e9b0edeee = L.popup({maxWidth: '100%'
            
            });

            
                var html_2a8ac10a43a54a87bb34a4a902998866 = $(`<div id="html_2a8ac10a43a54a87bb34a4a902998866" style="width: 100.0%; height: 100.0%;">Bahrain  50076  on 8/25/20</div>`)[0];
                popup_bcc7d027dc8f4f2bae41306e9b0edeee.setContent(html_2a8ac10a43a54a87bb34a4a902998866);
            

            circle_78c43dad180b405e8fe1345d5485eb1c.bindPopup(popup_bcc7d027dc8f4f2bae41306e9b0edeee)
            ;

            
        
    

            var circle_2b340286c13243fd9cf46fbf9717bdbc = L.circle(
                [23.685, 90.3563],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 149814.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4aadede51b3f40f18209730acd1427e1 = L.popup({maxWidth: '100%'
            
            });

            
                var html_5475226a4ace4be59ca294995f6f5cfc = $(`<div id="html_5475226a4ace4be59ca294995f6f5cfc" style="width: 100.0%; height: 100.0%;">Bangladesh  299628  on 8/25/20</div>`)[0];
                popup_4aadede51b3f40f18209730acd1427e1.setContent(html_5475226a4ace4be59ca294995f6f5cfc);
            

            circle_2b340286c13243fd9cf46fbf9717bdbc.bindPopup(popup_4aadede51b3f40f18209730acd1427e1)
            ;

            
        
    

            var circle_d9ef7ff0c53a4a96a223c92c9dc404f3 = L.circle(
                [13.1939, -59.5432],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 82.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ca83763f88d44d2bb65145f3477b30c8 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9232c6923e7049f592597b2463be8b7c = $(`<div id="html_9232c6923e7049f592597b2463be8b7c" style="width: 100.0%; height: 100.0%;">Barbados  164  on 8/25/20</div>`)[0];
                popup_ca83763f88d44d2bb65145f3477b30c8.setContent(html_9232c6923e7049f592597b2463be8b7c);
            

            circle_d9ef7ff0c53a4a96a223c92c9dc404f3.bindPopup(popup_ca83763f88d44d2bb65145f3477b30c8)
            ;

            
        
    

            var circle_902b35a2064a4d11a4a70880ca923aeb = L.circle(
                [53.7098, 27.9534],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 35363.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_aaf70af3584e4678899d7e7251803c65 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ff358b56b19a4489adfc650254a28608 = $(`<div id="html_ff358b56b19a4489adfc650254a28608" style="width: 100.0%; height: 100.0%;">Belarus  70727  on 8/25/20</div>`)[0];
                popup_aaf70af3584e4678899d7e7251803c65.setContent(html_ff358b56b19a4489adfc650254a28608);
            

            circle_902b35a2064a4d11a4a70880ca923aeb.bindPopup(popup_aaf70af3584e4678899d7e7251803c65)
            ;

            
        
    

            var circle_17c9ee89dd3e4765a81bfb89080817ea = L.circle(
                [50.8333, 4.469936],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 41223.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_09e956a145ad4cf5a738e0f2cdfca463 = L.popup({maxWidth: '100%'
            
            });

            
                var html_65a3e64e520647fdaead092b0624eebf = $(`<div id="html_65a3e64e520647fdaead092b0624eebf" style="width: 100.0%; height: 100.0%;">Belgium  82447  on 8/25/20</div>`)[0];
                popup_09e956a145ad4cf5a738e0f2cdfca463.setContent(html_65a3e64e520647fdaead092b0624eebf);
            

            circle_17c9ee89dd3e4765a81bfb89080817ea.bindPopup(popup_09e956a145ad4cf5a738e0f2cdfca463)
            ;

            
        
    

            var circle_3d7038dca1b74aeca7f88ff956bc26f3 = L.circle(
                [17.1899, -88.4976],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 365.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7fedb05490364f3fa087adf9abf6bc13 = L.popup({maxWidth: '100%'
            
            });

            
                var html_09eac50d5faf49798c5b434f0d11830e = $(`<div id="html_09eac50d5faf49798c5b434f0d11830e" style="width: 100.0%; height: 100.0%;">Belize  730  on 8/25/20</div>`)[0];
                popup_7fedb05490364f3fa087adf9abf6bc13.setContent(html_09eac50d5faf49798c5b434f0d11830e);
            

            circle_3d7038dca1b74aeca7f88ff956bc26f3.bindPopup(popup_7fedb05490364f3fa087adf9abf6bc13)
            ;

            
        
    

            var circle_139c5ccfdf4047d78ddd32d079169b3a = L.circle(
                [9.3077, 2.3158],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1057.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_5ae76ff501bc4c2e81bc1c95774f35b2 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9f6bb43c32284de19cc6428c063df312 = $(`<div id="html_9f6bb43c32284de19cc6428c063df312" style="width: 100.0%; height: 100.0%;">Benin  2115  on 8/25/20</div>`)[0];
                popup_5ae76ff501bc4c2e81bc1c95774f35b2.setContent(html_9f6bb43c32284de19cc6428c063df312);
            

            circle_139c5ccfdf4047d78ddd32d079169b3a.bindPopup(popup_5ae76ff501bc4c2e81bc1c95774f35b2)
            ;

            
        
    

            var circle_393e2d4f666846fca3f06a046bbf4c61 = L.circle(
                [27.5142, 90.4336],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 86.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_08f9be79d1e24c5d959f949f124f2b51 = L.popup({maxWidth: '100%'
            
            });

            
                var html_487d2f83adc94f66ae308ce740b044ab = $(`<div id="html_487d2f83adc94f66ae308ce740b044ab" style="width: 100.0%; height: 100.0%;">Bhutan  173  on 8/25/20</div>`)[0];
                popup_08f9be79d1e24c5d959f949f124f2b51.setContent(html_487d2f83adc94f66ae308ce740b044ab);
            

            circle_393e2d4f666846fca3f06a046bbf4c61.bindPopup(popup_08f9be79d1e24c5d959f949f124f2b51)
            ;

            
        
    

            var circle_e2f5900dd4924a75909c9c9698b15237 = L.circle(
                [-16.2902, -63.5887],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 55499.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2e99b582cb804268a411759c82973edc = L.popup({maxWidth: '100%'
            
            });

            
                var html_b032027f0228410894bc85e195dc4d92 = $(`<div id="html_b032027f0228410894bc85e195dc4d92" style="width: 100.0%; height: 100.0%;">Bolivia  110999  on 8/25/20</div>`)[0];
                popup_2e99b582cb804268a411759c82973edc.setContent(html_b032027f0228410894bc85e195dc4d92);
            

            circle_e2f5900dd4924a75909c9c9698b15237.bindPopup(popup_2e99b582cb804268a411759c82973edc)
            ;

            
        
    

            var circle_34249530376a4a658b4675743a87391b = L.circle(
                [43.9159, 17.6791],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 9163.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3f99ead9e01c4e16af49a0970742294c = L.popup({maxWidth: '100%'
            
            });

            
                var html_49fc0f93d6b2487a92c3c902f2960176 = $(`<div id="html_49fc0f93d6b2487a92c3c902f2960176" style="width: 100.0%; height: 100.0%;">Bosnia and Herzegovina  18326  on 8/25/20</div>`)[0];
                popup_3f99ead9e01c4e16af49a0970742294c.setContent(html_49fc0f93d6b2487a92c3c902f2960176);
            

            circle_34249530376a4a658b4675743a87391b.bindPopup(popup_3f99ead9e01c4e16af49a0970742294c)
            ;

            
        
    

            var circle_7b6697a23a724734a2a2ff04a2f4cd15 = L.circle(
                [-22.3285, 24.6849],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 781.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f7f3b81481c34de3b934101e09d5e4b4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d1aaa309ea104e7fbb7d02dbf7427fcf = $(`<div id="html_d1aaa309ea104e7fbb7d02dbf7427fcf" style="width: 100.0%; height: 100.0%;">Botswana  1562  on 8/25/20</div>`)[0];
                popup_f7f3b81481c34de3b934101e09d5e4b4.setContent(html_d1aaa309ea104e7fbb7d02dbf7427fcf);
            

            circle_7b6697a23a724734a2a2ff04a2f4cd15.bindPopup(popup_f7f3b81481c34de3b934101e09d5e4b4)
            ;

            
        
    

            var circle_0914418308ba469a88e471248c4c4c6b = L.circle(
                [-14.235, -51.9253],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1834997.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a72405776f064eb8a976c9a56dcd3212 = L.popup({maxWidth: '100%'
            
            });

            
                var html_61329de12a144a82852b662c191ecb50 = $(`<div id="html_61329de12a144a82852b662c191ecb50" style="width: 100.0%; height: 100.0%;">Brazil  3669995  on 8/25/20</div>`)[0];
                popup_a72405776f064eb8a976c9a56dcd3212.setContent(html_61329de12a144a82852b662c191ecb50);
            

            circle_0914418308ba469a88e471248c4c4c6b.bindPopup(popup_a72405776f064eb8a976c9a56dcd3212)
            ;

            
        
    

            var circle_9d7d35442892482ab04087844bc0b045 = L.circle(
                [4.5353, 114.7277],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 72.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b6e9614209094977ba45bcbdf6c31e00 = L.popup({maxWidth: '100%'
            
            });

            
                var html_78c46aa444284d3aa4525576fe3be28c = $(`<div id="html_78c46aa444284d3aa4525576fe3be28c" style="width: 100.0%; height: 100.0%;">Brunei  144  on 8/25/20</div>`)[0];
                popup_b6e9614209094977ba45bcbdf6c31e00.setContent(html_78c46aa444284d3aa4525576fe3be28c);
            

            circle_9d7d35442892482ab04087844bc0b045.bindPopup(popup_b6e9614209094977ba45bcbdf6c31e00)
            ;

            
        
    

            var circle_dccaf804c6dc46ffa5200a44928e39a8 = L.circle(
                [42.7339, 25.4858],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 7794.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_1621d76638d54ee185ac84efea6a314b = L.popup({maxWidth: '100%'
            
            });

            
                var html_30aaa19d3be940e783ed44402a5acf34 = $(`<div id="html_30aaa19d3be940e783ed44402a5acf34" style="width: 100.0%; height: 100.0%;">Bulgaria  15589  on 8/25/20</div>`)[0];
                popup_1621d76638d54ee185ac84efea6a314b.setContent(html_30aaa19d3be940e783ed44402a5acf34);
            

            circle_dccaf804c6dc46ffa5200a44928e39a8.bindPopup(popup_1621d76638d54ee185ac84efea6a314b)
            ;

            
        
    

            var circle_75744056ad164f418e4f467b72abc4f0 = L.circle(
                [12.2383, -1.5616],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 669.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ca2dd3e4cda34c889de07ad017f5c6d9 = L.popup({maxWidth: '100%'
            
            });

            
                var html_312c489747e040c88fa15e34874d3684 = $(`<div id="html_312c489747e040c88fa15e34874d3684" style="width: 100.0%; height: 100.0%;">Burkina Faso  1338  on 8/25/20</div>`)[0];
                popup_ca2dd3e4cda34c889de07ad017f5c6d9.setContent(html_312c489747e040c88fa15e34874d3684);
            

            circle_75744056ad164f418e4f467b72abc4f0.bindPopup(popup_ca2dd3e4cda34c889de07ad017f5c6d9)
            ;

            
        
    

            var circle_eb6a5fb4bfa748159476793fe954b368 = L.circle(
                [21.9162, 95.956],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 252.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_015f5acee0894965b5448956f4f10338 = L.popup({maxWidth: '100%'
            
            });

            
                var html_b33f198973de490ea737374eb926e390 = $(`<div id="html_b33f198973de490ea737374eb926e390" style="width: 100.0%; height: 100.0%;">Burma  504  on 8/25/20</div>`)[0];
                popup_015f5acee0894965b5448956f4f10338.setContent(html_b33f198973de490ea737374eb926e390);
            

            circle_eb6a5fb4bfa748159476793fe954b368.bindPopup(popup_015f5acee0894965b5448956f4f10338)
            ;

            
        
    

            var circle_3f1d52e5c9c541ed94b36e6ab3669217 = L.circle(
                [-3.3731, 29.9189],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 215.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a62a2e0c723d4bfb8d329612ba6e0a87 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bc3739e1d54c488f88a77f77bd4dfb10 = $(`<div id="html_bc3739e1d54c488f88a77f77bd4dfb10" style="width: 100.0%; height: 100.0%;">Burundi  430  on 8/25/20</div>`)[0];
                popup_a62a2e0c723d4bfb8d329612ba6e0a87.setContent(html_bc3739e1d54c488f88a77f77bd4dfb10);
            

            circle_3f1d52e5c9c541ed94b36e6ab3669217.bindPopup(popup_a62a2e0c723d4bfb8d329612ba6e0a87)
            ;

            
        
    

            var circle_27b671f1901c4292bfd946cd65fa214b = L.circle(
                [16.5388, -23.0418],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1784.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cb9bc331f8d2410999c59f4683b6421a = L.popup({maxWidth: '100%'
            
            });

            
                var html_af33c1ee88c9464a947914855a0566b6 = $(`<div id="html_af33c1ee88c9464a947914855a0566b6" style="width: 100.0%; height: 100.0%;">Cabo Verde  3568  on 8/25/20</div>`)[0];
                popup_cb9bc331f8d2410999c59f4683b6421a.setContent(html_af33c1ee88c9464a947914855a0566b6);
            

            circle_27b671f1901c4292bfd946cd65fa214b.bindPopup(popup_cb9bc331f8d2410999c59f4683b6421a)
            ;

            
        
    

            var circle_f7322eb12c0e471594a5be47c1e35881 = L.circle(
                [11.55, 104.9167],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 136.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0dd4cb7b95434aeaa5b347c246cd7c30 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ec1fdafa51e74547892436a9a24af958 = $(`<div id="html_ec1fdafa51e74547892436a9a24af958" style="width: 100.0%; height: 100.0%;">Cambodia  273  on 8/25/20</div>`)[0];
                popup_0dd4cb7b95434aeaa5b347c246cd7c30.setContent(html_ec1fdafa51e74547892436a9a24af958);
            

            circle_f7322eb12c0e471594a5be47c1e35881.bindPopup(popup_0dd4cb7b95434aeaa5b347c246cd7c30)
            ;

            
        
    

            var circle_e150db616240466292d5ece0f328df01 = L.circle(
                [3.848, 11.5021],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 9486.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f722664c28ea42f7ae0f9d2ff806ef43 = L.popup({maxWidth: '100%'
            
            });

            
                var html_4f28990b2cdf418289f56132ddfa63ae = $(`<div id="html_4f28990b2cdf418289f56132ddfa63ae" style="width: 100.0%; height: 100.0%;">Cameroon  18973  on 8/25/20</div>`)[0];
                popup_f722664c28ea42f7ae0f9d2ff806ef43.setContent(html_4f28990b2cdf418289f56132ddfa63ae);
            

            circle_e150db616240466292d5ece0f328df01.bindPopup(popup_f722664c28ea42f7ae0f9d2ff806ef43)
            ;

            
        
    

            var circle_0e2de842fa194bca9dd89bd5a070790e = L.circle(
                [638.5557999999999, -1119.4903],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 63951.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_651692da04ba4a5a898161eb9ef3fa86 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f5bebb3593834ebd8f06f2b39a65d492 = $(`<div id="html_f5bebb3593834ebd8f06f2b39a65d492" style="width: 100.0%; height: 100.0%;">Canada  127903  on 8/25/20</div>`)[0];
                popup_651692da04ba4a5a898161eb9ef3fa86.setContent(html_f5bebb3593834ebd8f06f2b39a65d492);
            

            circle_0e2de842fa194bca9dd89bd5a070790e.bindPopup(popup_651692da04ba4a5a898161eb9ef3fa86)
            ;

            
        
    

            var circle_8ef56e0849074ab3939934b39e50ca3d = L.circle(
                [6.6111, 20.9394],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2345.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a2599de3e3914fdd930f6bed8533ebc7 = L.popup({maxWidth: '100%'
            
            });

            
                var html_eb2e66de328e4ceebc4913324d5f6fa9 = $(`<div id="html_eb2e66de328e4ceebc4913324d5f6fa9" style="width: 100.0%; height: 100.0%;">Central African Republic  4691  on 8/25/20</div>`)[0];
                popup_a2599de3e3914fdd930f6bed8533ebc7.setContent(html_eb2e66de328e4ceebc4913324d5f6fa9);
            

            circle_8ef56e0849074ab3939934b39e50ca3d.bindPopup(popup_a2599de3e3914fdd930f6bed8533ebc7)
            ;

            
        
    

            var circle_d83c397904ee40e99545d3b3bba319c4 = L.circle(
                [15.4542, 18.7322],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 497.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4b82ddaf312e4b4e9fc6778bb06b1a59 = L.popup({maxWidth: '100%'
            
            });

            
                var html_3d8e597a301c484f8f8d9607fcc056e0 = $(`<div id="html_3d8e597a301c484f8f8d9607fcc056e0" style="width: 100.0%; height: 100.0%;">Chad  995  on 8/25/20</div>`)[0];
                popup_4b82ddaf312e4b4e9fc6778bb06b1a59.setContent(html_3d8e597a301c484f8f8d9607fcc056e0);
            

            circle_d83c397904ee40e99545d3b3bba319c4.bindPopup(popup_4b82ddaf312e4b4e9fc6778bb06b1a59)
            ;

            
        
    

            var circle_aa1fd04338e04596b0ecc5fc9f87c4f0 = L.circle(
                [-35.6751, -71.543],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 200492.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8c6e544343624543815b7dbfe41f0319 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c1eca52a42fa47caa9f101dc5ac3a1f0 = $(`<div id="html_c1eca52a42fa47caa9f101dc5ac3a1f0" style="width: 100.0%; height: 100.0%;">Chile  400985  on 8/25/20</div>`)[0];
                popup_8c6e544343624543815b7dbfe41f0319.setContent(html_c1eca52a42fa47caa9f101dc5ac3a1f0);
            

            circle_aa1fd04338e04596b0ecc5fc9f87c4f0.bindPopup(popup_8c6e544343624543815b7dbfe41f0319)
            ;

            
        
    

            var circle_330b6713e81c433f8b9ac1933561eab1 = L.circle(
                [1085.2923, 3688.937700000001],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 44876.0,
  "stroke": true,
  "weight": 3                    
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_d860d940784a4bd3bcb3d64d3cc8c6d3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c365a755a36c44a78ed567c4b0bdd47e = $(`<div id="html_c365a755a36c44a78ed567c4b0bdd47e" style="width: 100.0%; height: 100.0%;">China  89752  on 8/25/20</div>`)[0];
                popup_d860d940784a4bd3bcb3d64d3cc8c6d3.setContent(html_c365a755a36c44a78ed567c4b0bdd47e);
            

            circle_330b6713e81c433f8b9ac1933561eab1.bindPopup(popup_d860d940784a4bd3bcb3d64d3cc8c6d3)
            ;

            
        
    

            var circle_fb24c8bcb96b49b5b3aaa6d2c8c20ca4 = L.circle(
                [4.5709, -74.2973],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 281056.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_d5e53d99ae4e403c99816a6f523efe1c = L.popup({maxWidth: '100%'
            
            });

            
                var html_c1ca79a9e46941ca86296564772ddfe7 = $(`<div id="html_c1ca79a9e46941ca86296564772ddfe7" style="width: 100.0%; height: 100.0%;">Colombia  562113  on 8/25/20</div>`)[0];
                popup_d5e53d99ae4e403c99816a6f523efe1c.setContent(html_c1ca79a9e46941ca86296564772ddfe7);
            

            circle_fb24c8bcb96b49b5b3aaa6d2c8c20ca4.bindPopup(popup_d5e53d99ae4e403c99816a6f523efe1c)
            ;

            
        
    

            var circle_fe52a95d565044dfad56ad2980f04f47 = L.circle(
                [-11.6455, 43.3333],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 208.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_5a9267d8ab6247a2a14d8bb66f42ace5 = L.popup({maxWidth: '100%'
            
            });

            
                var html_af0e1574d186481c8d435eb7b61d7787 = $(`<div id="html_af0e1574d186481c8d435eb7b61d7787" style="width: 100.0%; height: 100.0%;">Comoros  417  on 8/25/20</div>`)[0];
                popup_5a9267d8ab6247a2a14d8bb66f42ace5.setContent(html_af0e1574d186481c8d435eb7b61d7787);
            

            circle_fe52a95d565044dfad56ad2980f04f47.bindPopup(popup_5a9267d8ab6247a2a14d8bb66f42ace5)
            ;

            
        
    

            var circle_a142023a07be4d18a6cf474ce4c70047 = L.circle(
                [-0.228, 15.8277],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1989.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_631fdff91b094159a8b4fbe235815b0c = L.popup({maxWidth: '100%'
            
            });

            
                var html_5dc16a053d1d4351a631f6742e3f6389 = $(`<div id="html_5dc16a053d1d4351a631f6742e3f6389" style="width: 100.0%; height: 100.0%;">Congo (Brazzaville)  3979  on 8/25/20</div>`)[0];
                popup_631fdff91b094159a8b4fbe235815b0c.setContent(html_5dc16a053d1d4351a631f6742e3f6389);
            

            circle_a142023a07be4d18a6cf474ce4c70047.bindPopup(popup_631fdff91b094159a8b4fbe235815b0c)
            ;

            
        
    

            var circle_c3a885fc2cec4233a42a62d06fd5c867 = L.circle(
                [-4.0383, 21.7587],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4945.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0a75c1a7c85b477d8c7bfab9c9682a0a = L.popup({maxWidth: '100%'
            
            });

            
                var html_f4abc215fa1d4fb5801bb87ed26541f4 = $(`<div id="html_f4abc215fa1d4fb5801bb87ed26541f4" style="width: 100.0%; height: 100.0%;">Congo (Kinshasa)  9891  on 8/25/20</div>`)[0];
                popup_0a75c1a7c85b477d8c7bfab9c9682a0a.setContent(html_f4abc215fa1d4fb5801bb87ed26541f4);
            

            circle_c3a885fc2cec4233a42a62d06fd5c867.bindPopup(popup_0a75c1a7c85b477d8c7bfab9c9682a0a)
            ;

            
        
    

            var circle_a6bcf4dd531f4204ac34b363fbf03bb9 = L.circle(
                [9.7489, -83.7534],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 17652.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e7b5ae6209e34c8d9c2c4b8e2302e69f = L.popup({maxWidth: '100%'
            
            });

            
                var html_181ff8e619a4457b969c2ce599eef85e = $(`<div id="html_181ff8e619a4457b969c2ce599eef85e" style="width: 100.0%; height: 100.0%;">Costa Rica  35305  on 8/25/20</div>`)[0];
                popup_e7b5ae6209e34c8d9c2c4b8e2302e69f.setContent(html_181ff8e619a4457b969c2ce599eef85e);
            

            circle_a6bcf4dd531f4204ac34b363fbf03bb9.bindPopup(popup_e7b5ae6209e34c8d9c2c4b8e2302e69f)
            ;

            
        
    

            var circle_edc15be2c1e44bb28e4a469a5f2698f3 = L.circle(
                [7.54, -5.5471],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 8781.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_644ec25988d344e88431958387b079e4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_454febee13d448a8b960e254210a6f9a = $(`<div id="html_454febee13d448a8b960e254210a6f9a" style="width: 100.0%; height: 100.0%;">Cote d'Ivoire  17562  on 8/25/20</div>`)[0];
                popup_644ec25988d344e88431958387b079e4.setContent(html_454febee13d448a8b960e254210a6f9a);
            

            circle_edc15be2c1e44bb28e4a469a5f2698f3.bindPopup(popup_644ec25988d344e88431958387b079e4)
            ;

            
        
    

            var circle_d1e7d16a74c94ccc9164878f1a9cc3fc = L.circle(
                [45.1, 15.2],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4265.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_da14bc7843fd4d1e9271613c12040e64 = L.popup({maxWidth: '100%'
            
            });

            
                var html_0b6ce671a2684db4af0cb18552fcacd0 = $(`<div id="html_0b6ce671a2684db4af0cb18552fcacd0" style="width: 100.0%; height: 100.0%;">Croatia  8530  on 8/25/20</div>`)[0];
                popup_da14bc7843fd4d1e9271613c12040e64.setContent(html_0b6ce671a2684db4af0cb18552fcacd0);
            

            circle_d1e7d16a74c94ccc9164878f1a9cc3fc.bindPopup(popup_da14bc7843fd4d1e9271613c12040e64)
            ;

            
        
    

            var circle_ca67dbd3cff348d497904ea9e3ce1bf3 = L.circle(
                [21.521757, -77.78116700000002],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1872.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3fa95ba2bf554927b8e1937e6f46092c = L.popup({maxWidth: '100%'
            
            });

            
                var html_65ee3a90949a4a7b9e94b253adb100aa = $(`<div id="html_65ee3a90949a4a7b9e94b253adb100aa" style="width: 100.0%; height: 100.0%;">Cuba  3744  on 8/25/20</div>`)[0];
                popup_3fa95ba2bf554927b8e1937e6f46092c.setContent(html_65ee3a90949a4a7b9e94b253adb100aa);
            

            circle_ca67dbd3cff348d497904ea9e3ce1bf3.bindPopup(popup_3fa95ba2bf554927b8e1937e6f46092c)
            ;

            
        
    

            var circle_688e1d7013d046a7b85215158b68b7e2 = L.circle(
                [35.1264, 33.4299],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 737.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_09772c15f33f458394aa8c9719450cff = L.popup({maxWidth: '100%'
            
            });

            
                var html_32a851df049647b0b5c07af6174bb0be = $(`<div id="html_32a851df049647b0b5c07af6174bb0be" style="width: 100.0%; height: 100.0%;">Cyprus  1474  on 8/25/20</div>`)[0];
                popup_09772c15f33f458394aa8c9719450cff.setContent(html_32a851df049647b0b5c07af6174bb0be);
            

            circle_688e1d7013d046a7b85215158b68b7e2.bindPopup(popup_09772c15f33f458394aa8c9719450cff)
            ;

            
        
    

            var circle_4747a8cf896d40859e76cb023a16e164 = L.circle(
                [49.8175, 15.473],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 11274.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_093a3ade03eb456dbd1b41b6eb76b693 = L.popup({maxWidth: '100%'
            
            });

            
                var html_95c0e434654e45c9bd8416856df90612 = $(`<div id="html_95c0e434654e45c9bd8416856df90612" style="width: 100.0%; height: 100.0%;">Czechia  22548  on 8/25/20</div>`)[0];
                popup_093a3ade03eb456dbd1b41b6eb76b693.setContent(html_95c0e434654e45c9bd8416856df90612);
            

            circle_4747a8cf896d40859e76cb023a16e164.bindPopup(popup_093a3ade03eb456dbd1b41b6eb76b693)
            ;

            
        
    

            var circle_f8dbd7fdb3134ad186181af30c3ecead = L.circle(
                [189.8634, -40.014300000000006],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 8452.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7a822ff1ed4242f98e4b7248a80e1948 = L.popup({maxWidth: '100%'
            
            });

            
                var html_fa8f10c8731a4120811906b217665e4e = $(`<div id="html_fa8f10c8731a4120811906b217665e4e" style="width: 100.0%; height: 100.0%;">Denmark  16905  on 8/25/20</div>`)[0];
                popup_7a822ff1ed4242f98e4b7248a80e1948.setContent(html_fa8f10c8731a4120811906b217665e4e);
            

            circle_f8dbd7fdb3134ad186181af30c3ecead.bindPopup(popup_7a822ff1ed4242f98e4b7248a80e1948)
            ;

            
        
    

            var circle_844ec8a08fda4ac5b48f5300fa973b58 = L.circle(
                [0.0, 0.0],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 356.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ee005c4e4e354a40ad8740b588476bfe = L.popup({maxWidth: '100%'
            
            });

            
                var html_732fa374808b4633babf3a9226fbcf6c = $(`<div id="html_732fa374808b4633babf3a9226fbcf6c" style="width: 100.0%; height: 100.0%;">Diamond Princess  712  on 8/25/20</div>`)[0];
                popup_ee005c4e4e354a40ad8740b588476bfe.setContent(html_732fa374808b4633babf3a9226fbcf6c);
            

            circle_844ec8a08fda4ac5b48f5300fa973b58.bindPopup(popup_ee005c4e4e354a40ad8740b588476bfe)
            ;

            
        
    

            var circle_c49eaad257be42ae9dd12e58267aaef5 = L.circle(
                [11.8251, 42.5903],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2691.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_200ea2b5643a4bbb901a16d3b2c85be8 = L.popup({maxWidth: '100%'
            
            });

            
                var html_de3a3966feff456e9e48b9a81e780061 = $(`<div id="html_de3a3966feff456e9e48b9a81e780061" style="width: 100.0%; height: 100.0%;">Djibouti  5383  on 8/25/20</div>`)[0];
                popup_200ea2b5643a4bbb901a16d3b2c85be8.setContent(html_de3a3966feff456e9e48b9a81e780061);
            

            circle_c49eaad257be42ae9dd12e58267aaef5.bindPopup(popup_200ea2b5643a4bbb901a16d3b2c85be8)
            ;

            
        
    

            var circle_d832671453f641e48ef4e0a235dfd714 = L.circle(
                [15.415, -61.371],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 10.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_24c6d6e68dcc44bc8014bc957bda8d8f = L.popup({maxWidth: '100%'
            
            });

            
                var html_5971985663fb436385fc6e229a30573d = $(`<div id="html_5971985663fb436385fc6e229a30573d" style="width: 100.0%; height: 100.0%;">Dominica  20  on 8/25/20</div>`)[0];
                popup_24c6d6e68dcc44bc8014bc957bda8d8f.setContent(html_5971985663fb436385fc6e229a30573d);
            

            circle_d832671453f641e48ef4e0a235dfd714.bindPopup(popup_24c6d6e68dcc44bc8014bc957bda8d8f)
            ;

            
        
    

            var circle_4a3986c173184345ac292e0463847a60 = L.circle(
                [18.7357, -70.1627],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 46108.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ec83df18348c4cb2be7d442809982b9c = L.popup({maxWidth: '100%'
            
            });

            
                var html_02c91c84417647109bc5dcb97fd93128 = $(`<div id="html_02c91c84417647109bc5dcb97fd93128" style="width: 100.0%; height: 100.0%;">Dominican Republic  92217  on 8/25/20</div>`)[0];
                popup_ec83df18348c4cb2be7d442809982b9c.setContent(html_02c91c84417647109bc5dcb97fd93128);
            

            circle_4a3986c173184345ac292e0463847a60.bindPopup(popup_ec83df18348c4cb2be7d442809982b9c)
            ;

            
        
    

            var circle_cc5c7c01cf164e1ab21ce4b0c8cace2f = L.circle(
                [-1.8312, -78.1834],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 54515.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ebe35d9eb2f1402ebd4c0209c4c5a998 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c33b5557bb1b4fa2a952ef952a22ce7c = $(`<div id="html_c33b5557bb1b4fa2a952ef952a22ce7c" style="width: 100.0%; height: 100.0%;">Ecuador  109030  on 8/25/20</div>`)[0];
                popup_ebe35d9eb2f1402ebd4c0209c4c5a998.setContent(html_c33b5557bb1b4fa2a952ef952a22ce7c);
            

            circle_cc5c7c01cf164e1ab21ce4b0c8cace2f.bindPopup(popup_ebe35d9eb2f1402ebd4c0209c4c5a998)
            ;

            
        
    

            var circle_d0132a0268ea4641b8a4f88277869991 = L.circle(
                [26.820553000000004, 30.802498],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 48809.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_90bd7d83e57b47c2828768bab5fd5acf = L.popup({maxWidth: '100%'
            
            });

            
                var html_4f37051cc9614f489c3b227915a415f7 = $(`<div id="html_4f37051cc9614f489c3b227915a415f7" style="width: 100.0%; height: 100.0%;">Egypt  97619  on 8/25/20</div>`)[0];
                popup_90bd7d83e57b47c2828768bab5fd5acf.setContent(html_4f37051cc9614f489c3b227915a415f7);
            

            circle_d0132a0268ea4641b8a4f88277869991.bindPopup(popup_90bd7d83e57b47c2828768bab5fd5acf)
            ;

            
        
    

            var circle_c534838fa1504b2dabdd5754277a7016 = L.circle(
                [13.7942, -88.8965],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 12493.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_eaaa9d15401845e5bd0264209055a3f7 = L.popup({maxWidth: '100%'
            
            });

            
                var html_7f311475287543d0b7b30e9a7ee8435c = $(`<div id="html_7f311475287543d0b7b30e9a7ee8435c" style="width: 100.0%; height: 100.0%;">El Salvador  24986  on 8/25/20</div>`)[0];
                popup_eaaa9d15401845e5bd0264209055a3f7.setContent(html_7f311475287543d0b7b30e9a7ee8435c);
            

            circle_c534838fa1504b2dabdd5754277a7016.bindPopup(popup_eaaa9d15401845e5bd0264209055a3f7)
            ;

            
        
    

            var circle_b0e57934af414d1898218384b9c916f9 = L.circle(
                [1.6508, 10.2679],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2463.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_209cc20282da4102af44e586c327bde0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_30c24d663d9b41a1a6aabf034f850501 = $(`<div id="html_30c24d663d9b41a1a6aabf034f850501" style="width: 100.0%; height: 100.0%;">Equatorial Guinea  4926  on 8/25/20</div>`)[0];
                popup_209cc20282da4102af44e586c327bde0.setContent(html_30c24d663d9b41a1a6aabf034f850501);
            

            circle_b0e57934af414d1898218384b9c916f9.bindPopup(popup_209cc20282da4102af44e586c327bde0)
            ;

            
        
    

            var circle_3dd1ad179c784736b11e9c28e036ab8f = L.circle(
                [15.1794, 39.7823],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 157.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e63ad38e3884467b94bdeab999ae0d61 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a9d7b548ae7946b0967f0c741ab8db78 = $(`<div id="html_a9d7b548ae7946b0967f0c741ab8db78" style="width: 100.0%; height: 100.0%;">Eritrea  315  on 8/25/20</div>`)[0];
                popup_e63ad38e3884467b94bdeab999ae0d61.setContent(html_a9d7b548ae7946b0967f0c741ab8db78);
            

            circle_3dd1ad179c784736b11e9c28e036ab8f.bindPopup(popup_e63ad38e3884467b94bdeab999ae0d61)
            ;

            
        
    

            var circle_60ffc912a3084f9d9ecf2b54dd5822c1 = L.circle(
                [58.5953, 25.0136],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1147.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_54cb5b5a4b174907bd8d7d39903cc00d = L.popup({maxWidth: '100%'
            
            });

            
                var html_f4a2aed664dd4a1488cb842632a9cfec = $(`<div id="html_f4a2aed664dd4a1488cb842632a9cfec" style="width: 100.0%; height: 100.0%;">Estonia  2294  on 8/25/20</div>`)[0];
                popup_54cb5b5a4b174907bd8d7d39903cc00d.setContent(html_f4a2aed664dd4a1488cb842632a9cfec);
            

            circle_60ffc912a3084f9d9ecf2b54dd5822c1.bindPopup(popup_54cb5b5a4b174907bd8d7d39903cc00d)
            ;

            
        
    

            var circle_0ef27adcc5824c77b0e7d10d3c741192 = L.circle(
                [-26.5225, 31.4659],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2163.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7a3605111d0f482eae6996c965309334 = L.popup({maxWidth: '100%'
            
            });

            
                var html_1bef7027b08f4d4db406b5473aaf2f57 = $(`<div id="html_1bef7027b08f4d4db406b5473aaf2f57" style="width: 100.0%; height: 100.0%;">Eswatini  4327  on 8/25/20</div>`)[0];
                popup_7a3605111d0f482eae6996c965309334.setContent(html_1bef7027b08f4d4db406b5473aaf2f57);
            

            circle_0ef27adcc5824c77b0e7d10d3c741192.bindPopup(popup_7a3605111d0f482eae6996c965309334)
            ;

            
        
    

            var circle_56b1a86e3e064c99be57feb1da607b08 = L.circle(
                [9.145, 40.4897],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 21844.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f01d4c3f7e7b45ee8dd2ec44539bf597 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ce8bcc68091b4d24ae2c1b09cc78e7c8 = $(`<div id="html_ce8bcc68091b4d24ae2c1b09cc78e7c8" style="width: 100.0%; height: 100.0%;">Ethiopia  43688  on 8/25/20</div>`)[0];
                popup_f01d4c3f7e7b45ee8dd2ec44539bf597.setContent(html_ce8bcc68091b4d24ae2c1b09cc78e7c8);
            

            circle_56b1a86e3e064c99be57feb1da607b08.bindPopup(popup_f01d4c3f7e7b45ee8dd2ec44539bf597)
            ;

            
        
    

            var circle_b6fbd7a2a4dd452d9479e726d928b3d9 = L.circle(
                [-17.7134, 178.065],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 14.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9d7c60548acb49688d9c503e9ce9979b = L.popup({maxWidth: '100%'
            
            });

            
                var html_d002f4a7311a4b2f87057c12feafb5da = $(`<div id="html_d002f4a7311a4b2f87057c12feafb5da" style="width: 100.0%; height: 100.0%;">Fiji  28  on 8/25/20</div>`)[0];
                popup_9d7c60548acb49688d9c503e9ce9979b.setContent(html_d002f4a7311a4b2f87057c12feafb5da);
            

            circle_b6fbd7a2a4dd452d9479e726d928b3d9.bindPopup(popup_9d7c60548acb49688d9c503e9ce9979b)
            ;

            
        
    

            var circle_dc840256c4fa4caf9abe15e179ca6900 = L.circle(
                [61.92411, 25.748151],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3990.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0e4ef2e606e140f39064e2bf3ee23a87 = L.popup({maxWidth: '100%'
            
            });

            
                var html_5ce0fc207f3244ac9226a6ed68a13b35 = $(`<div id="html_5ce0fc207f3244ac9226a6ed68a13b35" style="width: 100.0%; height: 100.0%;">Finland  7981  on 8/25/20</div>`)[0];
                popup_0e4ef2e606e140f39064e2bf3ee23a87.setContent(html_5ce0fc207f3244ac9226a6ed68a13b35);
            

            circle_dc840256c4fa4caf9abe15e179ca6900.bindPopup(popup_0e4ef2e606e140f39064e2bf3ee23a87)
            ;

            
        
    

            var circle_2466c2655821454689858062266aa934 = L.circle(
                [91.39739499999999, 60.04088600000003],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 142951.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f02ec7c8b8e845b4a6b667ce988445f0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_b67f2da4ffff4925bb5c200ae422775a = $(`<div id="html_b67f2da4ffff4925bb5c200ae422775a" style="width: 100.0%; height: 100.0%;">France  285902  on 8/25/20</div>`)[0];
                popup_f02ec7c8b8e845b4a6b667ce988445f0.setContent(html_b67f2da4ffff4925bb5c200ae422775a);
            

            circle_2466c2655821454689858062266aa934.bindPopup(popup_f02ec7c8b8e845b4a6b667ce988445f0)
            ;

            
        
    

            var circle_48160662bfe04120a8d6c61d3617c7c8 = L.circle(
                [-0.8037, 11.6094],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4204.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a391d6fa1f92442b8f311ee23824ac44 = L.popup({maxWidth: '100%'
            
            });

            
                var html_acc72239bb664179b091f3c04dca3997 = $(`<div id="html_acc72239bb664179b091f3c04dca3997" style="width: 100.0%; height: 100.0%;">Gabon  8409  on 8/25/20</div>`)[0];
                popup_a391d6fa1f92442b8f311ee23824ac44.setContent(html_acc72239bb664179b091f3c04dca3997);
            

            circle_48160662bfe04120a8d6c61d3617c7c8.bindPopup(popup_a391d6fa1f92442b8f311ee23824ac44)
            ;

            
        
    

            var circle_a7a71039061d4d9cabb75dea292a06f5 = L.circle(
                [13.4432, -15.3101],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1343.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_44e02ae51d4343e49f26d84d0112d697 = L.popup({maxWidth: '100%'
            
            });

            
                var html_4974c7d6236a4e94bba72b52426e69db = $(`<div id="html_4974c7d6236a4e94bba72b52426e69db" style="width: 100.0%; height: 100.0%;">Gambia  2686  on 8/25/20</div>`)[0];
                popup_44e02ae51d4343e49f26d84d0112d697.setContent(html_4974c7d6236a4e94bba72b52426e69db);
            

            circle_a7a71039061d4d9cabb75dea292a06f5.bindPopup(popup_44e02ae51d4343e49f26d84d0112d697)
            ;

            
        
    

            var circle_43f71e53894e4603ae055f13f21828f2 = L.circle(
                [42.3154, 43.3569],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 714.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_20fd38d297d447729d826f6ae9ca28c3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_eedb4a6ce4dc46dda8edfd83c19ea94b = $(`<div id="html_eedb4a6ce4dc46dda8edfd83c19ea94b" style="width: 100.0%; height: 100.0%;">Georgia  1429  on 8/25/20</div>`)[0];
                popup_20fd38d297d447729d826f6ae9ca28c3.setContent(html_eedb4a6ce4dc46dda8edfd83c19ea94b);
            

            circle_43f71e53894e4603ae055f13f21828f2.bindPopup(popup_20fd38d297d447729d826f6ae9ca28c3)
            ;

            
        
    

            var circle_50070b0078874b0fb731a761091edd3d = L.circle(
                [51.165691, 10.451526],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 118791.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8afa733e6c1749e1bd6bf42be0efca4f = L.popup({maxWidth: '100%'
            
            });

            
                var html_a0c18d8886dd4e36905d81210df89a68 = $(`<div id="html_a0c18d8886dd4e36905d81210df89a68" style="width: 100.0%; height: 100.0%;">Germany  237583  on 8/25/20</div>`)[0];
                popup_8afa733e6c1749e1bd6bf42be0efca4f.setContent(html_a0c18d8886dd4e36905d81210df89a68);
            

            circle_50070b0078874b0fb731a761091edd3d.bindPopup(popup_8afa733e6c1749e1bd6bf42be0efca4f)
            ;

            
        
    

            var circle_0e8b5f31182c419a82ddbe29abd104b9 = L.circle(
                [7.9465, -1.0232],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 21858.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_66c3f755f6384f5c909ebef32aee33cb = L.popup({maxWidth: '100%'
            
            });

            
                var html_7952f3602cee4ce892b81d3d92e0f3c3 = $(`<div id="html_7952f3602cee4ce892b81d3d92e0f3c3" style="width: 100.0%; height: 100.0%;">Ghana  43717  on 8/25/20</div>`)[0];
                popup_66c3f755f6384f5c909ebef32aee33cb.setContent(html_7952f3602cee4ce892b81d3d92e0f3c3);
            

            circle_0e8b5f31182c419a82ddbe29abd104b9.bindPopup(popup_66c3f755f6384f5c909ebef32aee33cb)
            ;

            
        
    

            var circle_82599f95637e4343a20cf12e5a179a9c = L.circle(
                [39.0742, 21.8243],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4493.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_48156906ee73489db55c967571dc95a5 = L.popup({maxWidth: '100%'
            
            });

            
                var html_38ae9665bfdc43b8adad04ee0ac4ba0d = $(`<div id="html_38ae9665bfdc43b8adad04ee0ac4ba0d" style="width: 100.0%; height: 100.0%;">Greece  8987  on 8/25/20</div>`)[0];
                popup_48156906ee73489db55c967571dc95a5.setContent(html_38ae9665bfdc43b8adad04ee0ac4ba0d);
            

            circle_82599f95637e4343a20cf12e5a179a9c.bindPopup(popup_48156906ee73489db55c967571dc95a5)
            ;

            
        
    

            var circle_75e28248f19f45849eefb73dbffb797f = L.circle(
                [12.1165, -61.679],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 12.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e025f832caa54cb5a50ecebc42c52fd3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_6cf961a4e6134bfdbf9498325cc25e4b = $(`<div id="html_6cf961a4e6134bfdbf9498325cc25e4b" style="width: 100.0%; height: 100.0%;">Grenada  24  on 8/25/20</div>`)[0];
                popup_e025f832caa54cb5a50ecebc42c52fd3.setContent(html_6cf961a4e6134bfdbf9498325cc25e4b);
            

            circle_75e28248f19f45849eefb73dbffb797f.bindPopup(popup_e025f832caa54cb5a50ecebc42c52fd3)
            ;

            
        
    

            var circle_1b6a4cd3daf04c4fa8ee4b0c4534111d = L.circle(
                [15.7835, -90.2308],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 34825.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2735707eb46f472ab15ba03e7bd98ca2 = L.popup({maxWidth: '100%'
            
            });

            
                var html_3771599146e04b97a82c4b1cf7f6874d = $(`<div id="html_3771599146e04b97a82c4b1cf7f6874d" style="width: 100.0%; height: 100.0%;">Guatemala  69651  on 8/25/20</div>`)[0];
                popup_2735707eb46f472ab15ba03e7bd98ca2.setContent(html_3771599146e04b97a82c4b1cf7f6874d);
            

            circle_1b6a4cd3daf04c4fa8ee4b0c4534111d.bindPopup(popup_2735707eb46f472ab15ba03e7bd98ca2)
            ;

            
        
    

            var circle_813381ee801940f386aae165f9564602 = L.circle(
                [9.9456, -9.6966],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4564.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f0f2204f9ea545e090fe5476cb8a0eb5 = L.popup({maxWidth: '100%'
            
            });

            
                var html_32bc9a7171d242829ca39bb4a533d55f = $(`<div id="html_32bc9a7171d242829ca39bb4a533d55f" style="width: 100.0%; height: 100.0%;">Guinea  9128  on 8/25/20</div>`)[0];
                popup_f0f2204f9ea545e090fe5476cb8a0eb5.setContent(html_32bc9a7171d242829ca39bb4a533d55f);
            

            circle_813381ee801940f386aae165f9564602.bindPopup(popup_f0f2204f9ea545e090fe5476cb8a0eb5)
            ;

            
        
    

            var circle_5eb9d59f163543a586cfd0dbe9f168f6 = L.circle(
                [11.8037, -15.1804],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1074.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_914d59f44ccb4f0d983e2505170b2730 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9b6f699f27a14d089290b8cbd93db0f4 = $(`<div id="html_9b6f699f27a14d089290b8cbd93db0f4" style="width: 100.0%; height: 100.0%;">Guinea-Bissau  2149  on 8/25/20</div>`)[0];
                popup_914d59f44ccb4f0d983e2505170b2730.setContent(html_9b6f699f27a14d089290b8cbd93db0f4);
            

            circle_5eb9d59f163543a586cfd0dbe9f168f6.bindPopup(popup_914d59f44ccb4f0d983e2505170b2730)
            ;

            
        
    

            var circle_310d42f7212042558eec5bec719e68b8 = L.circle(
                [4.860416000000002, -58.93018000000001],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 530.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3d39b1d9722c4615a412f93c71d0b870 = L.popup({maxWidth: '100%'
            
            });

            
                var html_df1519dbcdf647fb872c7e715fc214b6 = $(`<div id="html_df1519dbcdf647fb872c7e715fc214b6" style="width: 100.0%; height: 100.0%;">Guyana  1060  on 8/25/20</div>`)[0];
                popup_3d39b1d9722c4615a412f93c71d0b870.setContent(html_df1519dbcdf647fb872c7e715fc214b6);
            

            circle_310d42f7212042558eec5bec719e68b8.bindPopup(popup_3d39b1d9722c4615a412f93c71d0b870)
            ;

            
        
    

            var circle_f720995d4eef4ede929bb7a9683cfa28 = L.circle(
                [18.9712, -72.2852],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4056.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7ea13ae4445747aca69fe22685f0706a = L.popup({maxWidth: '100%'
            
            });

            
                var html_3ec9ec5f5c314fe5989fd466a4bde722 = $(`<div id="html_3ec9ec5f5c314fe5989fd466a4bde722" style="width: 100.0%; height: 100.0%;">Haiti  8112  on 8/25/20</div>`)[0];
                popup_7ea13ae4445747aca69fe22685f0706a.setContent(html_3ec9ec5f5c314fe5989fd466a4bde722);
            

            circle_f720995d4eef4ede929bb7a9683cfa28.bindPopup(popup_7ea13ae4445747aca69fe22685f0706a)
            ;

            
        
    

            var circle_90f55b5fa0c84922affbdb19a76da968 = L.circle(
                [41.9029, 12.4534],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_878d149b85a640acb053ef4287458d14 = L.popup({maxWidth: '100%'
            
            });

            
                var html_783b0f9f441d4de682d04d3061afeddc = $(`<div id="html_783b0f9f441d4de682d04d3061afeddc" style="width: 100.0%; height: 100.0%;">Holy See  12  on 8/25/20</div>`)[0];
                popup_878d149b85a640acb053ef4287458d14.setContent(html_783b0f9f441d4de682d04d3061afeddc);
            

            circle_90f55b5fa0c84922affbdb19a76da968.bindPopup(popup_878d149b85a640acb053ef4287458d14)
            ;

            
        
    

            var circle_99d377f5016d4116a81d40778cf5552c = L.circle(
                [15.2, -86.2419],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 27938.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_386f1ad0704b4172a788f0ac496df09d = L.popup({maxWidth: '100%'
            
            });

            
                var html_d6345e5246074246b2068eb7002ec3e4 = $(`<div id="html_d6345e5246074246b2068eb7002ec3e4" style="width: 100.0%; height: 100.0%;">Honduras  55877  on 8/25/20</div>`)[0];
                popup_386f1ad0704b4172a788f0ac496df09d.setContent(html_d6345e5246074246b2068eb7002ec3e4);
            

            circle_99d377f5016d4116a81d40778cf5552c.bindPopup(popup_386f1ad0704b4172a788f0ac496df09d)
            ;

            
        
    

            var circle_2752864ff8504ac1a8d06887c7ce74a6 = L.circle(
                [47.1625, 19.5033],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2607.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_84862e661ec145bc8f0807dfa5bde3a5 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a5a01021337843b6af6f3bbb1d8afd28 = $(`<div id="html_a5a01021337843b6af6f3bbb1d8afd28" style="width: 100.0%; height: 100.0%;">Hungary  5215  on 8/25/20</div>`)[0];
                popup_84862e661ec145bc8f0807dfa5bde3a5.setContent(html_a5a01021337843b6af6f3bbb1d8afd28);
            

            circle_2752864ff8504ac1a8d06887c7ce74a6.bindPopup(popup_84862e661ec145bc8f0807dfa5bde3a5)
            ;

            
        
    

            var circle_b439c6f7931241299e3fb1d3f620ef8a = L.circle(
                [64.9631, -19.0208],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1038.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_953023d9ada54a879c27bf079b35b4f1 = L.popup({maxWidth: '100%'
            
            });

            
                var html_0c20bf056eb54fb891b8d9291a19a3d1 = $(`<div id="html_0c20bf056eb54fb891b8d9291a19a3d1" style="width: 100.0%; height: 100.0%;">Iceland  2077  on 8/25/20</div>`)[0];
                popup_953023d9ada54a879c27bf079b35b4f1.setContent(html_0c20bf056eb54fb891b8d9291a19a3d1);
            

            circle_b439c6f7931241299e3fb1d3f620ef8a.bindPopup(popup_953023d9ada54a879c27bf079b35b4f1)
            ;

            
        
    

            var circle_507253f038f448009c907e0076bf71ff = L.circle(
                [20.593684, 78.96288],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1612273.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b487a075910a43038f7d2368e1a417a2 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f6294615b94b444a8f9ad883b7602fd3 = $(`<div id="html_f6294615b94b444a8f9ad883b7602fd3" style="width: 100.0%; height: 100.0%;">India  3224547  on 8/25/20</div>`)[0];
                popup_b487a075910a43038f7d2368e1a417a2.setContent(html_f6294615b94b444a8f9ad883b7602fd3);
            

            circle_507253f038f448009c907e0076bf71ff.bindPopup(popup_b487a075910a43038f7d2368e1a417a2)
            ;

            
        
    

            var circle_dfef53167a604ccdbf1edf32be6fea2c = L.circle(
                [-0.7893, 113.9213],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 78929.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3ef6c0d9813643cfb4689d22009ae754 = L.popup({maxWidth: '100%'
            
            });

            
                var html_598284d8437d44a1a9dc2cc6ae7a2d14 = $(`<div id="html_598284d8437d44a1a9dc2cc6ae7a2d14" style="width: 100.0%; height: 100.0%;">Indonesia  157859  on 8/25/20</div>`)[0];
                popup_3ef6c0d9813643cfb4689d22009ae754.setContent(html_598284d8437d44a1a9dc2cc6ae7a2d14);
            

            circle_dfef53167a604ccdbf1edf32be6fea2c.bindPopup(popup_3ef6c0d9813643cfb4689d22009ae754)
            ;

            
        
    

            var circle_67a492b24b7f408195b8099e26f0b4b8 = L.circle(
                [32.427908, 53.68804599999999],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 181681.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_976f667adb9a4f85a487e86bcc5b2850 = L.popup({maxWidth: '100%'
            
            });

            
                var html_e6ea8eec550c4102bb89bd86dac2ea73 = $(`<div id="html_e6ea8eec550c4102bb89bd86dac2ea73" style="width: 100.0%; height: 100.0%;">Iran  363363  on 8/25/20</div>`)[0];
                popup_976f667adb9a4f85a487e86bcc5b2850.setContent(html_e6ea8eec550c4102bb89bd86dac2ea73);
            

            circle_67a492b24b7f408195b8099e26f0b4b8.bindPopup(popup_976f667adb9a4f85a487e86bcc5b2850)
            ;

            
        
    

            var circle_ad0efc4248d043f98a004ec1e4117c62 = L.circle(
                [33.223191, 43.679291],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 105973.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_766e1620f7d24a5e87b9bfdff647ed95 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c1f9078313594b9cbc42f7168682c667 = $(`<div id="html_c1f9078313594b9cbc42f7168682c667" style="width: 100.0%; height: 100.0%;">Iraq  211947  on 8/25/20</div>`)[0];
                popup_766e1620f7d24a5e87b9bfdff647ed95.setContent(html_c1f9078313594b9cbc42f7168682c667);
            

            circle_ad0efc4248d043f98a004ec1e4117c62.bindPopup(popup_766e1620f7d24a5e87b9bfdff647ed95)
            ;

            
        
    

            var circle_60733b0fcf8f40a59040c98d98f494ad = L.circle(
                [53.1424, -7.6921],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 14100.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8ef01eaf60e544a08475bacf8dcf6728 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d04ca82418174ee2af19a1a9dc4a44c2 = $(`<div id="html_d04ca82418174ee2af19a1a9dc4a44c2" style="width: 100.0%; height: 100.0%;">Ireland  28201  on 8/25/20</div>`)[0];
                popup_8ef01eaf60e544a08475bacf8dcf6728.setContent(html_d04ca82418174ee2af19a1a9dc4a44c2);
            

            circle_60733b0fcf8f40a59040c98d98f494ad.bindPopup(popup_8ef01eaf60e544a08475bacf8dcf6728)
            ;

            
        
    

            var circle_c46285d3332d4f4f84abfe759840e9d9 = L.circle(
                [31.046051, 34.851612],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 53230.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9a1324fabf294142bb0ae854302a1b70 = L.popup({maxWidth: '100%'
            
            });

            
                var html_b4834b20aa704781b04baaa889e4dbe1 = $(`<div id="html_b4834b20aa704781b04baaa889e4dbe1" style="width: 100.0%; height: 100.0%;">Israel  106460  on 8/25/20</div>`)[0];
                popup_9a1324fabf294142bb0ae854302a1b70.setContent(html_b4834b20aa704781b04baaa889e4dbe1);
            

            circle_c46285d3332d4f4f84abfe759840e9d9.bindPopup(popup_9a1324fabf294142bb0ae854302a1b70)
            ;

            
        
    

            var circle_a312ef8acd754f1d880a801ceaaa9d8e = L.circle(
                [41.87194, 12.56738],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 130587.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4f631c53552f46068d8a47a9d4e1481c = L.popup({maxWidth: '100%'
            
            });

            
                var html_c8e778fcc9d34a809ac65661a78d7c29 = $(`<div id="html_c8e778fcc9d34a809ac65661a78d7c29" style="width: 100.0%; height: 100.0%;">Italy  261174  on 8/25/20</div>`)[0];
                popup_4f631c53552f46068d8a47a9d4e1481c.setContent(html_c8e778fcc9d34a809ac65661a78d7c29);
            

            circle_a312ef8acd754f1d880a801ceaaa9d8e.bindPopup(popup_4f631c53552f46068d8a47a9d4e1481c)
            ;

            
        
    

            var circle_9c0069da092549d8895c2adbb1530699 = L.circle(
                [18.1096, -77.2975],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 866.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a79d8b8d53d04f0a9381836555b1fba4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a326d10d16a541d9b3e15ff80b0af094 = $(`<div id="html_a326d10d16a541d9b3e15ff80b0af094" style="width: 100.0%; height: 100.0%;">Jamaica  1732  on 8/25/20</div>`)[0];
                popup_a79d8b8d53d04f0a9381836555b1fba4.setContent(html_a326d10d16a541d9b3e15ff80b0af094);
            

            circle_9c0069da092549d8895c2adbb1530699.bindPopup(popup_a79d8b8d53d04f0a9381836555b1fba4)
            ;

            
        
    

            var circle_ef05bbf28f0240529538247a0be0be06 = L.circle(
                [36.204824, 138.252924],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 31944.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_92cff87f7ca84bd98d3b3b8ced07a2d0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_013a17ef8124480fbb210629f369055b = $(`<div id="html_013a17ef8124480fbb210629f369055b" style="width: 100.0%; height: 100.0%;">Japan  63888  on 8/25/20</div>`)[0];
                popup_92cff87f7ca84bd98d3b3b8ced07a2d0.setContent(html_013a17ef8124480fbb210629f369055b);
            

            circle_ef05bbf28f0240529538247a0be0be06.bindPopup(popup_92cff87f7ca84bd98d3b3b8ced07a2d0)
            ;

            
        
    

            var circle_97e31b2ac50342dc87d263804f3e2fb1 = L.circle(
                [31.24, 36.51],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 858.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_adadf8fdbb3147b9a143da8498f8f283 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bf5b300418b3416aadbeec7b6b90100e = $(`<div id="html_bf5b300418b3416aadbeec7b6b90100e" style="width: 100.0%; height: 100.0%;">Jordan  1716  on 8/25/20</div>`)[0];
                popup_adadf8fdbb3147b9a143da8498f8f283.setContent(html_bf5b300418b3416aadbeec7b6b90100e);
            

            circle_97e31b2ac50342dc87d263804f3e2fb1.bindPopup(popup_adadf8fdbb3147b9a143da8498f8f283)
            ;

            
        
    

            var circle_cc9de5bcb2be4d5b8a3e7bbf24aa0d98 = L.circle(
                [48.0196, 66.9237],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 52537.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_13595cf2116241f0a702c3c4905d9201 = L.popup({maxWidth: '100%'
            
            });

            
                var html_128d1a3680d840d1b8df2d486d98cbc2 = $(`<div id="html_128d1a3680d840d1b8df2d486d98cbc2" style="width: 100.0%; height: 100.0%;">Kazakhstan  105075  on 8/25/20</div>`)[0];
                popup_13595cf2116241f0a702c3c4905d9201.setContent(html_128d1a3680d840d1b8df2d486d98cbc2);
            

            circle_cc9de5bcb2be4d5b8a3e7bbf24aa0d98.bindPopup(popup_13595cf2116241f0a702c3c4905d9201)
            ;

            
        
    

            var circle_65d5ed728b9c48df87674bec5c40020d = L.circle(
                [-0.0236, 37.9062],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 16401.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_1741df71bb644ee9a871de13842953f3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_51351b471d3e4a03aa776a42a66a644c = $(`<div id="html_51351b471d3e4a03aa776a42a66a644c" style="width: 100.0%; height: 100.0%;">Kenya  32803  on 8/25/20</div>`)[0];
                popup_1741df71bb644ee9a871de13842953f3.setContent(html_51351b471d3e4a03aa776a42a66a644c);
            

            circle_65d5ed728b9c48df87674bec5c40020d.bindPopup(popup_1741df71bb644ee9a871de13842953f3)
            ;

            
        
    

            var circle_c87da83af4e84a95b823293d3d8a26b6 = L.circle(
                [35.90775700000001, 127.766922],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 9132.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cd78aa6f942944d1974eb542dd4365fe = L.popup({maxWidth: '100%'
            
            });

            
                var html_92e5f4b748934be5b323ecb7edb86a01 = $(`<div id="html_92e5f4b748934be5b323ecb7edb86a01" style="width: 100.0%; height: 100.0%;">Korea, South  18265  on 8/25/20</div>`)[0];
                popup_cd78aa6f942944d1974eb542dd4365fe.setContent(html_92e5f4b748934be5b323ecb7edb86a01);
            

            circle_c87da83af4e84a95b823293d3d8a26b6.bindPopup(popup_cd78aa6f942944d1974eb542dd4365fe)
            ;

            
        
    

            var circle_25eb8b405a7a430c86f78418906d6950 = L.circle(
                [42.602636, 20.902977],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6341.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_fc11c66ac47d4572a832edefbd3108fe = L.popup({maxWidth: '100%'
            
            });

            
                var html_f74e17089b1149308f453a49cadcab7c = $(`<div id="html_f74e17089b1149308f453a49cadcab7c" style="width: 100.0%; height: 100.0%;">Kosovo  12683  on 8/25/20</div>`)[0];
                popup_fc11c66ac47d4572a832edefbd3108fe.setContent(html_f74e17089b1149308f453a49cadcab7c);
            

            circle_25eb8b405a7a430c86f78418906d6950.bindPopup(popup_fc11c66ac47d4572a832edefbd3108fe)
            ;

            
        
    

            var circle_a1ece775cfae4b46b9337e784ae6420b = L.circle(
                [29.31166, 47.481766],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 40786.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_18e8ce57a4ef449789dc0be47838d5fc = L.popup({maxWidth: '100%'
            
            });

            
                var html_592a0184632a482fa5fd854d88e519bd = $(`<div id="html_592a0184632a482fa5fd854d88e519bd" style="width: 100.0%; height: 100.0%;">Kuwait  81573  on 8/25/20</div>`)[0];
                popup_18e8ce57a4ef449789dc0be47838d5fc.setContent(html_592a0184632a482fa5fd854d88e519bd);
            

            circle_a1ece775cfae4b46b9337e784ae6420b.bindPopup(popup_18e8ce57a4ef449789dc0be47838d5fc)
            ;

            
        
    

            var circle_ae4d23e6b31c49818ab127689f1b219c = L.circle(
                [41.20438, 74.766098],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 21622.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ff523c66b01f488e8d0a1074b6902cd7 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d7f09b23e61246c596c9e700cd98017c = $(`<div id="html_d7f09b23e61246c596c9e700cd98017c" style="width: 100.0%; height: 100.0%;">Kyrgyzstan  43245  on 8/25/20</div>`)[0];
                popup_ff523c66b01f488e8d0a1074b6902cd7.setContent(html_d7f09b23e61246c596c9e700cd98017c);
            

            circle_ae4d23e6b31c49818ab127689f1b219c.bindPopup(popup_ff523c66b01f488e8d0a1074b6902cd7)
            ;

            
        
    

            var circle_30ecfa37c1834890b091a1c94109776f = L.circle(
                [19.85627, 102.495496],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 11.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_752530ed356b403faf5aaec215e6baf4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_11db91603e0242fab7a6ac037efcc088 = $(`<div id="html_11db91603e0242fab7a6ac037efcc088" style="width: 100.0%; height: 100.0%;">Laos  22  on 8/25/20</div>`)[0];
                popup_752530ed356b403faf5aaec215e6baf4.setContent(html_11db91603e0242fab7a6ac037efcc088);
            

            circle_30ecfa37c1834890b091a1c94109776f.bindPopup(popup_752530ed356b403faf5aaec215e6baf4)
            ;

            
        
    

            var circle_8ef062cbdb3040138285d0202dbbcabf = L.circle(
                [56.8796, 24.6032],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 671.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_fb45aee12dd9496291d8a7e00c18e180 = L.popup({maxWidth: '100%'
            
            });

            
                var html_94576ce02fd2416898a212e817170528 = $(`<div id="html_94576ce02fd2416898a212e817170528" style="width: 100.0%; height: 100.0%;">Latvia  1342  on 8/25/20</div>`)[0];
                popup_fb45aee12dd9496291d8a7e00c18e180.setContent(html_94576ce02fd2416898a212e817170528);
            

            circle_8ef062cbdb3040138285d0202dbbcabf.bindPopup(popup_fb45aee12dd9496291d8a7e00c18e180)
            ;

            
        
    

            var circle_f0c29e041f624601b1eb31d83db6a22f = L.circle(
                [33.8547, 35.8623],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6843.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a251ca11674741edaef0ec99c6c2ba44 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bf5c0cd052aa4bb5b2a9b88364e3c50c = $(`<div id="html_bf5c0cd052aa4bb5b2a9b88364e3c50c" style="width: 100.0%; height: 100.0%;">Lebanon  13687  on 8/25/20</div>`)[0];
                popup_a251ca11674741edaef0ec99c6c2ba44.setContent(html_bf5c0cd052aa4bb5b2a9b88364e3c50c);
            

            circle_f0c29e041f624601b1eb31d83db6a22f.bindPopup(popup_a251ca11674741edaef0ec99c6c2ba44)
            ;

            
        
    

            var circle_beda6324d29c47b0b41b91132bf3de7d = L.circle(
                [-29.61, 28.2336],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 524.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_eb83a828689941498f2791e035e24971 = L.popup({maxWidth: '100%'
            
            });

            
                var html_efb240880f484b3a92c6efca45eb1483 = $(`<div id="html_efb240880f484b3a92c6efca45eb1483" style="width: 100.0%; height: 100.0%;">Lesotho  1049  on 8/25/20</div>`)[0];
                popup_eb83a828689941498f2791e035e24971.setContent(html_efb240880f484b3a92c6efca45eb1483);
            

            circle_beda6324d29c47b0b41b91132bf3de7d.bindPopup(popup_eb83a828689941498f2791e035e24971)
            ;

            
        
    

            var circle_fb04c1cbb41646ce9255721044b371b7 = L.circle(
                [6.4280550000000005, -9.429499],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 647.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b68033aff379499d8b62dec070a423f0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_484a763a1c2b4f8985bb99ab5873ca5e = $(`<div id="html_484a763a1c2b4f8985bb99ab5873ca5e" style="width: 100.0%; height: 100.0%;">Liberia  1295  on 8/25/20</div>`)[0];
                popup_b68033aff379499d8b62dec070a423f0.setContent(html_484a763a1c2b4f8985bb99ab5873ca5e);
            

            circle_fb04c1cbb41646ce9255721044b371b7.bindPopup(popup_b68033aff379499d8b62dec070a423f0)
            ;

            
        
    

            var circle_3a0d6a1ddc33456fae8ea053f3090ad6 = L.circle(
                [26.3351, 17.228331],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5640.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_c9bfc60f45b24b358e5dc6c838e87e25 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f6c36ef5867b464c8246df696e42a669 = $(`<div id="html_f6c36ef5867b464c8246df696e42a669" style="width: 100.0%; height: 100.0%;">Libya  11281  on 8/25/20</div>`)[0];
                popup_c9bfc60f45b24b358e5dc6c838e87e25.setContent(html_f6c36ef5867b464c8246df696e42a669);
            

            circle_3a0d6a1ddc33456fae8ea053f3090ad6.bindPopup(popup_c9bfc60f45b24b358e5dc6c838e87e25)
            ;

            
        
    

            var circle_7899699c9c144ea1ac635fcbf104f06c = L.circle(
                [47.14, 9.55],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 51.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_fcee8e4aff2446c99e56ed0f08a79d24 = L.popup({maxWidth: '100%'
            
            });

            
                var html_10524c32ef8e48b4b2068c90963359e5 = $(`<div id="html_10524c32ef8e48b4b2068c90963359e5" style="width: 100.0%; height: 100.0%;">Liechtenstein  102  on 8/25/20</div>`)[0];
                popup_fcee8e4aff2446c99e56ed0f08a79d24.setContent(html_10524c32ef8e48b4b2068c90963359e5);
            

            circle_7899699c9c144ea1ac635fcbf104f06c.bindPopup(popup_fcee8e4aff2446c99e56ed0f08a79d24)
            ;

            
        
    

            var circle_30f688af512a4ea4b152a63708279771 = L.circle(
                [55.1694, 23.8813],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1347.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_6e1e0dacb1de4951af41300de2dccd2c = L.popup({maxWidth: '100%'
            
            });

            
                var html_bd5ae7b3c06148f8a867be86249fddc2 = $(`<div id="html_bd5ae7b3c06148f8a867be86249fddc2" style="width: 100.0%; height: 100.0%;">Lithuania  2694  on 8/25/20</div>`)[0];
                popup_6e1e0dacb1de4951af41300de2dccd2c.setContent(html_bd5ae7b3c06148f8a867be86249fddc2);
            

            circle_30f688af512a4ea4b152a63708279771.bindPopup(popup_6e1e0dacb1de4951af41300de2dccd2c)
            ;

            
        
    

            var circle_6af3812e4af2442ebbbb5cb90ddffc42 = L.circle(
                [49.8153, 6.1296],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3919.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4077dd923c5948df9cfc6cb56fb25c80 = L.popup({maxWidth: '100%'
            
            });

            
                var html_79cd66cdbfac44f09f64066fbaee1c9e = $(`<div id="html_79cd66cdbfac44f09f64066fbaee1c9e" style="width: 100.0%; height: 100.0%;">Luxembourg  7838  on 8/25/20</div>`)[0];
                popup_4077dd923c5948df9cfc6cb56fb25c80.setContent(html_79cd66cdbfac44f09f64066fbaee1c9e);
            

            circle_6af3812e4af2442ebbbb5cb90ddffc42.bindPopup(popup_4077dd923c5948df9cfc6cb56fb25c80)
            ;

            
        
    

            var circle_bfa0c9b916844a168e251cf2601bd658 = L.circle(
                [0.0, 0.0],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e9e48bfccc50477f99af7e78b337620d = L.popup({maxWidth: '100%'
            
            });

            
                var html_3118b1b3b96a4e429af768bac49e3796 = $(`<div id="html_3118b1b3b96a4e429af768bac49e3796" style="width: 100.0%; height: 100.0%;">MS Zaandam  9  on 8/25/20</div>`)[0];
                popup_e9e48bfccc50477f99af7e78b337620d.setContent(html_3118b1b3b96a4e429af768bac49e3796);
            

            circle_bfa0c9b916844a168e251cf2601bd658.bindPopup(popup_e9e48bfccc50477f99af7e78b337620d)
            ;

            
        
    

            var circle_b10f54b6003c44c5942c0be316615535 = L.circle(
                [-18.766947, 46.869107],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 7237.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_05b6131e39b548b2ab93513cc60eba40 = L.popup({maxWidth: '100%'
            
            });

            
                var html_0febdfbfb9474829b64d7ecf3cc8b87d = $(`<div id="html_0febdfbfb9474829b64d7ecf3cc8b87d" style="width: 100.0%; height: 100.0%;">Madagascar  14475  on 8/25/20</div>`)[0];
                popup_05b6131e39b548b2ab93513cc60eba40.setContent(html_0febdfbfb9474829b64d7ecf3cc8b87d);
            

            circle_b10f54b6003c44c5942c0be316615535.bindPopup(popup_05b6131e39b548b2ab93513cc60eba40)
            ;

            
        
    

            var circle_7055738d0ea748968ca2ecf36a772e31 = L.circle(
                [-13.2543, 34.3015],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2711.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0bcf7930100a43f6a8676f0907d5d351 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ce83047377cc48378e8e4788e999ef54 = $(`<div id="html_ce83047377cc48378e8e4788e999ef54" style="width: 100.0%; height: 100.0%;">Malawi  5423  on 8/25/20</div>`)[0];
                popup_0bcf7930100a43f6a8676f0907d5d351.setContent(html_ce83047377cc48378e8e4788e999ef54);
            

            circle_7055738d0ea748968ca2ecf36a772e31.bindPopup(popup_0bcf7930100a43f6a8676f0907d5d351)
            ;

            
        
    

            var circle_6833e5eb8dc24e6db4a2bf8d091ca3a7 = L.circle(
                [4.210483999999999, 101.975766],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4642.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_21681e74f2a84bfe9fc51548c875b6dc = L.popup({maxWidth: '100%'
            
            });

            
                var html_e7be0a950c8945fcba99e223467af26b = $(`<div id="html_e7be0a950c8945fcba99e223467af26b" style="width: 100.0%; height: 100.0%;">Malaysia  9285  on 8/25/20</div>`)[0];
                popup_21681e74f2a84bfe9fc51548c875b6dc.setContent(html_e7be0a950c8945fcba99e223467af26b);
            

            circle_6833e5eb8dc24e6db4a2bf8d091ca3a7.bindPopup(popup_21681e74f2a84bfe9fc51548c875b6dc)
            ;

            
        
    

            var circle_4e226164cef445309eb57d80a129ad25 = L.circle(
                [3.2028, 73.2207],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3523.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7759fb0735194b269b6cf22a8a3d55f3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a54861c13f3441699901bbb8cbf274f5 = $(`<div id="html_a54861c13f3441699901bbb8cbf274f5" style="width: 100.0%; height: 100.0%;">Maldives  7047  on 8/25/20</div>`)[0];
                popup_7759fb0735194b269b6cf22a8a3d55f3.setContent(html_a54861c13f3441699901bbb8cbf274f5);
            

            circle_4e226164cef445309eb57d80a129ad25.bindPopup(popup_7759fb0735194b269b6cf22a8a3d55f3)
            ;

            
        
    

            var circle_f5d03fbd08704a83833e51ac298a794a = L.circle(
                [17.570692, -3.996166000000001],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1356.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_73c8ab2cb81c491d96d4709ebaef60e0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_123af048091341a2a004fa286321ee39 = $(`<div id="html_123af048091341a2a004fa286321ee39" style="width: 100.0%; height: 100.0%;">Mali  2713  on 8/25/20</div>`)[0];
                popup_73c8ab2cb81c491d96d4709ebaef60e0.setContent(html_123af048091341a2a004fa286321ee39);
            

            circle_f5d03fbd08704a83833e51ac298a794a.bindPopup(popup_73c8ab2cb81c491d96d4709ebaef60e0)
            ;

            
        
    

            var circle_7c8ebbc7ea2f4010bacfa309f424563c = L.circle(
                [35.9375, 14.3754],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 852.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_368ade080b2e4dd89820534a379ba7ab = L.popup({maxWidth: '100%'
            
            });

            
                var html_3b47311f2d5d4092b20d1437849f7c68 = $(`<div id="html_3b47311f2d5d4092b20d1437849f7c68" style="width: 100.0%; height: 100.0%;">Malta  1705  on 8/25/20</div>`)[0];
                popup_368ade080b2e4dd89820534a379ba7ab.setContent(html_3b47311f2d5d4092b20d1437849f7c68);
            

            circle_7c8ebbc7ea2f4010bacfa309f424563c.bindPopup(popup_368ade080b2e4dd89820534a379ba7ab)
            ;

            
        
    

            var circle_f3b7276b1ced45ee85acba1f556583b7 = L.circle(
                [21.0079, -10.9408],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3480.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_66cc93b69bd1409e9de2c630af7d3dd3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bcc47c0647304452bc95a2d1fc677ecc = $(`<div id="html_bcc47c0647304452bc95a2d1fc677ecc" style="width: 100.0%; height: 100.0%;">Mauritania  6960  on 8/25/20</div>`)[0];
                popup_66cc93b69bd1409e9de2c630af7d3dd3.setContent(html_bcc47c0647304452bc95a2d1fc677ecc);
            

            circle_f3b7276b1ced45ee85acba1f556583b7.bindPopup(popup_66cc93b69bd1409e9de2c630af7d3dd3)
            ;

            
        
    

            var circle_eca3f03014e2478eb166fb9cfec19768 = L.circle(
                [-20.348404, 57.552152],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 174.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_96d346ae5ede470aa4aa3114f1229745 = L.popup({maxWidth: '100%'
            
            });

            
                var html_2b0f95cd80cd4b9daebdef202a759b3e = $(`<div id="html_2b0f95cd80cd4b9daebdef202a759b3e" style="width: 100.0%; height: 100.0%;">Mauritius  348  on 8/25/20</div>`)[0];
                popup_96d346ae5ede470aa4aa3114f1229745.setContent(html_2b0f95cd80cd4b9daebdef202a759b3e);
            

            circle_eca3f03014e2478eb166fb9cfec19768.bindPopup(popup_96d346ae5ede470aa4aa3114f1229745)
            ;

            
        
    

            var circle_d736da5c699149ac89af8df508bdf9a7 = L.circle(
                [23.6345, -102.5528],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 284310.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_eca1c5a8180b49718d1b78ffafd95938 = L.popup({maxWidth: '100%'
            
            });

            
                var html_69306eab64ef4003bc3555b340fae4a3 = $(`<div id="html_69306eab64ef4003bc3555b340fae4a3" style="width: 100.0%; height: 100.0%;">Mexico  568621  on 8/25/20</div>`)[0];
                popup_eca1c5a8180b49718d1b78ffafd95938.setContent(html_69306eab64ef4003bc3555b340fae4a3);
            

            circle_d736da5c699149ac89af8df508bdf9a7.bindPopup(popup_eca1c5a8180b49718d1b78ffafd95938)
            ;

            
        
    

            var circle_81338143752744e69a364d3d4f29769f = L.circle(
                [47.4116, 28.3699],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 17179.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3069a039466b466ba0d9fe35ac0531f5 = L.popup({maxWidth: '100%'
            
            });

            
                var html_383a23b7249d46eb937c0dca417ab56c = $(`<div id="html_383a23b7249d46eb937c0dca417ab56c" style="width: 100.0%; height: 100.0%;">Moldova  34358  on 8/25/20</div>`)[0];
                popup_3069a039466b466ba0d9fe35ac0531f5.setContent(html_383a23b7249d46eb937c0dca417ab56c);
            

            circle_81338143752744e69a364d3d4f29769f.bindPopup(popup_3069a039466b466ba0d9fe35ac0531f5)
            ;

            
        
    

            var circle_a8ae607e806d4180bd2dc41989e281d5 = L.circle(
                [43.7333, 7.4167],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 77.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_1bb62af157474ac69ed530cf049656e7 = L.popup({maxWidth: '100%'
            
            });

            
                var html_38ed8959b0c04e47b9334daa20317460 = $(`<div id="html_38ed8959b0c04e47b9334daa20317460" style="width: 100.0%; height: 100.0%;">Monaco  154  on 8/25/20</div>`)[0];
                popup_1bb62af157474ac69ed530cf049656e7.setContent(html_38ed8959b0c04e47b9334daa20317460);
            

            circle_a8ae607e806d4180bd2dc41989e281d5.bindPopup(popup_1bb62af157474ac69ed530cf049656e7)
            ;

            
        
    

            var circle_4ef05b27aefa4e9d9999bbdf64c1fed4 = L.circle(
                [46.8625, 103.8467],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 150.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8eb71ce3991541a1b93ca343fb91a864 = L.popup({maxWidth: '100%'
            
            });

            
                var html_b5ec7f9bc1524f0ba8488d5fc7109821 = $(`<div id="html_b5ec7f9bc1524f0ba8488d5fc7109821" style="width: 100.0%; height: 100.0%;">Mongolia  300  on 8/25/20</div>`)[0];
                popup_8eb71ce3991541a1b93ca343fb91a864.setContent(html_b5ec7f9bc1524f0ba8488d5fc7109821);
            

            circle_4ef05b27aefa4e9d9999bbdf64c1fed4.bindPopup(popup_8eb71ce3991541a1b93ca343fb91a864)
            ;

            
        
    

            var circle_1b620875b23a4495a466ce2e652cba28 = L.circle(
                [42.708678000000006, 19.37439],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2222.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a8c02cfaff7f4eee997a423cb5419c96 = L.popup({maxWidth: '100%'
            
            });

            
                var html_dd8a3c4c93424d4f8ee616c9a970f84f = $(`<div id="html_dd8a3c4c93424d4f8ee616c9a970f84f" style="width: 100.0%; height: 100.0%;">Montenegro  4444  on 8/25/20</div>`)[0];
                popup_a8c02cfaff7f4eee997a423cb5419c96.setContent(html_dd8a3c4c93424d4f8ee616c9a970f84f);
            

            circle_1b620875b23a4495a466ce2e652cba28.bindPopup(popup_a8c02cfaff7f4eee997a423cb5419c96)
            ;

            
        
    

            var circle_4a5940e1ea2e41f68db81e98142e0fa7 = L.circle(
                [31.7917, -7.0926],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 27264.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b9c40185ca974b158777a97dc560e88c = L.popup({maxWidth: '100%'
            
            });

            
                var html_60b8de8c3cff40e5bc304e77a017fca6 = $(`<div id="html_60b8de8c3cff40e5bc304e77a017fca6" style="width: 100.0%; height: 100.0%;">Morocco  54528  on 8/25/20</div>`)[0];
                popup_b9c40185ca974b158777a97dc560e88c.setContent(html_60b8de8c3cff40e5bc304e77a017fca6);
            

            circle_4a5940e1ea2e41f68db81e98142e0fa7.bindPopup(popup_b9c40185ca974b158777a97dc560e88c)
            ;

            
        
    

            var circle_e17c6a2c093f4aee8918ed2305096d9b = L.circle(
                [-18.665695, 35.529562],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1754.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_93b2029a259a4b1ca70841f2f1fd83cb = L.popup({maxWidth: '100%'
            
            });

            
                var html_95a42564a39d47af8478ce27d754ccb3 = $(`<div id="html_95a42564a39d47af8478ce27d754ccb3" style="width: 100.0%; height: 100.0%;">Mozambique  3508  on 8/25/20</div>`)[0];
                popup_93b2029a259a4b1ca70841f2f1fd83cb.setContent(html_95a42564a39d47af8478ce27d754ccb3);
            

            circle_e17c6a2c093f4aee8918ed2305096d9b.bindPopup(popup_93b2029a259a4b1ca70841f2f1fd83cb)
            ;

            
        
    

            var circle_ca17cc9bbe5b43b8a8461fa7a057ef97 = L.circle(
                [-22.9576, 18.4904],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3080.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_143fe062b92d4019b146b9a2757366ce = L.popup({maxWidth: '100%'
            
            });

            
                var html_7126d71a708140ea9f3f4fcfbb51bc83 = $(`<div id="html_7126d71a708140ea9f3f4fcfbb51bc83" style="width: 100.0%; height: 100.0%;">Namibia  6160  on 8/25/20</div>`)[0];
                popup_143fe062b92d4019b146b9a2757366ce.setContent(html_7126d71a708140ea9f3f4fcfbb51bc83);
            

            circle_ca17cc9bbe5b43b8a8461fa7a057ef97.bindPopup(popup_143fe062b92d4019b146b9a2757366ce)
            ;

            
        
    

            var circle_d40d7591fdd445078da8606431f986a7 = L.circle(
                [28.1667, 84.25],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 16766.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3df98367f08f4e84b99f5db1ef08eb5d = L.popup({maxWidth: '100%'
            
            });

            
                var html_2309bf2f14054d068f7f6e525e910d04 = $(`<div id="html_2309bf2f14054d068f7f6e525e910d04" style="width: 100.0%; height: 100.0%;">Nepal  33533  on 8/25/20</div>`)[0];
                popup_3df98367f08f4e84b99f5db1ef08eb5d.setContent(html_2309bf2f14054d068f7f6e525e910d04);
            

            circle_d40d7591fdd445078da8606431f986a7.bindPopup(popup_3df98367f08f4e84b99f5db1ef08eb5d)
            ;

            
        
    

            var circle_f7fcd2b103e9420ca728a258afb3b135 = L.circle(
                [107.0442, -264.9603],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 34841.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_443a63d00cbf43aca50e9a765660b39f = L.popup({maxWidth: '100%'
            
            });

            
                var html_986e133077e54f17acaee615995510e7 = $(`<div id="html_986e133077e54f17acaee615995510e7" style="width: 100.0%; height: 100.0%;">Netherlands  69683  on 8/25/20</div>`)[0];
                popup_443a63d00cbf43aca50e9a765660b39f.setContent(html_986e133077e54f17acaee615995510e7);
            

            circle_f7fcd2b103e9420ca728a258afb3b135.bindPopup(popup_443a63d00cbf43aca50e9a765660b39f)
            ;

            
        
    

            var circle_fafe8bb181d34669a2b8a199b90998c5 = L.circle(
                [-40.9006, 174.886],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 847.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_6706350e67cf4017bf3b10204cff55d9 = L.popup({maxWidth: '100%'
            
            });

            
                var html_484077e3cbe54a98bf6ddb2971a15db8 = $(`<div id="html_484077e3cbe54a98bf6ddb2971a15db8" style="width: 100.0%; height: 100.0%;">New Zealand  1695  on 8/25/20</div>`)[0];
                popup_6706350e67cf4017bf3b10204cff55d9.setContent(html_484077e3cbe54a98bf6ddb2971a15db8);
            

            circle_fafe8bb181d34669a2b8a199b90998c5.bindPopup(popup_6706350e67cf4017bf3b10204cff55d9)
            ;

            
        
    

            var circle_fc4b2ac984f245b9a29c8754b9613c6b = L.circle(
                [12.865416, -85.207229],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2247.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_88b1927cc1764e78b0861465c16f405b = L.popup({maxWidth: '100%'
            
            });

            
                var html_2e5a7df22ddc476fa9f86b2ac480334e = $(`<div id="html_2e5a7df22ddc476fa9f86b2ac480334e" style="width: 100.0%; height: 100.0%;">Nicaragua  4494  on 8/25/20</div>`)[0];
                popup_88b1927cc1764e78b0861465c16f405b.setContent(html_2e5a7df22ddc476fa9f86b2ac480334e);
            

            circle_fc4b2ac984f245b9a29c8754b9613c6b.bindPopup(popup_88b1927cc1764e78b0861465c16f405b)
            ;

            
        
    

            var circle_b547acad60a4437ba9b2b65be643dc1c = L.circle(
                [17.607789, 8.081666],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 586.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cfd8469fb97b4a31b452ea179288bbc2 = L.popup({maxWidth: '100%'
            
            });

            
                var html_148276d042a944f08fed16b9c7c819d4 = $(`<div id="html_148276d042a944f08fed16b9c7c819d4" style="width: 100.0%; height: 100.0%;">Niger  1173  on 8/25/20</div>`)[0];
                popup_cfd8469fb97b4a31b452ea179288bbc2.setContent(html_148276d042a944f08fed16b9c7c819d4);
            

            circle_b547acad60a4437ba9b2b65be643dc1c.bindPopup(popup_cfd8469fb97b4a31b452ea179288bbc2)
            ;

            
        
    

            var circle_6c381c821d344ae5907b0b3cffe72989 = L.circle(
                [9.082, 8.6753],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 26400.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7a1e4b7da6624f05860b3db09c1072bc = L.popup({maxWidth: '100%'
            
            });

            
                var html_1e275a57068f49fe917cf4e599550b07 = $(`<div id="html_1e275a57068f49fe917cf4e599550b07" style="width: 100.0%; height: 100.0%;">Nigeria  52800  on 8/25/20</div>`)[0];
                popup_7a1e4b7da6624f05860b3db09c1072bc.setContent(html_1e275a57068f49fe917cf4e599550b07);
            

            circle_6c381c821d344ae5907b0b3cffe72989.bindPopup(popup_7a1e4b7da6624f05860b3db09c1072bc)
            ;

            
        
    

            var circle_86243c655cac481e936953c7d926d1d3 = L.circle(
                [41.6086, 21.7453],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6899.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_bd2f1027073047b0865d57a64cc01ff9 = L.popup({maxWidth: '100%'
            
            });

            
                var html_68de90b6ff054d33971f59ea08ab30fa = $(`<div id="html_68de90b6ff054d33971f59ea08ab30fa" style="width: 100.0%; height: 100.0%;">North Macedonia  13799  on 8/25/20</div>`)[0];
                popup_bd2f1027073047b0865d57a64cc01ff9.setContent(html_68de90b6ff054d33971f59ea08ab30fa);
            

            circle_86243c655cac481e936953c7d926d1d3.bindPopup(popup_bd2f1027073047b0865d57a64cc01ff9)
            ;

            
        
    

            var circle_5686b194710c427b8ca1a50caafa2d19 = L.circle(
                [60.472, 8.4689],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5227.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_7e3c571cd6314ca8b12879f2477a897b = L.popup({maxWidth: '100%'
            
            });

            
                var html_96466bae36684521b096213cb3b46877 = $(`<div id="html_96466bae36684521b096213cb3b46877" style="width: 100.0%; height: 100.0%;">Norway  10454  on 8/25/20</div>`)[0];
                popup_7e3c571cd6314ca8b12879f2477a897b.setContent(html_96466bae36684521b096213cb3b46877);
            

            circle_5686b194710c427b8ca1a50caafa2d19.bindPopup(popup_7e3c571cd6314ca8b12879f2477a897b)
            ;

            
        
    

            var circle_7986a954fe6e4892b1796e1e97925846 = L.circle(
                [21.512583, 55.92325500000001],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 42326.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_c9c3c206d67043a8b33e0f1520aa44e6 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f23252f10bce4114b43e927ce6ffcb02 = $(`<div id="html_f23252f10bce4114b43e927ce6ffcb02" style="width: 100.0%; height: 100.0%;">Oman  84652  on 8/25/20</div>`)[0];
                popup_c9c3c206d67043a8b33e0f1520aa44e6.setContent(html_f23252f10bce4114b43e927ce6ffcb02);
            

            circle_7986a954fe6e4892b1796e1e97925846.bindPopup(popup_c9c3c206d67043a8b33e0f1520aa44e6)
            ;

            
        
    

            var circle_928aaf1ee461477baaaabde091e3ca7f = L.circle(
                [30.3753, 69.3451],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 146855.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ed87593ab73f403e975f139e7b1712ce = L.popup({maxWidth: '100%'
            
            });

            
                var html_c75acb1f767845d8b7b274a35071f6ed = $(`<div id="html_c75acb1f767845d8b7b274a35071f6ed" style="width: 100.0%; height: 100.0%;">Pakistan  293711  on 8/25/20</div>`)[0];
                popup_ed87593ab73f403e975f139e7b1712ce.setContent(html_c75acb1f767845d8b7b274a35071f6ed);
            

            circle_928aaf1ee461477baaaabde091e3ca7f.bindPopup(popup_ed87593ab73f403e975f139e7b1712ce)
            ;

            
        
    

            var circle_332ba4ec868b4f37b7f650c88c19ab3a = L.circle(
                [8.538, -80.7821],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 44190.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_de411a30397846c5b2e66f9e9f8423aa = L.popup({maxWidth: '100%'
            
            });

            
                var html_3d9eab4dc5d14030a7d767f5544f6470 = $(`<div id="html_3d9eab4dc5d14030a7d767f5544f6470" style="width: 100.0%; height: 100.0%;">Panama  88381  on 8/25/20</div>`)[0];
                popup_de411a30397846c5b2e66f9e9f8423aa.setContent(html_3d9eab4dc5d14030a7d767f5544f6470);
            

            circle_332ba4ec868b4f37b7f650c88c19ab3a.bindPopup(popup_de411a30397846c5b2e66f9e9f8423aa)
            ;

            
        
    

            var circle_f4ec0d7fc0404af1be2e570ae75c2ab3 = L.circle(
                [-6.314993, 143.95555],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 209.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8548986bcd0f4a7ba5c54eb23c66aceb = L.popup({maxWidth: '100%'
            
            });

            
                var html_b69cd05c0ae04a4c90803866571a59bf = $(`<div id="html_b69cd05c0ae04a4c90803866571a59bf" style="width: 100.0%; height: 100.0%;">Papua New Guinea  419  on 8/25/20</div>`)[0];
                popup_8548986bcd0f4a7ba5c54eb23c66aceb.setContent(html_b69cd05c0ae04a4c90803866571a59bf);
            

            circle_f4ec0d7fc0404af1be2e570ae75c2ab3.bindPopup(popup_8548986bcd0f4a7ba5c54eb23c66aceb)
            ;

            
        
    

            var circle_bce73d080d3f4621bee5504a6e391e45 = L.circle(
                [-23.4425, -58.4438],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 7114.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_ce74bc1e4ee54dc28885fbad7e41519d = L.popup({maxWidth: '100%'
            
            });

            
                var html_58d97b91465e4c1b903facd28c4dacf1 = $(`<div id="html_58d97b91465e4c1b903facd28c4dacf1" style="width: 100.0%; height: 100.0%;">Paraguay  14228  on 8/25/20</div>`)[0];
                popup_ce74bc1e4ee54dc28885fbad7e41519d.setContent(html_58d97b91465e4c1b903facd28c4dacf1);
            

            circle_bce73d080d3f4621bee5504a6e391e45.bindPopup(popup_ce74bc1e4ee54dc28885fbad7e41519d)
            ;

            
        
    

            var circle_37a7d3d79e0e4771b49e5e3a97357b25 = L.circle(
                [-9.19, -75.0152],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 300219.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e0ba375b895d4f2492792e25cc8bc9c4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_49238f8efeb740648bad7da2d3eb9358 = $(`<div id="html_49238f8efeb740648bad7da2d3eb9358" style="width: 100.0%; height: 100.0%;">Peru  600438  on 8/25/20</div>`)[0];
                popup_e0ba375b895d4f2492792e25cc8bc9c4.setContent(html_49238f8efeb740648bad7da2d3eb9358);
            

            circle_37a7d3d79e0e4771b49e5e3a97357b25.bindPopup(popup_e0ba375b895d4f2492792e25cc8bc9c4)
            ;

            
        
    

            var circle_1303a64462a248778e53458e723fd152 = L.circle(
                [12.879721, 121.774017],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 98582.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9b748958aa5c4a79815d5755fa3fc480 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ce30c7cdeca045aca7539247a484ae97 = $(`<div id="html_ce30c7cdeca045aca7539247a484ae97" style="width: 100.0%; height: 100.0%;">Philippines  197164  on 8/25/20</div>`)[0];
                popup_9b748958aa5c4a79815d5755fa3fc480.setContent(html_ce30c7cdeca045aca7539247a484ae97);
            

            circle_1303a64462a248778e53458e723fd152.bindPopup(popup_9b748958aa5c4a79815d5755fa3fc480)
            ;

            
        
    

            var circle_9d74e79e8c29430bbc9515fa340a3117 = L.circle(
                [51.9194, 19.1451],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 31536.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e4f8635009854a64b397a112c063dbf4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9442da8b7cc9444f85e3c4f7165b0122 = $(`<div id="html_9442da8b7cc9444f85e3c4f7165b0122" style="width: 100.0%; height: 100.0%;">Poland  63073  on 8/25/20</div>`)[0];
                popup_e4f8635009854a64b397a112c063dbf4.setContent(html_9442da8b7cc9444f85e3c4f7165b0122);
            

            circle_9d74e79e8c29430bbc9515fa340a3117.bindPopup(popup_e4f8635009854a64b397a112c063dbf4)
            ;

            
        
    

            var circle_bd66e3d41bec4f97bdbedf4d64f973b2 = L.circle(
                [39.3999, -8.2245],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 27956.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_c53b18a928a44ceeb492cb470d86d3ec = L.popup({maxWidth: '100%'
            
            });

            
                var html_30196b46bca04bfcae011358d22be878 = $(`<div id="html_30196b46bca04bfcae011358d22be878" style="width: 100.0%; height: 100.0%;">Portugal  55912  on 8/25/20</div>`)[0];
                popup_c53b18a928a44ceeb492cb470d86d3ec.setContent(html_30196b46bca04bfcae011358d22be878);
            

            circle_bd66e3d41bec4f97bdbedf4d64f973b2.bindPopup(popup_c53b18a928a44ceeb492cb470d86d3ec)
            ;

            
        
    

            var circle_3da0ad323e5648b19202371f5d524c3c = L.circle(
                [25.3548, 51.1839],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 58749.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8f7822ff3793431cb771e434a9a44eb6 = L.popup({maxWidth: '100%'
            
            });

            
                var html_6a7ef70da29c42e39c480ee1ba1f060d = $(`<div id="html_6a7ef70da29c42e39c480ee1ba1f060d" style="width: 100.0%; height: 100.0%;">Qatar  117498  on 8/25/20</div>`)[0];
                popup_8f7822ff3793431cb771e434a9a44eb6.setContent(html_6a7ef70da29c42e39c480ee1ba1f060d);
            

            circle_3da0ad323e5648b19202371f5d524c3c.bindPopup(popup_8f7822ff3793431cb771e434a9a44eb6)
            ;

            
        
    

            var circle_a25437b277af4d1b8d9c644cec00fe52 = L.circle(
                [45.9432, 24.9668],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 40195.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9fb6093bf64b48e086695f0477c340f6 = L.popup({maxWidth: '100%'
            
            });

            
                var html_5509c6fa45fe404b9d28a8f145d6111a = $(`<div id="html_5509c6fa45fe404b9d28a8f145d6111a" style="width: 100.0%; height: 100.0%;">Romania  80390  on 8/25/20</div>`)[0];
                popup_9fb6093bf64b48e086695f0477c340f6.setContent(html_5509c6fa45fe404b9d28a8f145d6111a);
            

            circle_a25437b277af4d1b8d9c644cec00fe52.bindPopup(popup_9fb6093bf64b48e086695f0477c340f6)
            ;

            
        
    

            var circle_3a675f435696455faefbca24f6db1f32 = L.circle(
                [61.52401, 105.318756],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 481827.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_fac181dfa33e4609907033d8a90bfb19 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a60d5bd0719045eb84541f3c52966f0a = $(`<div id="html_a60d5bd0719045eb84541f3c52966f0a" style="width: 100.0%; height: 100.0%;">Russia  963655  on 8/25/20</div>`)[0];
                popup_fac181dfa33e4609907033d8a90bfb19.setContent(html_a60d5bd0719045eb84541f3c52966f0a);
            

            circle_3a675f435696455faefbca24f6db1f32.bindPopup(popup_fac181dfa33e4609907033d8a90bfb19)
            ;

            
        
    

            var circle_d39f44dbcd4c4b3885020da632a4c4e1 = L.circle(
                [-1.9403, 29.8739],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1768.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0bc58e776eb143e0be4f90762958ad2c = L.popup({maxWidth: '100%'
            
            });

            
                var html_0450f1fb2fbd4e4f82bf5f0a4fe4dfa9 = $(`<div id="html_0450f1fb2fbd4e4f82bf5f0a4fe4dfa9" style="width: 100.0%; height: 100.0%;">Rwanda  3537  on 8/25/20</div>`)[0];
                popup_0bc58e776eb143e0be4f90762958ad2c.setContent(html_0450f1fb2fbd4e4f82bf5f0a4fe4dfa9);
            

            circle_d39f44dbcd4c4b3885020da632a4c4e1.bindPopup(popup_0bc58e776eb143e0be4f90762958ad2c)
            ;

            
        
    

            var circle_a71f695b978348a5a6fb9dd5afaa92d0 = L.circle(
                [17.357822, -62.782998],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 8.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2d668e506526456d9179b72af6420042 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d279195a9e9c4a03afb3ab8bff26519a = $(`<div id="html_d279195a9e9c4a03afb3ab8bff26519a" style="width: 100.0%; height: 100.0%;">Saint Kitts and Nevis  17  on 8/25/20</div>`)[0];
                popup_2d668e506526456d9179b72af6420042.setContent(html_d279195a9e9c4a03afb3ab8bff26519a);
            

            circle_a71f695b978348a5a6fb9dd5afaa92d0.bindPopup(popup_2d668e506526456d9179b72af6420042)
            ;

            
        
    

            var circle_8c979d3293554dafb06e5e120c9a0eb3 = L.circle(
                [13.9094, -60.9789],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 13.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_833eae47162043068b058a0159c5f9ad = L.popup({maxWidth: '100%'
            
            });

            
                var html_438545fed44e40a5b46295536fcf1114 = $(`<div id="html_438545fed44e40a5b46295536fcf1114" style="width: 100.0%; height: 100.0%;">Saint Lucia  26  on 8/25/20</div>`)[0];
                popup_833eae47162043068b058a0159c5f9ad.setContent(html_438545fed44e40a5b46295536fcf1114);
            

            circle_8c979d3293554dafb06e5e120c9a0eb3.bindPopup(popup_833eae47162043068b058a0159c5f9ad)
            ;

            
        
    

            var circle_947e19cfc71848b4b8c78f3644e1253f = L.circle(
                [12.9843, -61.2872],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 29.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4c0289b1cb5b42ae8cb825be1c6b75d4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_1e65652292424fe7bdfd2c679391995d = $(`<div id="html_1e65652292424fe7bdfd2c679391995d" style="width: 100.0%; height: 100.0%;">Saint Vincent and the Grenadines  58  on 8/25/20</div>`)[0];
                popup_4c0289b1cb5b42ae8cb825be1c6b75d4.setContent(html_1e65652292424fe7bdfd2c679391995d);
            

            circle_947e19cfc71848b4b8c78f3644e1253f.bindPopup(popup_4c0289b1cb5b42ae8cb825be1c6b75d4)
            ;

            
        
    

            var circle_dd2ed5ea48b14507a6d53eda94aa5883 = L.circle(
                [43.9424, 12.4578],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 355.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_e7a3ab032ea04ac9af018aa699199fad = L.popup({maxWidth: '100%'
            
            });

            
                var html_d8c7281da0ff4528a65fe7a6c1b136cb = $(`<div id="html_d8c7281da0ff4528a65fe7a6c1b136cb" style="width: 100.0%; height: 100.0%;">San Marino  710  on 8/25/20</div>`)[0];
                popup_e7a3ab032ea04ac9af018aa699199fad.setContent(html_d8c7281da0ff4528a65fe7a6c1b136cb);
            

            circle_dd2ed5ea48b14507a6d53eda94aa5883.bindPopup(popup_e7a3ab032ea04ac9af018aa699199fad)
            ;

            
        
    

            var circle_3b8bf02e43594f2eb52649c35271f6c0 = L.circle(
                [0.1864, 6.6131],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 446.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cffbdefcd0df42af9ecdf2ae40b29d66 = L.popup({maxWidth: '100%'
            
            });

            
                var html_4d483ec454944d6aaeb0a8ab31d64073 = $(`<div id="html_4d483ec454944d6aaeb0a8ab31d64073" style="width: 100.0%; height: 100.0%;">Sao Tome and Principe  892  on 8/25/20</div>`)[0];
                popup_cffbdefcd0df42af9ecdf2ae40b29d66.setContent(html_4d483ec454944d6aaeb0a8ab31d64073);
            

            circle_3b8bf02e43594f2eb52649c35271f6c0.bindPopup(popup_cffbdefcd0df42af9ecdf2ae40b29d66)
            ;

            
        
    

            var circle_007133238141404999ed7f5a2bf7bf9b = L.circle(
                [23.885942, 45.079162],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 154884.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_21ed3a02449141f5b3e935900fab664e = L.popup({maxWidth: '100%'
            
            });

            
                var html_8640a96354724c148b9c5540c33b833f = $(`<div id="html_8640a96354724c148b9c5540c33b833f" style="width: 100.0%; height: 100.0%;">Saudi Arabia  309768  on 8/25/20</div>`)[0];
                popup_21ed3a02449141f5b3e935900fab664e.setContent(html_8640a96354724c148b9c5540c33b833f);
            

            circle_007133238141404999ed7f5a2bf7bf9b.bindPopup(popup_21ed3a02449141f5b3e935900fab664e)
            ;

            
        
    

            var circle_250f4654e4324633b5efdba4b5885234 = L.circle(
                [14.4974, -14.4524],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6528.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_23e49eb9f7a24a7daa7a8d7f4a742081 = L.popup({maxWidth: '100%'
            
            });

            
                var html_22d049278df34f04a578e99c73be558d = $(`<div id="html_22d049278df34f04a578e99c73be558d" style="width: 100.0%; height: 100.0%;">Senegal  13056  on 8/25/20</div>`)[0];
                popup_23e49eb9f7a24a7daa7a8d7f4a742081.setContent(html_22d049278df34f04a578e99c73be558d);
            

            circle_250f4654e4324633b5efdba4b5885234.bindPopup(popup_23e49eb9f7a24a7daa7a8d7f4a742081)
            ;

            
        
    

            var circle_70d37c5335784248ba125503e4093ffb = L.circle(
                [44.0165, 21.0059],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 15410.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8286fddd79dd42c69e273e9ff668f87c = L.popup({maxWidth: '100%'
            
            });

            
                var html_19707ad21ffd4da8a6033c9128e189d8 = $(`<div id="html_19707ad21ffd4da8a6033c9128e189d8" style="width: 100.0%; height: 100.0%;">Serbia  30820  on 8/25/20</div>`)[0];
                popup_8286fddd79dd42c69e273e9ff668f87c.setContent(html_19707ad21ffd4da8a6033c9128e189d8);
            

            circle_70d37c5335784248ba125503e4093ffb.bindPopup(popup_8286fddd79dd42c69e273e9ff668f87c)
            ;

            
        
    

            var circle_cf835e640bb34b758c4d9e00fd1c7f21 = L.circle(
                [-4.6796, 55.492],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 68.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2038c7ffc23742bcbf6ac1f34d833301 = L.popup({maxWidth: '100%'
            
            });

            
                var html_b938945facc3457598bf61ce169e77d3 = $(`<div id="html_b938945facc3457598bf61ce169e77d3" style="width: 100.0%; height: 100.0%;">Seychelles  136  on 8/25/20</div>`)[0];
                popup_2038c7ffc23742bcbf6ac1f34d833301.setContent(html_b938945facc3457598bf61ce169e77d3);
            

            circle_cf835e640bb34b758c4d9e00fd1c7f21.bindPopup(popup_2038c7ffc23742bcbf6ac1f34d833301)
            ;

            
        
    

            var circle_854eed9a417644e0b7926841ee7b993e = L.circle(
                [8.460555000000001, -11.779889],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1000.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_63bc265a036d47e4948a3ffcab9f4ad8 = L.popup({maxWidth: '100%'
            
            });

            
                var html_dbf0f77228744326a331464f60f51f83 = $(`<div id="html_dbf0f77228744326a331464f60f51f83" style="width: 100.0%; height: 100.0%;">Sierra Leone  2001  on 8/25/20</div>`)[0];
                popup_63bc265a036d47e4948a3ffcab9f4ad8.setContent(html_dbf0f77228744326a331464f60f51f83);
            

            circle_854eed9a417644e0b7926841ee7b993e.bindPopup(popup_63bc265a036d47e4948a3ffcab9f4ad8)
            ;

            
        
    

            var circle_23342004b706411b9e870a64820c1c47 = L.circle(
                [1.2833, 103.8333],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 28217.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_aba328ff2fb6484d8dcaa46c53e152c3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_33d3099743914de7b71ae61839527762 = $(`<div id="html_33d3099743914de7b71ae61839527762" style="width: 100.0%; height: 100.0%;">Singapore  56435  on 8/25/20</div>`)[0];
                popup_aba328ff2fb6484d8dcaa46c53e152c3.setContent(html_33d3099743914de7b71ae61839527762);
            

            circle_23342004b706411b9e870a64820c1c47.bindPopup(popup_aba328ff2fb6484d8dcaa46c53e152c3)
            ;

            
        
    

            var circle_26302e1c6bab45d49c830994ccd16e7a = L.circle(
                [48.669, 19.699],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1726.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3a6ee5835dbc4244a8bfafc28e4ee3a6 = L.popup({maxWidth: '100%'
            
            });

            
                var html_2f0747a18fd54580b2f434491e19157d = $(`<div id="html_2f0747a18fd54580b2f434491e19157d" style="width: 100.0%; height: 100.0%;">Slovakia  3452  on 8/25/20</div>`)[0];
                popup_3a6ee5835dbc4244a8bfafc28e4ee3a6.setContent(html_2f0747a18fd54580b2f434491e19157d);
            

            circle_26302e1c6bab45d49c830994ccd16e7a.bindPopup(popup_3a6ee5835dbc4244a8bfafc28e4ee3a6)
            ;

            
        
    

            var circle_76ee432155594e638606aa29c1bb34c0 = L.circle(
                [46.1512, 14.9955],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1343.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f94457920ff544439f3a13b914d0dc15 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a44835c09ec04e16aad600dbffd0a3e0 = $(`<div id="html_a44835c09ec04e16aad600dbffd0a3e0" style="width: 100.0%; height: 100.0%;">Slovenia  2686  on 8/25/20</div>`)[0];
                popup_f94457920ff544439f3a13b914d0dc15.setContent(html_a44835c09ec04e16aad600dbffd0a3e0);
            

            circle_76ee432155594e638606aa29c1bb34c0.bindPopup(popup_f94457920ff544439f3a13b914d0dc15)
            ;

            
        
    

            var circle_e6e1d29168104323ae5ab3b89b7bb95e = L.circle(
                [5.152149, 46.199616],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1637.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_881ebc08aa1c4b649604180074f770a9 = L.popup({maxWidth: '100%'
            
            });

            
                var html_9e992188712645e98c50046245520d50 = $(`<div id="html_9e992188712645e98c50046245520d50" style="width: 100.0%; height: 100.0%;">Somalia  3275  on 8/25/20</div>`)[0];
                popup_881ebc08aa1c4b649604180074f770a9.setContent(html_9e992188712645e98c50046245520d50);
            

            circle_e6e1d29168104323ae5ab3b89b7bb95e.bindPopup(popup_881ebc08aa1c4b649604180074f770a9)
            ;

            
        
    

            var circle_42963312550d43b2aaed0d0d4e9f4e65 = L.circle(
                [-30.5595, 22.9375],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 306508.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_bce9c78366a14e4c81244c39109544c4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c5903869945b4934a1d7582ca195fe99 = $(`<div id="html_c5903869945b4934a1d7582ca195fe99" style="width: 100.0%; height: 100.0%;">South Africa  613017  on 8/25/20</div>`)[0];
                popup_bce9c78366a14e4c81244c39109544c4.setContent(html_c5903869945b4934a1d7582ca195fe99);
            

            circle_42963312550d43b2aaed0d0d4e9f4e65.bindPopup(popup_bce9c78366a14e4c81244c39109544c4)
            ;

            
        
    

            var circle_52080566ac3e4dc9bb4493d108393c4e = L.circle(
                [6.877000000000002, 31.307],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1253.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_d194ecd150894e2fa7f728b059309711 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f5b5b51dc649458e9194390d2dac0bb6 = $(`<div id="html_f5b5b51dc649458e9194390d2dac0bb6" style="width: 100.0%; height: 100.0%;">South Sudan  2507  on 8/25/20</div>`)[0];
                popup_d194ecd150894e2fa7f728b059309711.setContent(html_f5b5b51dc649458e9194390d2dac0bb6);
            

            circle_52080566ac3e4dc9bb4493d108393c4e.bindPopup(popup_d194ecd150894e2fa7f728b059309711)
            ;

            
        
    

            var circle_fc7ae01af4e54c35ae29cce42b7bb4a7 = L.circle(
                [40.463667, -3.74922],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 206276.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_b739ff8d171242a3a109985e3ab57916 = L.popup({maxWidth: '100%'
            
            });

            
                var html_5043d79d0d7e4cad9713c59f894bd536 = $(`<div id="html_5043d79d0d7e4cad9713c59f894bd536" style="width: 100.0%; height: 100.0%;">Spain  412553  on 8/25/20</div>`)[0];
                popup_b739ff8d171242a3a109985e3ab57916.setContent(html_5043d79d0d7e4cad9713c59f894bd536);
            

            circle_fc7ae01af4e54c35ae29cce42b7bb4a7.bindPopup(popup_b739ff8d171242a3a109985e3ab57916)
            ;

            
        
    

            var circle_0c7b64283a06438c82dd2205dc1c06ee = L.circle(
                [7.873054, 80.77179699999998],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1485.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_1d45c5ec7b754a4987bb0132c41c3983 = L.popup({maxWidth: '100%'
            
            });

            
                var html_1747d180ee5f44d58e0ca80873256af8 = $(`<div id="html_1747d180ee5f44d58e0ca80873256af8" style="width: 100.0%; height: 100.0%;">Sri Lanka  2971  on 8/25/20</div>`)[0];
                popup_1d45c5ec7b754a4987bb0132c41c3983.setContent(html_1747d180ee5f44d58e0ca80873256af8);
            

            circle_0c7b64283a06438c82dd2205dc1c06ee.bindPopup(popup_1d45c5ec7b754a4987bb0132c41c3983)
            ;

            
        
    

            var circle_d7627e806d424ce5a0ea569d20ef6ddf = L.circle(
                [12.8628, 30.2176],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 6487.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_d75cf9546d4447f6ad786b8afab29436 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c8e9259c83ec43319753a5d224f59043 = $(`<div id="html_c8e9259c83ec43319753a5d224f59043" style="width: 100.0%; height: 100.0%;">Sudan  12974  on 8/25/20</div>`)[0];
                popup_d75cf9546d4447f6ad786b8afab29436.setContent(html_c8e9259c83ec43319753a5d224f59043);
            

            circle_d7627e806d424ce5a0ea569d20ef6ddf.bindPopup(popup_d75cf9546d4447f6ad786b8afab29436)
            ;

            
        
    

            var circle_756efbbb490f43ff922ce872324b8916 = L.circle(
                [3.9193, -56.0278],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1849.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_36c15e30e55944e7b54ba88b110205fe = L.popup({maxWidth: '100%'
            
            });

            
                var html_9ebe893208bc4952af50e547dfcc73b8 = $(`<div id="html_9ebe893208bc4952af50e547dfcc73b8" style="width: 100.0%; height: 100.0%;">Suriname  3698  on 8/25/20</div>`)[0];
                popup_36c15e30e55944e7b54ba88b110205fe.setContent(html_9ebe893208bc4952af50e547dfcc73b8);
            

            circle_756efbbb490f43ff922ce872324b8916.bindPopup(popup_36c15e30e55944e7b54ba88b110205fe)
            ;

            
        
    

            var circle_de7bb0379bad4f1aa1aa784726847866 = L.circle(
                [60.128161, 18.643501],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 43445.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_0d2e84e77ad04db6a589f53556e32b0b = L.popup({maxWidth: '100%'
            
            });

            
                var html_77a9aad08f874d5791d6938111dfda03 = $(`<div id="html_77a9aad08f874d5791d6938111dfda03" style="width: 100.0%; height: 100.0%;">Sweden  86891  on 8/25/20</div>`)[0];
                popup_0d2e84e77ad04db6a589f53556e32b0b.setContent(html_77a9aad08f874d5791d6938111dfda03);
            

            circle_de7bb0379bad4f1aa1aa784726847866.bindPopup(popup_0d2e84e77ad04db6a589f53556e32b0b)
            ;

            
        
    

            var circle_c8a19a763df848ada9251fd9db97c202 = L.circle(
                [46.8182, 8.2275],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 20131.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_2dad870a48884521b4eb23845e5fe930 = L.popup({maxWidth: '100%'
            
            });

            
                var html_a0369be7035246b79bf8277a8ef1ecff = $(`<div id="html_a0369be7035246b79bf8277a8ef1ecff" style="width: 100.0%; height: 100.0%;">Switzerland  40262  on 8/25/20</div>`)[0];
                popup_2dad870a48884521b4eb23845e5fe930.setContent(html_a0369be7035246b79bf8277a8ef1ecff);
            

            circle_c8a19a763df848ada9251fd9db97c202.bindPopup(popup_2dad870a48884521b4eb23845e5fe930)
            ;

            
        
    

            var circle_64a8de2b720e4126908118c87f5f7a32 = L.circle(
                [34.802075, 38.99681500000001],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1182.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4c9e3dfabff5427589f7bafbb3b5a7b3 = L.popup({maxWidth: '100%'
            
            });

            
                var html_03edaf59e13045c4bade2bf3ff50305a = $(`<div id="html_03edaf59e13045c4bade2bf3ff50305a" style="width: 100.0%; height: 100.0%;">Syria  2365  on 8/25/20</div>`)[0];
                popup_4c9e3dfabff5427589f7bafbb3b5a7b3.setContent(html_03edaf59e13045c4bade2bf3ff50305a);
            

            circle_64a8de2b720e4126908118c87f5f7a32.bindPopup(popup_4c9e3dfabff5427589f7bafbb3b5a7b3)
            ;

            
        
    

            var circle_c97d77e03f69488db21a97fdcd80edb7 = L.circle(
                [23.7, 121.0],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 243.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_3edba8a07e034b0c9ca104096ac2081f = L.popup({maxWidth: '100%'
            
            });

            
                var html_64ebbd227a6b48e5ae45b3275172d47b = $(`<div id="html_64ebbd227a6b48e5ae45b3275172d47b" style="width: 100.0%; height: 100.0%;">Taiwan*  487  on 8/25/20</div>`)[0];
                popup_3edba8a07e034b0c9ca104096ac2081f.setContent(html_64ebbd227a6b48e5ae45b3275172d47b);
            

            circle_c97d77e03f69488db21a97fdcd80edb7.bindPopup(popup_3edba8a07e034b0c9ca104096ac2081f)
            ;

            
        
    

            var circle_3ef4b7803b524c86b3132b96aa8f06b0 = L.circle(
                [38.861, 71.2761],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 4189.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cf7ab46eab534c8aafb9a5c9544ab799 = L.popup({maxWidth: '100%'
            
            });

            
                var html_eab5bea66d0941ad88b2b364344b99f1 = $(`<div id="html_eab5bea66d0941ad88b2b364344b99f1" style="width: 100.0%; height: 100.0%;">Tajikistan  8379  on 8/25/20</div>`)[0];
                popup_cf7ab46eab534c8aafb9a5c9544ab799.setContent(html_eab5bea66d0941ad88b2b364344b99f1);
            

            circle_3ef4b7803b524c86b3132b96aa8f06b0.bindPopup(popup_cf7ab46eab534c8aafb9a5c9544ab799)
            ;

            
        
    

            var circle_f7690d715c064e4d8cd2ff18dad5cbab = L.circle(
                [-6.369028, 34.888822],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 254.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_97322e2f4c404a7fa2c3f1bae9029469 = L.popup({maxWidth: '100%'
            
            });

            
                var html_d9246150295a4c879595210b3a791a00 = $(`<div id="html_d9246150295a4c879595210b3a791a00" style="width: 100.0%; height: 100.0%;">Tanzania  509  on 8/25/20</div>`)[0];
                popup_97322e2f4c404a7fa2c3f1bae9029469.setContent(html_d9246150295a4c879595210b3a791a00);
            

            circle_f7690d715c064e4d8cd2ff18dad5cbab.bindPopup(popup_97322e2f4c404a7fa2c3f1bae9029469)
            ;

            
        
    

            var circle_d2c7aac471d14899867c5c5881d705d0 = L.circle(
                [15.870032, 100.992541],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1701.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4ada45a2f1374d85aa129da910ea45bc = L.popup({maxWidth: '100%'
            
            });

            
                var html_c54571b900b64d8aacb21f0a51827945 = $(`<div id="html_c54571b900b64d8aacb21f0a51827945" style="width: 100.0%; height: 100.0%;">Thailand  3402  on 8/25/20</div>`)[0];
                popup_4ada45a2f1374d85aa129da910ea45bc.setContent(html_c54571b900b64d8aacb21f0a51827945);
            

            circle_d2c7aac471d14899867c5c5881d705d0.bindPopup(popup_4ada45a2f1374d85aa129da910ea45bc)
            ;

            
        
    

            var circle_6755a4a16388494ab21c31d6817804e1 = L.circle(
                [-8.874217, 125.727539],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 13.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_dd3681f469c34523b83fdd09fa5a4ac0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_ec65c36363334d819cc0eb98d5bc7c5b = $(`<div id="html_ec65c36363334d819cc0eb98d5bc7c5b" style="width: 100.0%; height: 100.0%;">Timor-Leste  26  on 8/25/20</div>`)[0];
                popup_dd3681f469c34523b83fdd09fa5a4ac0.setContent(html_ec65c36363334d819cc0eb98d5bc7c5b);
            

            circle_6755a4a16388494ab21c31d6817804e1.bindPopup(popup_dd3681f469c34523b83fdd09fa5a4ac0)
            ;

            
        
    

            var circle_4409c9dac4c547f7b6a44c6d251db37d = L.circle(
                [8.6195, 0.8248],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 654.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_cb218bf4e9b54aa3ab8cf23853dffa00 = L.popup({maxWidth: '100%'
            
            });

            
                var html_bef669b3ee81456591223dcf5ede004b = $(`<div id="html_bef669b3ee81456591223dcf5ede004b" style="width: 100.0%; height: 100.0%;">Togo  1309  on 8/25/20</div>`)[0];
                popup_cb218bf4e9b54aa3ab8cf23853dffa00.setContent(html_bef669b3ee81456591223dcf5ede004b);
            

            circle_4409c9dac4c547f7b6a44c6d251db37d.bindPopup(popup_cb218bf4e9b54aa3ab8cf23853dffa00)
            ;

            
        
    

            var circle_052e302df7aa45808cda6fe0d7805ba5 = L.circle(
                [10.6918, -61.2225],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 626.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_f304e587f9c04220a24a69a4858e0414 = L.popup({maxWidth: '100%'
            
            });

            
                var html_85c75623a00b4a7c8f2df699f183822a = $(`<div id="html_85c75623a00b4a7c8f2df699f183822a" style="width: 100.0%; height: 100.0%;">Trinidad and Tobago  1252  on 8/25/20</div>`)[0];
                popup_f304e587f9c04220a24a69a4858e0414.setContent(html_85c75623a00b4a7c8f2df699f183822a);
            

            circle_052e302df7aa45808cda6fe0d7805ba5.bindPopup(popup_f304e587f9c04220a24a69a4858e0414)
            ;

            
        
    

            var circle_211d263d3947470c8538c7ab88a9da0a = L.circle(
                [33.886917, 9.537499],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1534.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_4c0734cfb09a47ceb21294e398a0429b = L.popup({maxWidth: '100%'
            
            });

            
                var html_807d357b3f994b36b138725a3d35cca7 = $(`<div id="html_807d357b3f994b36b138725a3d35cca7" style="width: 100.0%; height: 100.0%;">Tunisia  3069  on 8/25/20</div>`)[0];
                popup_4c0734cfb09a47ceb21294e398a0429b.setContent(html_807d357b3f994b36b138725a3d35cca7);
            

            circle_211d263d3947470c8538c7ab88a9da0a.bindPopup(popup_4c0734cfb09a47ceb21294e398a0429b)
            ;

            
        
    

            var circle_4592403807dd4e76997f5280770b4fa4 = L.circle(
                [38.9637, 35.2433],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 130597.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_33ee4c8904e54e1d9e8fb4037cfb055f = L.popup({maxWidth: '100%'
            
            });

            
                var html_222b384f8710424ead4f5fc9ea608d80 = $(`<div id="html_222b384f8710424ead4f5fc9ea608d80" style="width: 100.0%; height: 100.0%;">Turkey  261194  on 8/25/20</div>`)[0];
                popup_33ee4c8904e54e1d9e8fb4037cfb055f.setContent(html_222b384f8710424ead4f5fc9ea608d80);
            

            circle_4592403807dd4e76997f5280770b4fa4.bindPopup(popup_33ee4c8904e54e1d9e8fb4037cfb055f)
            ;

            
        
    

            var circle_20a2247d91194e2f94157dd568cf03f7 = L.circle(
                [40.0, -100.0],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 2888855.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9c33f231399043e3b58909fba8fb8162 = L.popup({maxWidth: '100%'
            
            });

            
                var html_29f5ad28ab8d40e5be9ba307a1dcdbce = $(`<div id="html_29f5ad28ab8d40e5be9ba307a1dcdbce" style="width: 100.0%; height: 100.0%;">US  5777710  on 8/25/20</div>`)[0];
                popup_9c33f231399043e3b58909fba8fb8162.setContent(html_29f5ad28ab8d40e5be9ba307a1dcdbce);
            

            circle_20a2247d91194e2f94157dd568cf03f7.bindPopup(popup_9c33f231399043e3b58909fba8fb8162)
            ;

            
        
    

            var circle_03b4d701011f4db8a52296180c2d37d0 = L.circle(
                [1.373333, 32.290275],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 1213.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_c7f30f06da1345b0969ac2423f102f5d = L.popup({maxWidth: '100%'
            
            });

            
                var html_04030c3e1604459e91920970b42bcb75 = $(`<div id="html_04030c3e1604459e91920970b42bcb75" style="width: 100.0%; height: 100.0%;">Uganda  2426  on 8/25/20</div>`)[0];
                popup_c7f30f06da1345b0969ac2423f102f5d.setContent(html_04030c3e1604459e91920970b42bcb75);
            

            circle_03b4d701011f4db8a52296180c2d37d0.bindPopup(popup_c7f30f06da1345b0969ac2423f102f5d)
            ;

            
        
    

            var circle_59cfbc98d1a74701a655f3bede69f185 = L.circle(
                [48.3794, 31.1656],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 55474.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_05cdf36dba8c400bb21b1ac65ddd0aae = L.popup({maxWidth: '100%'
            
            });

            
                var html_e8c1d1cbd2ad436db283637e7ccdf62e = $(`<div id="html_e8c1d1cbd2ad436db283637e7ccdf62e" style="width: 100.0%; height: 100.0%;">Ukraine  110949  on 8/25/20</div>`)[0];
                popup_05cdf36dba8c400bb21b1ac65ddd0aae.setContent(html_e8c1d1cbd2ad436db283637e7ccdf62e);
            

            circle_59cfbc98d1a74701a655f3bede69f185.bindPopup(popup_05cdf36dba8c400bb21b1ac65ddd0aae)
            ;

            
        
    

            var circle_5f130a0437f04f11b9cca8912a0e35b3 = L.circle(
                [23.424076, 53.847818],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 33810.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_9d285e3974434d0c81a0d685dd71e0d2 = L.popup({maxWidth: '100%'
            
            });

            
                var html_c67dd2368773440894c9eb338e204ecf = $(`<div id="html_c67dd2368773440894c9eb338e204ecf" style="width: 100.0%; height: 100.0%;">United Arab Emirates  67621  on 8/25/20</div>`)[0];
                popup_9d285e3974434d0c81a0d685dd71e0d2.setContent(html_c67dd2368773440894c9eb338e204ecf);
            

            circle_5f130a0437f04f11b9cca8912a0e35b3.bindPopup(popup_9d285e3974434d0c81a0d685dd71e0d2)
            ;

            
        
    

            var circle_746ced6ad6044b1491dfc43d2d148bf1 = L.circle(
                [270.02989800000006, -482.92466599999995],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 164910.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_48364f674e4049f3bbfee3a79c2bfe8a = L.popup({maxWidth: '100%'
            
            });

            
                var html_0ba966d1235842468ff56ce09f524bb3 = $(`<div id="html_0ba966d1235842468ff56ce09f524bb3" style="width: 100.0%; height: 100.0%;">United Kingdom  329821  on 8/25/20</div>`)[0];
                popup_48364f674e4049f3bbfee3a79c2bfe8a.setContent(html_0ba966d1235842468ff56ce09f524bb3);
            

            circle_746ced6ad6044b1491dfc43d2d148bf1.bindPopup(popup_48364f674e4049f3bbfee3a79c2bfe8a)
            ;

            
        
    

            var circle_5547907ae4d74d7e95e0638dbe4ae534 = L.circle(
                [-32.5228, -55.7658],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 768.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_c71b9a0b61704e889b237c919b3fd3f4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_039ab653d7fe41058007df86997893d4 = $(`<div id="html_039ab653d7fe41058007df86997893d4" style="width: 100.0%; height: 100.0%;">Uruguay  1536  on 8/25/20</div>`)[0];
                popup_c71b9a0b61704e889b237c919b3fd3f4.setContent(html_039ab653d7fe41058007df86997893d4);
            

            circle_5547907ae4d74d7e95e0638dbe4ae534.bindPopup(popup_c71b9a0b61704e889b237c919b3fd3f4)
            ;

            
        
    

            var circle_78ad834b730e47a387375a23c241433c = L.circle(
                [41.377491, 64.585262],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 19820.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_a77e8bfe501a42578d98ac8d27a5fb33 = L.popup({maxWidth: '100%'
            
            });

            
                var html_99751ea78b4b4a82b70fcd6aa61d61f7 = $(`<div id="html_99751ea78b4b4a82b70fcd6aa61d61f7" style="width: 100.0%; height: 100.0%;">Uzbekistan  39641  on 8/25/20</div>`)[0];
                popup_a77e8bfe501a42578d98ac8d27a5fb33.setContent(html_99751ea78b4b4a82b70fcd6aa61d61f7);
            

            circle_78ad834b730e47a387375a23c241433c.bindPopup(popup_a77e8bfe501a42578d98ac8d27a5fb33)
            ;

            
        
    

            var circle_7b96c135f9d843cbbae13b9d3b6281db = L.circle(
                [6.4238, -66.5897],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 20579.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_76ae455755704160941ce83b86e7df5b = L.popup({maxWidth: '100%'
            
            });

            
                var html_3c808f53e35f4e21ae9c9bfd4fa684f1 = $(`<div id="html_3c808f53e35f4e21ae9c9bfd4fa684f1" style="width: 100.0%; height: 100.0%;">Venezuela  41158  on 8/25/20</div>`)[0];
                popup_76ae455755704160941ce83b86e7df5b.setContent(html_3c808f53e35f4e21ae9c9bfd4fa684f1);
            

            circle_7b96c135f9d843cbbae13b9d3b6281db.bindPopup(popup_76ae455755704160941ce83b86e7df5b)
            ;

            
        
    

            var circle_5f60ad0ea50348229896962d48853574 = L.circle(
                [14.058324, 108.277199],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 514.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_afb395b0316347db8eae9b5ef0b51fbf = L.popup({maxWidth: '100%'
            
            });

            
                var html_fc4b28af935f4ee7b8ed18a85fb8da6e = $(`<div id="html_fc4b28af935f4ee7b8ed18a85fb8da6e" style="width: 100.0%; height: 100.0%;">Vietnam  1029  on 8/25/20</div>`)[0];
                popup_afb395b0316347db8eae9b5ef0b51fbf.setContent(html_fc4b28af935f4ee7b8ed18a85fb8da6e);
            

            circle_5f60ad0ea50348229896962d48853574.bindPopup(popup_afb395b0316347db8eae9b5ef0b51fbf)
            ;

            
        
    

            var circle_2b7e600c443f48b9a24b12ca0109afcc = L.circle(
                [31.9522, 35.2332],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 9839.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_abd664ce40ce4187bb25b4087df407b4 = L.popup({maxWidth: '100%'
            
            });

            
                var html_472d61b0db874af5b4a40be11505d890 = $(`<div id="html_472d61b0db874af5b4a40be11505d890" style="width: 100.0%; height: 100.0%;">West Bank and Gaza  19678  on 8/25/20</div>`)[0];
                popup_abd664ce40ce4187bb25b4087df407b4.setContent(html_472d61b0db874af5b4a40be11505d890);
            

            circle_2b7e600c443f48b9a24b12ca0109afcc.bindPopup(popup_abd664ce40ce4187bb25b4087df407b4)
            ;

            
        
    

            var circle_7a70ed70f16c4f6cbd3961dc22dd11a3 = L.circle(
                [24.2155, -12.8858],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_8a2de7bd5dd140e29aa191989069ca07 = L.popup({maxWidth: '100%'
            
            });

            
                var html_f82ecfd6cf484c64bf19b616f5d8dfd6 = $(`<div id="html_f82ecfd6cf484c64bf19b616f5d8dfd6" style="width: 100.0%; height: 100.0%;">Western Sahara  10  on 8/25/20</div>`)[0];
                popup_8a2de7bd5dd140e29aa191989069ca07.setContent(html_f82ecfd6cf484c64bf19b616f5d8dfd6);
            

            circle_7a70ed70f16c4f6cbd3961dc22dd11a3.bindPopup(popup_8a2de7bd5dd140e29aa191989069ca07)
            ;

            
        
    

            var circle_27ee4e5f3bbe45328da9c64db7e4803e = L.circle(
                [15.552727, 48.516388],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 962.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_91436f3afb694381bc37e6033256a1b0 = L.popup({maxWidth: '100%'
            
            });

            
                var html_985f12129b894888af100d2cb7c1c3af = $(`<div id="html_985f12129b894888af100d2cb7c1c3af" style="width: 100.0%; height: 100.0%;">Yemen  1924  on 8/25/20</div>`)[0];
                popup_91436f3afb694381bc37e6033256a1b0.setContent(html_985f12129b894888af100d2cb7c1c3af);
            

            circle_27ee4e5f3bbe45328da9c64db7e4803e.bindPopup(popup_91436f3afb694381bc37e6033256a1b0)
            ;

            
        
    

            var circle_8587d19dbbe54dc8b3d3592e22c04095 = L.circle(
                [-13.133897, 27.849332],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 5642.5,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_feff9eba961544c9935e6664633ec5bd = L.popup({maxWidth: '100%'
            
            });

            
                var html_6ea7857a6bb84e9f8925da45ac0bdee8 = $(`<div id="html_6ea7857a6bb84e9f8925da45ac0bdee8" style="width: 100.0%; height: 100.0%;">Zambia  11285  on 8/25/20</div>`)[0];
                popup_feff9eba961544c9935e6664633ec5bd.setContent(html_6ea7857a6bb84e9f8925da45ac0bdee8);
            

            circle_8587d19dbbe54dc8b3d3592e22c04095.bindPopup(popup_feff9eba961544c9935e6664633ec5bd)
            ;

            
        
    

            var circle_e3035a5f1f5e419090b154a435d2b243 = L.circle(
                [-19.015438, 29.154857],
                {
  "bubblingMouseEvents": true,
  "color": "red",
  "dashArray": null,
  "dashOffset": null,
  "fill": true,
  "fillColor": "red",
  "fillOpacity": 0.2,
  "fillRule": "evenodd",
  "lineCap": "round",
  "lineJoin": "round",
  "opacity": 1.0,
  "radius": 3098.0,
  "stroke": true,
  "weight": 3
}
                )
                .addTo(map_750562447c2149d7a0fc2231ddd22c4c);
            
    
            var popup_5682cbd99b644e86807f9e38b8030333 = L.popup({maxWidth: '100%'
            
            });

            
                var html_237752d9728a409d8333bd1b18e3ce83 = $(`<div id="html_237752d9728a409d8333bd1b18e3ce83" style="width: 100.0%; height: 100.0%;">Zimbabwe  6196  on 8/25/20</div>`)[0];
                popup_5682cbd99b644e86807f9e38b8030333.setContent(html_237752d9728a409d8333bd1b18e3ce83);
            

            circle_e3035a5f1f5e419090b154a435d2b243.bindPopup(popup_5682cbd99b644e86807f9e38b8030333)
            ;

            
        
</script>
