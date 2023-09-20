import React from 'react';
import { Row, Col, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function AnonymousUser() {
  return (
    <Row>
      <Col>
        <Link to="/log-in" className="UserSession-Login">
          <Button variant="link">Log In</Button>
        </Link>
      </Col>
      <Col>
        <Link to="/sign-up" className="UserSession-SignUp">
          <Button variant="dark">Sign Up</Button>
        </Link>
      </Col>
    </Row>
  );
}

export default AnonymousUser;
