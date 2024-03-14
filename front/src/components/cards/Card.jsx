import React from 'react';
// eslint-disable-next-line import/no-named-default
import { default as CardBootstrap } from 'react-bootstrap/Card';

function Card({ title, description }) {
  return (
    <CardBootstrap>
      <CardBootstrap.Body>
        <CardBootstrap.Title>{title}</CardBootstrap.Title>
        <CardBootstrap.Text>{description}</CardBootstrap.Text>
      </CardBootstrap.Body>
    </CardBootstrap>
  );
}

export default Card;
