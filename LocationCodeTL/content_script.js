// content_script.js
console.log("Hello, World!");

function find_item() {
  item_id = $("#item_id").val;
}

// Send a message to the background script
chrome.runtime.sendMessage({ message: "Hello, World!" });
