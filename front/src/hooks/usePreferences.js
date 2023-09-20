import { useState, useEffect } from 'react';
import preferencesApi from '../apis/preferencesApi';

export default function usePreferences(resourceType, resourceId) {
  const [isLoaded, setIsLoaded] = useState(false);
  const [preferences, setPreferences] = useState({});
  const [itemValue, setItemValue] = useState(null);

  useEffect(() => {
    const loadPreferences = async () => {
      const res = await preferencesApi.getAll();
      if (!res.error) {
        setPreferences(res.data.preferences);
        setIsLoaded(true);
      }
    };
    loadPreferences();
  }, [resourceType, resourceId]);

  const getForCurrent = () => {
    let current = null;
    try {
      const value = preferences[resourceType][resourceId];
      current = { id: resourceId, value };
      setItemValue(value);
    } catch (err) {
    }
    return current;
  };

  const updateCurrent = (resourceValue) => {
    if (resourceValue !== itemValue) {
      try {
        preferences[resourceType][resourceId] = resourceValue;
      } catch (err) {
        preferences[resourceType] = {};
        preferences[resourceType][resourceId] = resourceValue;
      }

      update(resourceValue);
    }
  };

  const update = (resourceValue) => {
    const data = { resourceType, resourceId, resourceValue };
    preferencesApi.create(data);
    setItemValue(resourceValue);
  };

  return {
    isLoaded,
    getForCurrent,
    updateCurrent,
  };
}
