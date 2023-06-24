console.log("starting scripts");

const samplesUrl = "http://127.0.0.1:5000/api/v1.0/druglist/substancecount";


d3.json(samplesUrl).then(function(data) {
    // console.log(data);

    let count = [];
    let names = [];

    for (i=0; i<data.length; i++) {
        count.push(data[i].count);
        if (data[i].substance_name) {
            let name = "";
            for (x=0; x<data[i].substance_name.length; x++) {
                name += data[i].substance_name[x] + " ";
            }
            names.push(name);
        } else {
            names.push("N/A");
        }
    }

    updatePlotly(count, names);

})

function updatePlotly(count, name) {

    // console.log(count);
    // console.log(name);
   
    let trace1 = {
        x: name,
        y: count,
        type: bar
    };

    dataTrace = [trace1];

    // set layout
    let layout = {
        autosize: true
    };

    // Create graph
    Plotly.newPlot("bar", dataTrace, layout);
}