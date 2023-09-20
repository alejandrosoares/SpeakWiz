import React, {
  createContext, useState, useEffect,
} from 'react';
import userApi from '../apis/userApi';
import authenticationToken from '../utils/authentication';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const token = authenticationToken.getFromLocalAndSave();

  useEffect(() => {
    if (token) loadUser();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const loadUser = async () => {
    const res = await userApi.getUserByToken();
    handleUserResponse(res);
  };

  const handleUserResponse = (res) => {
    const receivedUser = res.data;
    if (receivedUser.email) {
      login(receivedUser);
    } else {
      logout();
    }
  };

  const login = (loggedUser, rememberUser) => {
    const authToken = token || loggedUser.token;
    setUser(loggedUser);
    authenticationToken.save(authToken, rememberUser);
  };

  const logout = () => {
    setUser(null);
    authenticationToken.remove();
  };

  return (
    <AuthContext.Provider value={{
      user,
      login,
      logout,
    }}
    >
      {children}
    </AuthContext.Provider>
  );
}
