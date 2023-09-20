import React from 'react';
import '../../assets/css/buttons/SoundBtn.css';

function SoundBtn({ text }) {
  const speech = new SpeechSynthesisUtterance();

  const onClick = () => {
    const voices = window.speechSynthesis.getVoices();
    const [firstVoice] = voices;
    speech.text = text;
    speech.voice = firstVoice;
    window.speechSynthesis.speak(speech);
  };

  function onKeyDown(e) {
    if (e.keyCode === 13) {
      onClick();
    }
  }

  return (
    <div className="SoundBtn" onClick={onClick} onKeyDown={onKeyDown} role="button" tabIndex={0}>
      <i className="bi bi-volume-up-fill" />
    </div>
  );
}

export default SoundBtn;
