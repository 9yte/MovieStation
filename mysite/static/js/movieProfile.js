$(document).ready(function() {
    var tableRow = $('.awards .table-header');
    while(tableRow.next().length !== 0){
        tableRow = tableRow.next();
        var x = $(tableRow.find('div'));
        if(x.text().trim() == 'Won')
            x.css({'color':'green', 'font-weight':'bolder'});
        else
            x.css({'color':'red', 'font-weight':'bolder'})
    }
});

function submitPost(){
    $.modal.close();
}
