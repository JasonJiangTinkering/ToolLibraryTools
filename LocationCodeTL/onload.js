// A $( document ).ready() block.
$(document).ready(function () {
  $("#targetfind").click(function () {
    find_item();
  });
  $("#item_id").focus();
  $("#banner")
    .css({
      width: "200px",
      height: "70px",
    })
    .attr({
      src: "data:image/png;base64," + toollibrarylogo,
    });
});
