import { useState, useEffect } from 'react';
import favoritesApi from '../apis/favoritesApi';

export default function useFavorites(resourceType, resourceId) {
  const [isLoaded, setIsLoaded] = useState(false);
  const [favorite, setFavorite] = useState(null);
  const [isFavorite, setIsFavorite] = useState(false);

  useEffect(() => {
    const loadFavorite = async () => {
      const res = await favoritesApi.get(resourceType, resourceId);
      if (!res.error) {
        setFavorite(res.data);
        setIsFavorite(Boolean(res.data));
        setIsLoaded(true);
      }
    };
    loadFavorite();
  }, [resourceType, resourceId]);

  const getForCurrent = () => isFavorite;

  const deleteForCurrent = () => {
    if (isFavorite) del();
  };

  const addForCurrent = () => {
    if (!isFavorite) add();
  };

  const add = async () => {
    const data = { resourceType, resourceId };
    const res = await favoritesApi.create(data);
    setIsFavorite(true);
    setFavorite(res.data);
  };

  const del = async () => {
    await favoritesApi.delete(favorite.id);
    setIsFavorite(false);
  };

  return {
    isLoaded,
    getForCurrent,
    addForCurrent,
    deleteForCurrent,
  };
}
