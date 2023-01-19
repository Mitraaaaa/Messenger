var messageBody = document.querySelector('#chat-log');
messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;

const chatLog = document.querySelector("#chat-log")
const roomName = JSON.parse(document.getElementById('room-name').textContent);

if (chatLog.childNodes.length <= 1){
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
    const loggedInUser = JSON.parse(document.getElementById("username").textContent)
    console.log(loggedInUser)
    console.log(data.username)
    messageElement.innerText = data.message

    if (data.username === loggedInUser){
        messageElement.classList.add("message", "sender")
    }else{
        messageElement.classList.add("message", "receiver")
    }

    chatLog.appendChild(messageElement)

    if(document.querySelector("#emptyText")){
        document.querySelector("#emptyText").remove()
    }

    var messageBody = document.querySelector('#chat-log');
    messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
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
    if (message.length != 0){
        // Send the msg object as a JSON-formatted string.
        chatSocket.send(JSON.stringify({
            'message': message,
            'username' : "{{request.user.username}}"
        }));

        // Blank the text input element, ready to receive the next line of text from the user.
        messageInputDom.value = '';
    }else {
        alert('Type Something pls :/')
    }
};