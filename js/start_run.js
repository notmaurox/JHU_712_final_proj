function submitRun( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var user_email = $('#user_email').serialize();
    var sequence_name = $('#sequence_name').serialize();
    var sequence_dna = $('#sequence_dna').serialize();
    console.log("here");
    console.log(user_email);
    $.ajax({
        url: './start_run.cgi',
        dataType: 'json',
        type: "post",
        data: JSON.stringify(
            {'param':
                {
                    "user_email": user_email,
                    "seq_name": sequence_name,
                    "seq": sequence_dna
                }
            }
        ),
        success: function(data, textStatus, jqXHR) {
            $('#in_progress').show();
            $('#status_button').hide();
            populateInProgress(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to process sequence! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function checkStatus( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var job_id = window.job_id
    console.log(job_id)

    $.ajax({
        url: './check_run_status.cgi',
        dataType: 'json',
        data: "job_id="+job_id,
        success: function(data, textStatus, jqXHR) {
            console.log(data)
            $('#in_progress').show();
            processResults(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to process sequence! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function populateInProgress( data ) {
    $('#job_id').text( data.job_id );
    $("#status_button").hide();
    window.job_id = data.job_id;
    var timeleft = 10;
    var downloadTimer = setInterval(function(){
        if(timeleft <= 0){
            clearInterval(downloadTimer);
            document.getElementById("countdown").innerHTML = "Finished";
            $("#status_button").show();

        } else {
            document.getElementById("countdown").innerHTML = timeleft + " seconds remaining";
            $("#status_button").hide();
        }
        timeleft -= 1;
    }, 1500);
}

// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processResults( data ) {
    // set the span that lists the match count
    $('#vadr_status').text( data.vadr_status );
    if (!data.vadr_status.includes("JOB NOT FINISHED")) {
        $("#status_button").hide();
        $("#job_finished").show();
    }

    $('#seq_length').text( data.seq_length );
    $('#model_used').text( data.model_used );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // // iterate over each match and add a row to the result table for each
    $.each( data.sequence_features, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
    
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#results_table');
        
        // add the type column
        $('<td/>', { "text" : item.type } ).appendTo('#' + this_row_id);
        
        // add the name column
        $('<td/>', { "text" : item.name } ).appendTo('#' + this_row_id);

        // add the start column
        $('<td/>', { "text" : item.start } ).appendTo('#' + this_row_id);

        // add the end column
        $('<td/>', { "text" : item.end } ).appendTo('#' + this_row_id);
        
        // add the coords column
        $('<td/>', { "text" : item.seq_coords } ).appendTo('#' + this_row_id);

        // add the coords column
        $('<td/>', { "text" : item.alerts } ).appendTo('#' + this_row_id);
    });
    
    // // now show the result section that was previously hidden
    $('#results').show();
}

function validateForm() {
    var email = document.getElementById("user_email").value;
    if (email == "") {
      alert("email must be filled out");
      return false;
    }
    var sequence_name = document.getElementById("sequence_name").value;
    if (sequence_name == "") {
      alert("sequence name must be filled out");
      return false;
    }
    var sequence_dna = document.getElementById("sequence_dna").value;
    if (sequence_dna == "") {
      alert("sequence dna must be filled out");
      return false;
    }
    return true;
  }

// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        if (validateForm()) {
            submitRun();
            $("#status_button").hide();
        }
        return false;  // prevents 'normal' form submission
    });
    $('#status_button').click( function() {
        checkStatus();
        return false;  // prevents 'normal' form submission
    });
});


