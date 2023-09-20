import React from 'react';
import '../../assets/css/Tag.css';
import { Badge } from 'react-bootstrap';

function PremiumTag() {
  return (
    <Badge
      bg="success"
      className="Premium Tag"
    >
      <i className="bi bi-star-fill" />
      Premium
    </Badge>
  );
}

export default PremiumTag;
