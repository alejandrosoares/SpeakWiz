import React from 'react';
import '../../assets/css/modals/BaseModal.css';
import { Modal } from 'react-bootstrap';

function BaseModal({
  children, title, subtitle, handleClose, show,
}) {
  return (
    <Modal show={show} onHide={handleClose} className="BaseModal">
      <Modal.Header closeButton>
        <Modal.Title>
          <p className="BaseModal-Title">{title}</p>
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {subtitle && <p className="BaseModal-Subtitle">{subtitle}</p>}
        {children}
      </Modal.Body>
    </Modal>
  );
}

export default BaseModal;
