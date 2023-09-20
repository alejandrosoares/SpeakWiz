import React from 'react';
import '../../assets/css/logos/PageLogo.css';
import FlashLogoImage from '../../assets/images/flashCard.png';

function PageLogo() {
  return (
    <div className="PageLogo">
      <img src={FlashLogoImage} className="PageLogo-Image" alt="Logo" />
      <span className="PageLogo-Title text-dark">FlashCard</span>
    </div>
  );
}

export default PageLogo;
