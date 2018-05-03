


 function insertable(data, tag) {
 	var newDiv = document.createElement("div");
 	var wrapperDiv = document.getElementById("table-wrapper")
 		wrapperDiv.insertAdjacentElement('afterbegin', newDiv)
 		newDiv.setAttribute('id', tag)
 		newDiv.innerHTML
 		drawTable(tableToArray(data), tag)
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
			if (j == 1){
			t.push(parseInt(cells[j].textContent));
			}else{
 			t.push(cells[j].textContent);
 			}
 		}
 		result.push(t);
 	}
 	return result;
 }

  function drawTable(tableData, tag) {
 	x = Array.from(tableData);
 	y = new String(arguments[1])
 		console.log(tableData);
 	console.log(typeof tableData);
 	var data = new google.visualization.DataTable();
 	data.addColumn('string', 'Name');
 	data.addColumn('number', 'Count');
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

function load_tables() {
	var art = document.querySelectorAll('table')
	insertable(art.item(0), "test");
	}


google.charts.setOnLoadCallback(load_tables);