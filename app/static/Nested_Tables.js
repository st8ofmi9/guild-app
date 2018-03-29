function load_nested() {

nu_array = []

var cor =  document.getElementsByClassName('google-visualization-table-td')
for (var i = 0; i < cor.length; i++)
    {
		if(i % 2 == 1)
		{
			cor[i].id = cor[i-1].innerHTML
			}
		else if( i == 0)
		{
			cor[i].id = cor[i+1].innerHTML
		}
	}

for (var array_count = 0; array_count < datarray.length; array_count++)
{
	tab_data = []
	var aray = datarray[array_count][2].split(",")
	for (i = 0; i < aray.length ; i+=3)
	{
		//console.log(aray.slice(i, i+3))
		tab_data.push(aray.slice(i, i+3))

	}
	nu_array.push(tab_data)
	try {
	//drawTable2(tab_data, datarray[array_count][0])
	}
	catch(err)
	{
	tab_data.length
	}


}



return nu_array;

}

function drawTable2(tdata, tag) {
 		//console.log(tableData);
 	//console.log(typeof tableData);
 	var data = new google.visualization.DataTable();
 	data.addColumn('string', 'Name');
 	data.addColumn('string', 'Joined');
 	data.addColumn('string', 'Days');
 	console.log(x);
 	//console.log(y);
 	data.addRows(tdata);
 	var table = new google.visualization.Table(document.getElementById(String(tag)));

 	table.draw(data, {
 		showRowNumber: false,
 		width: '100%',
 		height: '100%',
 		title: 'This Is A Title'
 	});
 }

//google.charts.setOnLoadCallback(load_nested);




