(function ($, d3utils) {
    "use strict";

    var selector = "#github-activity-timeseries .graph";

    var jsonsrc = $(selector).attr('data-jsonsrc');
        $.getJSON(jsonsrc, function (jsondata) {
            for (var k in jsondata) {
                $(selector).append('<hr/><h5 class="tm40">Time series graph of <i>'+k+'</i> github activity in a day</h5>');
                d3utils.vertBarChart(selector, jsondata[k], {});
            }
        });

}) (jQuery, d3utils);
