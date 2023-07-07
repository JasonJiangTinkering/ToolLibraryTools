// background_script.js
// Listen for messages from the content script
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.message === "Hello, World!") {
    // Log the message from the content script in the background console
    console.log(message.message);
  }
});
