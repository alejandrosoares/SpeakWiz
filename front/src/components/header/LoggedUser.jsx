import React, { useState, useContext } from 'react';
import '../../assets/css/header/LoggedUser.css';
import { Row, Col } from 'react-bootstrap';
import UserMenu from './UserMenu';
import { AuthContext } from '../../context/AuthContext';

function LoggedUser() {
  const authContext = useContext(AuthContext);
  const [showMenu, setShowMenu] = useState(false);

  return (
    <Row>
      <Col>
        <Row className="justify-content-center align-items-center">
          <Col xs={4} className="LoggedUser" onClick={() => setShowMenu(!showMenu)}>
            <span>{authContext.user?.initialName}</span>
            {showMenu && <UserMenu />}
          </Col>
        </Row>
      </Col>
    </Row>
  );
}

export default LoggedUser;
