(function (window, document, d3, _, undefined) {

    var barChart = function (selector, data, options) {
        var _default = {
            totalWidth: 720,
            barHeight: 30,
            chartOffset: 200,
            valueLabel: String,
            keyLabel: String
        };
        options = _.extend(_default, options);

        var pairs = _.pairs(data).sort(function (a, b) {
            return b[1] - a[1];
        });

        var keys = _.map(pairs, function (x) { return x[0]; });
        var values = _.map(pairs, function (x) { return x[1]; });

        var totalWidth = options.totalWidth;
        var barHeight = options.barHeight;
        var chartOffset = options.chartOffset;
        var chartWidth = totalWidth - chartOffset;

        var chart = d3.select(selector).append("svg")
            .attr("class", "chart")
            .attr("width", totalWidth)
            .attr("height", barHeight * values.length);

        var domain = [0, _.max(values)];

        var x = d3.scale.linear()
            .domain(domain)
            .range([0, chartWidth]);

        chart.selectAll("rect")
            .data(values)
            .enter().append("rect")
            .attr("x", chartOffset)
            .attr("y", function (d, i) { return i * barHeight })
            .attr("width", x)
            .attr("height", barHeight);

        chart.append("line")
            .attr("x1", chartOffset)
            .attr("y1", 0)
            .attr("x2", chartOffset)
            .attr("y2", barHeight * values.length)
            .style("stroke", "#ccc")
            .style("stroke-width", "1px");

        var textY = function (d, i) {
            return i * barHeight + barHeight / 2;
        };

        // text for no. of commits
        chart.selectAll("text")
            .data(values)
            .enter().append("text")
            .attr("x", function (d) { return x(d) + chartOffset; })
            .attr("y", textY)
            .attr("dx", -5)
            .attr("dy", ".35em")
            .attr("text-anchor", "end")
            .text(options.valueLabel);

        chart.append("g")
            .selectAll("text")
            .data(keys)
            .enter().append("text")
            .attr("x", chartOffset - 5)
            .attr("y", textY)
            .attr("dy", ".35em")
            .attr("text-anchor", "end")
            .style("fill", "#333")
            .text(options.keyLabel);
    };

    var Davis = {};

    Davis.github = {
        forks: function (selector, data) {
            return barChart(selector, data, {
                valueLabel: function (d) {
                    return d === 30 ? '>30' : String(d);
                }
            });
        },
        languages: function (selector, data) {
            return barChart(selector, data, {
                totalWidth: 1000,
                keyLabel: function (k) {
                    return data[k] < 30 ? k + ' (' + data[k] + ')' : k;
                }
            });
        }
    };

    window.Davis = Davis;

}) (window, document, d3, _);
