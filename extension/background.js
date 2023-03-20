function getInfo() {
    /**
     * @brief will provide a prompt to ChatGPT API to provide information on the currently selected text
     */

}

chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
        "id": "contextMenu",
        "title": "Get More Information",
        "contexts": ["selection"]
    })
    chrome.contextMenus.onClicked.addListener(getInfo)
})

