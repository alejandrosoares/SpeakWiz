import React from 'react';
import Loader from './Loader';

function BtnLoader({ color }) {
  return (
    <Loader type="Btn" withText={false} color={color} />
  );
}

export default BtnLoader;
