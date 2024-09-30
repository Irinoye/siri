// Check if the browser supports SpeechRecognition
window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!window.SpeechRecognition) {
    alert('Your browser does not support speech recognition. Please try with a supported browser.');
} else {
    const recognition = new window.SpeechRecognition();
    const startBtn = document.getElementById('start-btn');
    const resultPara = document.getElementById('result');

    recognition.interimResults = true;
    recognition.continuous = false;

    recognition.onresult = (event) => {
        const transcript = Array.from(event.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join('');

        resultPara.textContent = transcript;
        speak(transcript);  // Call the speak function when speech recognition captures text
    };

    startBtn.addEventListener('click', () => {
        recognition.start();
    });
}

// Function to use Web Speech API for speech synthesis
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}
