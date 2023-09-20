import { useState } from 'react';

export default function useLocalStorage(key, defaultValue) {
  const parsedItem = defaultValue || JSON.parse(localStorage.getItem(key));
  const [item, setItem] = useState(parsedItem);

  const saveItem = (newItem) => {
    localStorage.setItem(key, JSON.stringify(newItem));
    setItem(item);
  };

  const removeItem = (removedItem) => {
    localStorage.removeItem(key, JSON.stringify(removedItem));
    setItem(defaultValue);
  };

  return { item, saveItem, removeItem };
}
