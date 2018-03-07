 function drawTable(tableData, tag) {
 	x = Array.from(tableData);
 	y = new String(arguments[1])
 		console.log(tableData);
 	console.log(typeof tableData);
 	var data = new google.visualization.DataTable();
 	data.addColumn('string', 'Name');
 	data.addColumn('string', 'Joined');
 	data.addColumn('string', 'Days');
 	console.log(x);
 	console.log(y);
 	data.addRows(x);
 	console.log(String(tag));
 	var table = new google.visualization.Table(document.getElementById(String(tag)));

 	table.draw(data, {
 		showRowNumber: false,
 		width: '100%',
 		height: '100%',
 		title: 'This Is A Title'
 	});
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

 function insertable(data, tag) {
 	var newDiv = document.createElement("div");
 	var wrapperDiv = document.getElementById("table-wrapper")
 		wrapperDiv.insertAdjacentElement('afterbegin', newDiv)
 		newDiv.setAttribute('id', tag)
 		newDiv.innerHTML
 		drawTable(tableToArray(data), tag)
 }

 function load_tables() {

 	var art = document.querySelectorAll('table')
 		var i = 0

 		for (var item of art) {
 			var curr_item = art.item(i)
 				insertable(curr_item, curr_item.id)
 				i++
 		}

 		var x = document.getElementById("table_div");
 	x.style.display = "none";

 }

 function chartdata() {
 	i = 0
 		datarray = []

 	function test(key) {
 		x = document.querySelectorAll(key);
 		xarray = tableToArray(x['1']);
 		return [key, xarray.length]
 	}

 	var art = document.querySelectorAll('table')

 		for (var item of art) {
 			if (art.item(i).id === "") {
 				i++
 			} else if (datarray.length <= 0) {
 				datarray.unshift(["Rank", "Number of Members"])
 			} else {
 				var curr_item = art.item(i);
 				datarray.push(test("#" + curr_item.id));
 				i++
 			}

 		}
 		return datarray
 }

 function pie_chart() {
 	var newDiv = document.createElement("div");
 	var wrapperDiv = document.getElementById("table-wrapper")
 		wrapperDiv.insertAdjacentElement('afterbegin', newDiv)
 		newDiv.setAttribute('id', 'piechart')
 		var chart = new google.visualization.PieChart(document.getElementById('piechart'))
 		data = google.visualization.arrayToDataTable(chartdata())
		var options = {title: 'Members'};
		options['chartArea'] = {width: 400, height: 300}

 		chart.draw(data,options)
 }

 google.charts.setOnLoadCallback(load_tables);
 google.charts.setOnLoadCallback(pie_chart);