import React from 'react';
import { Row, Col } from 'react-bootstrap';
import WelcomeImage from '../assets/images/teaching.jpeg';
import WelcomeImageMedium from '../assets/images/teaching-md.jpeg';
import WelcomeImageSmall from '../assets/images/teaching-sm.jpeg';
import '../assets/css/Welcome.css';

function Welcome() {
  return (
    <Row className="Welcome">
      <Col md={6} className="WelcomeTitle">
        <h1>Welcome to Speak Wiz</h1>
        <h2>Here you will find to endless of cards to practice</h2>
      </Col>
      <Col md={6}>
        <picture>
          <source media="(max-width: 576px)" srcSet={WelcomeImageSmall} />
          <source media="(min-width: 577px) and (max-width: 992px)" srcSet={WelcomeImageMedium} />
          <img src={WelcomeImage} alt="Image" className="Welcome-Image" />
        </picture>
      </Col>
    </Row>
  );
}

export default Welcome;
