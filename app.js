var endpoint = "https://asia-northeast1-gamecardsolver.cloudfunctions.net/gameCardSolver"

function start() {
    var target = $("#target").val();
    var c1 = $("#c1").val();
    var c2 = $("#c2").val();
    var c3 = $("#c3").val();
    var c4 = $("#c4").val();
    var c5 = $("#c5").val();

    $.post(endpoint, "Test", function(data) {
        console.log(data)
    })

}