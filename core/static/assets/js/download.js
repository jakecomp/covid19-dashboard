



function tableToCSV(){

    var data = [];

    var cases_table = document.getElementById("cases_table");
    var quote = '"';
    var rows = cases_table.getElementsByTagName('tr');
    for (var i=0; i<rows.length; i++){
        var cols = rows[i].querySelectorAll('td,th');

        var csvrow = [];
        for (var j=0; j<cols.length; j++){
            csvrow.push(quote.concat(cols[j].innerHTML).toString(), quote);
        }

        data.push(csvrow.join(','));
    }

    data = data.join('\n');

    // Download the prepared csv data
    downloadCSVFile(data);
}

function downloadCSVFile(data){

    CSVFile = new Blob([data], { type: "text/csv" });

    var temp = document.createElement('a');
    temp.download = "data.csv";
    var url = window.URL.createObjectURL(CSVFile);
    temp.href = url;

    temp.style.display = "none";
    document.body.appendChild(temp);
    temp.click()
    document.body.removeChild(temp);
}