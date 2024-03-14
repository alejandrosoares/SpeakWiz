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
        <Col xs={authContext.user ? 6 : 12} md={9} className="LogoContainer">
          <Link to="/">
            <PageLogo />
          </Link>
        </Col>
        <Col xs={authContext.user ? 6 : 12} md={3} className="UserSession">
          { authContext.user ? <LoggedUser /> : <AnonymousUser /> }
        </Col>
      </Row>
    </header>
  );
}

export default Header;
