console.log("hallo")

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        // getting meals - array
        // => array rüber an popup
        let meals: Array<object> = [{"testEssen": "pfund fritten"}]
        sendResponse(meals);
        
    });

  chrome.runtime.sendMessage({greeting: "hello"}, function(response) {
    console.log(response.farewell);
  });
  