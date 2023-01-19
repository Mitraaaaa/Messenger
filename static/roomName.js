const user_id = JSON.parse(document.getElementById('user_id').textContent);

document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value;
    var roomType = document.querySelector('#select1').value;

    if (roomType === "Private"){
        window.location.pathname = '/chat/' + user_id + "_" + roomName + '/';
    }
    else{
        window.location.pathname = '/chat/' + roomType + "_" + roomName + '/';
    }
};

document.querySelector('#account-info-button').onclick = function(e) {
        window.location.pathname = '/chat/account/' + user_id + '/';
  };