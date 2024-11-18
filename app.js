document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('message-input');
    const usernameInput = document.getElementById('username-input');
    const messagesDiv = document.getElementById('messages');

    // Function to add a message to the chat window
    function addMessage(message, username) {
        const messageElement = document.createElement('div');
        messageElement.textContent = `${username}: ${message}`; // Include username
        messagesDiv.appendChild(messageElement);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    // Detect when the user presses "Enter" and send the message
    messageInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && messageInput.value.trim() !== '') {
            const message = messageInput.value;
            const username = usernameInput.value || 'Anonymous'; // Default to 'Anonymous' if no username
            addMessage(message, username); // Include username in the message
            messageInput.value = '';
        }
    });
});

