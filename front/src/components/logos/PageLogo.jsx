import React from 'react';
import '../../assets/css/logos/PageLogo.css';
import LogoImage from '../../assets/images/logo.png';

function PageLogo() {
  return (
    <div className="PageLogo">
      <img src={LogoImage} className="PageLogo-Image" alt="Logo" />
    </div>
  );
}

export default PageLogo;
