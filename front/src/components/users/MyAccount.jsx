import React, { useContext } from 'react';
import '../../assets/css/MyAccount.css';
import { Row, Col } from 'react-bootstrap';
import { AuthContext } from '../../context/AuthContext';
import SectionTitle from '../titles/SectionTitle';
import formatDate from '../../utils/dates';

function MyAccount() {
  const authContext = useContext(AuthContext);

  return (
    <Row className="MyAccount">
      <Col xs={12}>
        <SectionTitle title="My Account" />
      </Col>
      <Col xs={12}>
        <span>Name:</span>
        <span className="MyAccount-field-value">{authContext.user.name}</span>
      </Col>
      <Col xs={12}>
        <span>Email:</span>
        <span className="MyAccount-field-value">{authContext.user.email}</span>
      </Col>
      <Col xs={12}>
        <span>Joined:</span>
        <span className="MyAccount-field-value">{formatDate(authContext.user.joined)}</span>
      </Col>
    </Row>
  );
}

export default MyAccount;
