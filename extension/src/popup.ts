document.addEventListener("DOMContentLoaded", function () {
  console.log("idk")
    const button = document.getElementById("requestLinkButton")!;
    button.addEventListener("click", async () => {
        console.log("erwfwefsf")
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(<number> tabs[0].id, {greeting: "hello"}, function(response) {
            console.log(response);
            // => backend
            });
        });
    });
});

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      console.log(sender.tab ?
                  "from a content script:" + sender.tab.url :
                  "from the extension");
      if (request.greeting === "hello")
        sendResponse({farewell: "goodbye"});
    }
  );