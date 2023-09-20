import React, { useContext } from 'react';
import LogIn from '../users/LogIn';
import { LoginModalContext } from '../../context/LoginModalContext';
import BaseModal from './BaseModal';

function LoginModal() {
  const loginModalContext = useContext(LoginModalContext);
  const handleClose = () => loginModalContext.setShow(false);
  const title = 'Oops! This is a premium resource.';
  const subtitle = "Log in to access to a premium card. If you don't have an account yet, create one, it's free.";

  return (
    <BaseModal
      title={title}
      subtitle={subtitle}
      handleClose={handleClose}
      show={loginModalContext.show}
    >
      <LogIn />
    </BaseModal>
  );
}

export default LoginModal;
