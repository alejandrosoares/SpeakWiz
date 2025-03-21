import React, { useRef, useState } from 'react';
import { Button, Row, Col } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import '../../assets/css/Form.css';
import PASSWORD_REGEX from '../../utils/constants/regexs';
import useLocalStorage from '../../hooks/useLocalStorage';
import LOCAL_STORAGE from '../../utils/constants/localstorage';
import userApi from '../../apis/userApi';

function SignUp() {
  const { saveItem: setUserEmail } = useLocalStorage(LOCAL_STORAGE.EMAIL, '');
  const navigate = useNavigate();
  const formRef = useRef(null);
  const [emailError, setEmailError] = useState(null);
  const [passError, setPassError] = useState(null);

  const onSubmitForm = async (event) => {
    event.preventDefault();
    resetErrorMessages();

    const formData = new FormData(formRef.current);
    const data = {
      name: formData.get('name'),
      email: formData.get('email'),
      password: formData.get('password'),
    };
    const res = await userApi.signUp(data);
    handleSignUpResponse(res);
  };

  const handleSignUpResponse = (res) => {
    if (res.error) {
      setEmailError(res.data.email?.[0]);
      setPassError(res.data.password?.[0]);
    } else {
      saveEmailToLogIn();
      navigate('/log-in');
    }
  };

  const saveEmailToLogIn = () => {
    const formData = new FormData(formRef.current);
    setUserEmail(formData.get('email'));
  };

  const resetErrorMessages = () => {
    setEmailError(null);
    setPassError(null);
  };

  return (
    <Col xs={12} className="Form">
      <Row>
        <Col xs={12} className="Form-Title">
          <h1>Sign Up</h1>
        </Col>
        <Col xs={12}>
          <form onSubmit={onSubmitForm} ref={formRef}>
            <label className="Form-Label" htmlFor="name">
              <input id="name" type="text" name="name" required placeholder="Name" minLength="3" />
            </label>
            <label className="Form-Label" htmlFor="email">
              <span className="text-danger">{emailError}</span>
              <input id="email" type="email" name="email" required placeholder="Email" />
            </label>
            <label className="Form-Label" htmlFor="password">
              <span className="text-danger">{passError}</span>
              <input
                id="password"
                type="password"
                name="password"
                required
                placeholder="Password"
                pattern={PASSWORD_REGEX}
                title="Must contain at least one number, one uppercase and lowercase letter. At least 8 or more characters."
              />
            </label>
            <div className="button-container">
              <Button className="Form-Btn" type="submit" variant="primary">Sign Up</Button>
            </div>
          </form>
        </Col>
      </Row>
    </Col>
  );
}

export default SignUp;
