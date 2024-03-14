import React from 'react';
import '../../assets/css/Footer.css';
import { Row, Col } from 'react-bootstrap';

function Footer() {
  return (
    <footer className="Footer">
      <Row>
        <Col xs={12}>
          <span className="text-muted">SpeakWiz &copy; 2024.</span>
        </Col>
      </Row>
    </footer>
  );
}

export default Footer;
