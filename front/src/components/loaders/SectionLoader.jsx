import React from 'react';
import Loader from './Loader';

function SectionLoader({ color }) {
  return (
    <Loader type="Section" withText color={color} />
  );
}

export default SectionLoader;
