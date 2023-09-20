import { useContext } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import { RedirectionContext } from '../../context/RedirectionContext';

function AuthRoute({ children }) {
  const navigate = useNavigate();
  const location = useLocation();
  const authContext = useContext(AuthContext);
  const redirectionContext = useContext(RedirectionContext);

  if (!authContext.user) {
    redirectionContext.setRedirectTo(location.pathname);
    navigate('/log-in');
    return null;
  }

  return children;
}

export default AuthRoute;
