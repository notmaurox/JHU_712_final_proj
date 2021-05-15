function setupTopNav() {
    document.getElementById('new_run').addEventListener(
    'click', function() {
            $('#past_run_div').hide();
            $('#new_run_div').show();
    }, false
    );
    document.getElementById('past_run').addEventListener(
    'click', function() {
            $('#new_run_div').hide();
            $('#past_run_div').show();
    }, false
    );
}