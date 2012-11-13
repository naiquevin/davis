(function (d3, d3utils, undefined) {
    "use strict";

    d3utils.pieChart = function (selector, values, keys, options) {
        // this may or may not be used
        var color = d3.scale.category20();

        var _default = {
            pieWidth: 400,
            pieHeight: 400,
            colorFill: function (d, i) {
                return color(i);
            },
            textLabel: function (d, i) {
                return d.value;
            }
        };
        options = _.extend(_default, options || {});

        var width = options.pieWidth,
        height = options.pieHeight,
        outerRadius = Math.min(width, height) / 2,
        innerRadius = outerRadius * .6,
        donut = d3.layout.pie(),
        arc = d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius);
        
        var vis = d3.select(selector)
            .append("svg")
            .data([values])
            .attr("width", width)
            .attr("height", height);

        var arcs = vis.selectAll("g.arc")
            .data(donut)
            .enter().append("g")
            .attr("class", "arc")
            .attr("transform", "translate(" + outerRadius + "," + outerRadius + ")");

        arcs.append("path")
            .attr("fill", options.colorFill)
            .attr("d", arc);

        arcs.append("text")
            .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
            .attr("dy", ".35em")
            .attr("text-anchor", "middle")
            .attr("display", function(d) { return d.value > .15 ? null : "none"; })
            .text(options.textLabel);
    };

}) (d3, d3utils);
