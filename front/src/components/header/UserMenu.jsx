import React, { useContext } from 'react';
import '../../assets/css/header/UserMenu.css';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';

function UserMenu() {
  const navigate = useNavigate();
  const authContext = useContext(AuthContext);

  const onClickLogOut = () => {
    authContext.logout();
    navigate('/');
  };

  const onClickFavorites = () => {
    navigate('/favorites');
  };

  const onClickMyAccount = () => {
    navigate('/my-account');
  };

  const onKeyDownLogOut = () => {
    onClickLogOut();
  };

  const onKeyDownFavorites = () => {
    onClickFavorites();
  };

  const onKeyDownMyAccount = () => {
    onClickMyAccount();
  };

  return (
    <div className="UserMenu">
      <ul>
        <li>
          <button type="button" onClick={onClickMyAccount} onKeyDown={onKeyDownMyAccount} tabIndex={0}>My account</button>
        </li>
        <li>
          <button type="button" onClick={onClickFavorites} onKeyDown={onKeyDownFavorites} tabIndex={0}>Favorites</button>
        </li>
        <li>
          <button type="button" onClick={onClickLogOut} onKeyDown={onKeyDownLogOut} tabIndex={0}>Logout</button>
        </li>
      </ul>
    </div>
  );
}

export default UserMenu;
