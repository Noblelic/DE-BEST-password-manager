chrome.runtime.onMessage.addListener((message,sender,sendResponse) => {
    if (message.type === "SAVE_PASSWORD" )  {console.log("Background received password information.");
        fetch ('http://127.0.0.1:5000/save-password',{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
                      },
            body:JSON.stringify(message.data)
        })
        .then(response => response.json())
        .then(data => {console.log("Python server response:", data);
            })
        .catch(error => {
            console.error("Could not connect to Python:", error);
        
    });
}

});