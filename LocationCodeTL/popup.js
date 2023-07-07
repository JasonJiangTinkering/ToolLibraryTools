// popup.js
console.log("Hello, World!");

function find_item() {
  var item = $("#item_id").val();
  if (item == "" || item == undefined || item == null) {
    return;
  }
  console.log(item);
  $.ajax({
    url:
      "https://universityheights.myturn.com/library/inventory/browse?q=" + item,
    dataType: "html",
    success: function (response) {
      url = $(response).find("a:contains('Edit')")[0].href;
      url_parts = url.slice(19).split("/");
      url_parts.splice(0, 1);
      url_ending = "";
      url_parts.forEach(function (part) {
        url_ending += "/" + part;
      });
      chrome.tabs.create({
        url: "https://universityheights.myturn.com" + url_ending,
      });
    },
  });
}
