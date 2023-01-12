const chatLog = document.querySelector("#chat-log")
const roomName = JSON.parse(document.getElementById('room-name').textContent);

if (!chatLog.hasChildNodes()){
    const emptyText = document.createElement("h3")
    emptyText.id = "emptyText"
    emptyText.innerText = "No Messages, Say Hello!"
    emptyText.className = "emptyText"
    chatLog.appendChild(emptyText)
}

const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

// Called when a message is received from the server.
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const messageElement = document.createElement('div')
    messageElement.innerText = data.message
    messageElement.className = 'message'
    chatLog.appendChild(messageElement)

    if(document.querySelector("#emptyText")){
        document.querySelector("#emptyText").remove()
    }
};

// Called when the connection is closed.
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    // Send the msg object as a JSON-formatted string.
    chatSocket.send(JSON.stringify({
        'message': message,
        'username' : "{{request.user.username}}"}
    ));

    // Blank the text input element, ready to receive the next line of text from the user.
    messageInputDom.value = '';
};