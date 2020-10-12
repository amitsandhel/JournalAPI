//https://jsfiddle.net/MNSwiftOne/7aqj42d5

$(document).ready(function(){
    console.log("hello"); 
    $(function() {
         var $table = $('#myTable');
        /*$('#myTable').bootstrapTable({
        })*/
        $('#myTable').bootstrapTable('destroy').bootstrapTable({
        });



        $('#export').click(function() {
         $table.tableExport({
           type: 'csv',
           escape: false,
           exportDataType: 'all',
           refreshOptions: {
             exportDataType: 'all'
           }
         });
       });



    });

});