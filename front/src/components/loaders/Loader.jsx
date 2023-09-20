import React from 'react';
import '../../assets/css/loaders/Loader.css';

function Loader({ type = 'Section', color, withText = false }) {
  const style = {
    border: `5px dotted ${color}`,
  };
  return (
    <div className={`Loader Loader_${type}`}>
      <div className="Loader-Icon" style={{ ...style }} />
      {withText && <p>Loading...</p>}
    </div>
  );
}

export default Loader;
