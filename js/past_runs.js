function getPastRuns() {
    var user_email = document.getElementById("past_user_email").value;
    $.ajax({
        url: './get_past_runs.cgi',
        dataType: 'json',
        data: "user_email="+user_email,
        success: function(data, textStatus, jqXHR) {
            console.log(data)
            populatePastRuns(data)
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to process sequence! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function populatePastRuns(data) {

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // // iterate over each match and add a row to the result table for each
    $.each( data.past_jobs, function(i, item) {
        var this_row_id = 'past_runs_row_' + next_row_num++;
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#past_runs_table_body');
        $('<td/>', { "text" : item.id } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.seq_name } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.sequence_length } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.vadr_status } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.sequence } ).appendTo('#' + this_row_id);
    });
    
    // // now show the result section that was previously hidden
    $('#past_runs_body').show();
}

// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#past_run_submit').click( function() {
        getPastRuns();
        return false;  // prevents 'normal' form submission
    });
});