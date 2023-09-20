import React, {
  useRef, useState, useContext, useEffect,
} from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../../assets/css/Form.css';
import { Row, Col, Button } from 'react-bootstrap';
import { LoginModalContext } from '../../context/LoginModalContext';
import { RedirectionContext } from '../../context/RedirectionContext';
import { AuthContext } from '../../context/AuthContext';
import useLocalStorage from '../../hooks/useLocalStorage';
import LOCAL_STORAGE from '../../utils/constants/localstorage';
import userApi from '../../apis/userApi';

function LogIn() {
  const navigate = useNavigate();
  const { item: userEmail } = useLocalStorage(LOCAL_STORAGE.EMAIL, '');
  const authContext = useContext(AuthContext);
  const loginModalContext = useContext(LoginModalContext);
  const redirectionContext = useContext(RedirectionContext);
  const formRef = useRef(null);
  const [errorMessage, setErrorMessage] = useState(null);

  useEffect(() => {
    loadEmail();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const loadEmail = () => {
    formRef.current.email.value = userEmail;
  };

  const onSubmitForm = async (event) => {
    event.preventDefault();
    setErrorMessage(null);

    const formData = new FormData(formRef.current);
    const data = {
      email: formData.get('email'),
      password: formData.get('password'),
    };
    const remember = formData.get('remember');
    const res = await userApi.logIn(data);
    handleLogInResponse(res, { remember });
  };

  const handleLogInResponse = (res, { remember }) => {
    if (res.error) {
      setErrorMessage(res.data);
    } else {
      const user = res.data;
      authContext.login(user, remember);
      loginModalContext.setShow(false);
      navigate(redirectionContext.redirectTo || '/');
    }
  };

  return (
    <Col xs={12} className="Form">
      <Row>
        <Col xs={12} className="Form-Title">
          <h1>Log In FlashCard</h1>
        </Col>
        <Col xs={12}>
          <form onSubmit={onSubmitForm} ref={formRef}>
            <div>
              <span className="text-danger font-weight-bold">{errorMessage}</span>
            </div>
            <label className="Form-Label" htmlFor="email">
              <input id="email" type="email" name="email" required placeholder="Email" />
            </label>
            <label className="Form-Label" htmlFor="password">
              <input id="password" type="password" name="password" required placeholder="Password" />
            </label>
            <Row className="pt-4 pb-4">
              <Col xs={6} className="d-flex justify-content-center">
                <label className="Form-Label" htmlFor="remember">
                  <input className="Form-Remember" id="remember" type="checkbox" name="remember" />
                  <span>Remember me</span>
                </label>
              </Col>
              <Col xs={6} className="d-flex justify-content-center">
                <Link to="/sign-up">
                  <span>Sign Up</span>
                </Link>
              </Col>
            </Row>
            <div className="button-container d-flex justify-content-center">
              <Button className="Form-Btn d-flex justify-content-center" type="submit" variant="primary">
                <span>Log In </span>
              </Button>
            </div>
          </form>
        </Col>
      </Row>
    </Col>
  );
}

export default LogIn;
