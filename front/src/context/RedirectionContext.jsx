import React, { createContext, useState } from 'react';

export const RedirectionContext = createContext();

export function RedirectionProvider({ children }) {
  const [redirectTo, setRedirectTo] = useState(null);
  const [resource, setResource] = useState(null);

  return (
    <RedirectionContext.Provider value={{
      redirectTo,
      setRedirectTo,
      resource,
      setResource,
    }}
    >
      {children}
    </RedirectionContext.Provider>
  );
}
