(function ($, d3utils) {
    "use strict";

    var selector = "#github-forks .graph";
    var jsonsrc = $(selector).attr('data-jsonsrc');

    $.getJSON(jsonsrc, function (data) {
        d3utils.barChart(selector, data, {
            valueLabel: function (d) {
                return d === 30 ? '>30' : String(d);
            }
        });
    });

}) (jQuery, d3utils);
