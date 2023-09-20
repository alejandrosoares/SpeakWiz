import React, { useEffect, useState } from 'react';
import '../../assets/css/Favorite.css';
import useFavorites from '../../hooks/useFavorites';

function Favorite({ resourceType, resource }) {
  const [isFavorite, setIsFavorite] = useState(false);
  const {
    isLoaded, getForCurrent, addForCurrent, deleteForCurrent,
  } = useFavorites(resourceType, resource.id);

  useEffect(() => {
    if (isLoaded) setIsFavorite(getForCurrent());
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isLoaded]);

  useEffect(() => {
    if (isLoaded) {
      if (isFavorite) {
        addForCurrent();
      } else {
        deleteForCurrent();
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isFavorite]);

  const onClick = () => {
    setIsFavorite(!isFavorite);
  };

  const onKeyDown = () => {
    onClick();
  };

  return (
    <div className="Favorite" onClick={onClick} onKeyDown={onKeyDown} role="button" tabIndex={0}>
      {isFavorite
        ? <i className="bi bi-heart-fill Favorite-Icon--active" />
        : <i className="bi bi-heart" />}
    </div>
  );
}

export default Favorite;
