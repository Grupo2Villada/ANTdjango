$(document).ready(function(){
    $("#form").submit(function(){
        var success = "<div class='alert alert-success bg-success ' role='alert'>Grade uploaded succesfully</div>";
        $("body").append(success);
        console.log("ast");
    });
});
$("#mySelect").attr("selectedIndex", -1);
