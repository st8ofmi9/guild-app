// Load the Visualization API and the controls package.
google.charts.load('current', {
    'packages': ['table', 'corechart', 'controls']
});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawDashboard);

// Callback that creates and populates a data table,
// instantiates a dashboard, a range slider and a pie chart,
// passes in the data and draws it.
function drawDashboard() {

    // Create our data table.
    data = google.visualization.arrayToDataTable(chartdata());
    //data = Array(chartdata());

        // Create a dashboard.
        var dashboard = new google.visualization.Dashboard(
            document.getElementById('dashboard_div'));

    // Create a range slider, passing some options
    var donutRangeSlider = new google.visualization.ControlWrapper({
            'controlType': 'CategoryFilter',
            'containerId': 'filter_div',
            'options': {
                'filterColumnLabel': 'Rank'
          }
        });

    // Create a pie chart, passing some options
    var pieChart = new google.visualization.ChartWrapper({
            'chartType': 'PieChart',
            'containerId': 'chart_div',
            'options': {
                'width': '100%',
                'height': '100%',
                'pieSliceText': 'value',
                'legend': 'right'
            },
            'view': {
                'columns': [0, 1]
            }
        });

    var table_1ists = new google.visualization.ChartWrapper({
            'chartType': 'Table',
            'containerId': 'table_div',
            'options': {
                'width': '100%',
                'height': '100%',
                'allowHtml': true,

            },
            'cssClassNames':{
            'tableCell': 'Nested-Div'
            },
            'view': {
                'columns': [2, 3, 4]
            }
        });

    // Establish dependencies, declaring that 'filter' drives 'pieChart',
    // so that the pie chart will only display entries that are let through
    // given the chosen slider range.
    dashboard.bind(donutRangeSlider, [pieChart, table_1ists]);

    // Draw the dashboard.
    dashboard.draw(data);
}

function chartdata() {

    datarray = [];

    function test(key) {

        x = document.querySelectorAll(key);
        xarray = tableToArray(x.item(0));
        xnames = [];
        for (step = 0; step < xarray.length; step++) {

            xnames.push("<td>"+xarray[step][0]+"</td>");

        }
        //return [key, xarray.length, "<table>"+xnames.toString().replace(/,/g,"")+"</table>"]//.replace(/,/g,)];
        return [key, xarray.length];
    }

    var art = document.querySelectorAll('table')
        for (i = 0; i <= art.length; i++) {
            try {
                console.log(art.item(i));
                if (art.item(i).attributes.class !== undefined || art.item(i).attributes.id === undefined) {}
                else if (datarray.length <= 0) {
                    datarray.unshift(["Rank", "Number of Members", "Members", "Date", "Tenure"])
                    i--;
                } else {
                    console.log(art.item(i).id);
                    var curr_item = "#" + art.item(i).id;
                    console.log("Current Item is:" + curr_item);
                    console.log(test(curr_item));
                    keyValues = test(curr_item)

                    for(var things of xarray)
                    {
                    datarray.push([keyValues[0], "", things[0], things[1], things[2]]);
                    }


                }
            } catch (TypeError) {}


        }

var ranks = ["#Rogue", "#Strange", "#Bomb", "#Bombling","#Fiery", "#Flash", "#Fizzling"]
for (var rank of ranks)
{
rankData = test(rank)
datarray.push([rankData[0],rankData[1], "", "", ""])
}

        return datarray;

}

function tableToArray(table) {
    var result = []
    var rows = table.rows;
    var cells,
    t;

    // Iterate over rows
    for (var i = 0, iLen = rows.length; i < iLen; i++) {
        cells = rows[i].cells;
        t = [];

        // Iterate over cells
        for (var j = 0, jLen = cells.length; j < jLen; j++) {
            t.push(cells[j].textContent);
        }
        result.push(t);
    }
    return result;
}
