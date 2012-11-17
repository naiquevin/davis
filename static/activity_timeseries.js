(function ($, d3utils) {
    "use strict";

    var selector = "#github-activity-timeseries .graph";

    var jsonsrc = $(selector).attr('data-jsonsrc');
        $.getJSON(jsonsrc, function (jsondata) {
            d3utils.vertBarChart(selector, jsondata, {});
        });

}) (jQuery, d3utils);
