// popup.js
console.log("Hello, World!");

function find_item() {
  var item = $("#item_id").val();
  if (item == "" || item == undefined || item == null) {
    return;
  }
  console.log(item);
  
  chrome.tabs.create({ url: item });

    // chrome.tabs.create({ url: "https://www.google.com/search?q=" + item });
}
