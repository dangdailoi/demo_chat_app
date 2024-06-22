document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    socket.on('receive_message', (data) => {
        const messageContainer = document.createElement('div');
        messageContainer.className = 'message';
        messageContainer.innerHTML = `<strong>${data.username}</strong>: ${data.message}`;
        document.getElementById('chat-messages').appendChild(messageContainer);
    });
});

function sendMessage() {
    const username = document.getElementById('username').value;
    const message = document.getElementById('message').value;

    if (username && message) {
        const socket = io();
        socket.emit('send_message', {
            username: username,
            message: message
        });

        document.getElementById('message').value = '';
    }
}