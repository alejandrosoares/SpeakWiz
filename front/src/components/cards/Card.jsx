import React from 'react';
// eslint-disable-next-line import/no-named-default
import { default as CardBootstrap } from 'react-bootstrap/Card';

function Card({ title, numberQuestions, description }) {
  return (
    <CardBootstrap>
      <CardBootstrap.Body>
        <CardBootstrap.Title>{title}</CardBootstrap.Title>
        <CardBootstrap.Subtitle>{numberQuestions}</CardBootstrap.Subtitle>
        <CardBootstrap.Text className="text-muted">{description}</CardBootstrap.Text>
      </CardBootstrap.Body>
    </CardBootstrap>
  );
}

export default Card;
