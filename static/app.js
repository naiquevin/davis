(function (window, document, d3, _, undefined) {

    var Davis = {};

    Davis.github = {

        forks: function (selector, data) {
            var keys = _.keys(data);
            var values = _.values(data);
            
            var totalWidth = 720;
            var barHeight = 30;
            var chartOffset = 200;
            var chartWidth = totalWidth - chartOffset;

            var chart = d3.select(selector).append("svg")
                .attr("class", "chart")
                .attr("width", totalWidth)
                .attr("height", barHeight * values.length);

            var x = d3.scale.linear()
                .domain([0, 30])
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
                .text(function (d) {
                    return d === 30 ? '>30' : String(d);
                });

            chart.append("g")
                .selectAll("text")
                .data(keys)
                .enter().append("text")
                .attr("x", chartOffset - 5)
                .attr("y", textY)
                .attr("dy", ".35em")
                .attr("text-anchor", "end")
                .style("fill", "#333")
                .text(String);
        }
    };

    window.Davis = Davis;

}) (window, document, d3, _);


