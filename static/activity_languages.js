(function ($, d3utils) {
    "use strict";

    var selector = "#github-languages .graph";
    var jsonsrc = $(selector).attr('data-jsonsrc');

    $.getJSON(jsonsrc, function (data) {
        d3utils.barChart(selector, data, {
            totalWidth: 1000,
            keyLabel: function (k) {
                return data[k] < 30 ? k + ' (' + data[k] + ')' : k;
            }
        });
    });

}) (jQuery, d3utils);
