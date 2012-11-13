(function ($, d3utils) {
    "use strict";

    var selector = "#github-activity-types .graph";
    var jsonsrc = $(selector).attr('data-jsonsrc');

    $.getJSON(jsonsrc, function (jsondata) {
        var keys = d3.keys(jsondata),
        values = d3.values(jsondata);
        d3utils.pieChart(selector, values, keys, {
            pieWidth: 450,
            pieHeight: 450
        });
    });

}) (jQuery, d3utils);
