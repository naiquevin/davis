(function ($, d3) {
    "use strict";

    var selector = "#github-languages .graph",
    jsonsrc = $(selector).attr('data-jsonsrc');

    d3.json(jsonsrc, function (jsondata) {
        var colors = GithubColors,
        keys = d3.keys(jsondata).map(function (x) { 
            return x === 'null' ? 'Other' : x;
        }),
        values = d3.values(jsondata);        
        d3utils.pieChart(selector, values, keys, {
            colorFill: function(d, i) { return colors[keys[i]]; },
            textLabel: function(d, i) { return keys[i] + ' ('+ d.value + ')'; }
        });
    });

}) (jQuery, d3);
