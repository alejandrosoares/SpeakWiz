import React, { useContext } from 'react';
import '../../assets/css/header/Header.css';
import '../../assets/css/header/UserSession.css';
import { Row, Col } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import AnonymousUser from './AnonymousUser';
import LoggedUser from './LoggedUser';
import PageLogo from '../logos/PageLogo';

function Header() {
  const authContext = useContext(AuthContext);

  return (
    <header className="Header">
      <Row>
        <Col xs={6} lg={2}>
          <Link to="/">
            <PageLogo />
          </Link>
        </Col>
        <Col lg={7} className="d-none d-lg-block" />
        <Col xs={6} lg={2} className="UserSession">
          { authContext.user ? <LoggedUser /> : <AnonymousUser /> }
        </Col>
      </Row>
    </header>
  );
}

export default Header;
