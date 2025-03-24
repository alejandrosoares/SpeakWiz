import React from 'react';
import { useNavigate } from 'react-router-dom';

function FavoriteEmptyList() {
  const navigate = useNavigate();
  return (
    <>
      <p className="text-muted text-center">Your favorite list is empty.</p>
      <button
        type="button"
        className="btn btn-primary w-30"
        style={{ maxWidth: '500px' }}
        onClick={() => navigate('/')}
      >
        Browser to find cards and add to your favorite list
      </button>
    </>
  );
}

export default FavoriteEmptyList;
