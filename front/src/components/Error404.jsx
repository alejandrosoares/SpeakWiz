import React from 'react';
import { Link } from 'react-router-dom';

function Error404() {
  return (
    <div className="Error">
      <h2>Error 404 - Not Found</h2>
      <Link className="btn-back" to="/"> Go to Home</Link>
    </div>
  );
}

export default Error404;
