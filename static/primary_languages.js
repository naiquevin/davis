(function ($, d3) {
    "use strict";

    var selector = "#github-languages .graph",
    jsonsrc = $(selector).attr('data-jsonsrc');

    var colors = GithubColors;

    d3.json(jsonsrc, function (jsondata) {
        var width = 400,
        height = 400,
        outerRadius = Math.min(width, height) / 2,
        innerRadius = outerRadius * .6,
        data = d3.values(jsondata),
        keys = d3.keys(jsondata).map(function (x) { 
            return x === 'null' ? 'Other' : x;
        }),
        donut = d3.layout.pie(),
        arc = d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius);
        
        var vis = d3.select(selector)
            .append("svg")
            .data([data])
            .attr("width", width)
            .attr("height", height);

        var arcs = vis.selectAll("g.arc")
            .data(donut)
            .enter().append("g")
            .attr("class", "arc")
            .attr("transform", "translate(" + outerRadius + "," + outerRadius + ")");

        arcs.append("path")
            .attr("fill", function(d, i) { return colors[keys[i]]; })
            .attr("d", arc);

        arcs.append("text")
            .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
            .attr("dy", ".35em")
            .attr("text-anchor", "middle")
            .attr("display", function(d) { return d.value > .15 ? null : "none"; })
            .text(function(d, i) { return keys[i] + ' ('+ d.value + ')'; });
    });

}) (jQuery, d3);
