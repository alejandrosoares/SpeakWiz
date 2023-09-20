import React from 'react';
import WelcomeImage from '../assets/images/teaching.jpeg';
import WelcomeImageMedium from '../assets/images/teaching-md.jpeg';
import WelcomeImageSmall from '../assets/images/teaching-sm.jpeg';
import '../assets/css/Welcome.css';

function Welcome() {
  return (
    <div className="Welcome">
      <picture>
        <source media="(max-width: 576px)" srcSet={WelcomeImageSmall} />
        <source media="(min-width: 577px) and (max-width: 992px)" srcSet={WelcomeImageMedium} />
        <img src={WelcomeImage} alt="Image" className="Welcome-Image" />
      </picture>
      <h1>Welcome to FlashCard</h1>
      <h2>Here you can find to endless of flashcard to practice</h2>
    </div>
  );
}

export default Welcome;
