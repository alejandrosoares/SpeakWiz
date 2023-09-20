import React from 'react';
import '../../assets/css/topic/Topic.css';
import { Row, Col } from 'react-bootstrap';

function SectionTitle({ title }) {
  return (
    <Row>
      <Col>
        <h1>{title}</h1>
      </Col>
    </Row>
  );
}

export default SectionTitle;
