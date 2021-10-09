export function sendMessagePromise<M = any, R = any> (
  tabId: number,
  message: M
): Promise<R> {
  return new Promise<R>((resolve) =>
    chrome.tabs.sendMessage(tabId, message, resolve)
  )
}