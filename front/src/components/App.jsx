import React from 'react';
import '../assets/css/App.css';
import { Routes, Route } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { TopicProvider } from '../context/TopicContext';
import { AuthProvider } from '../context/AuthContext';
import { LoginModalProvider } from '../context/LoginModalContext';
import { RedirectionProvider } from '../context/RedirectionContext';
import Header from './header/Header';
import Home from './Home';
import TopicDetail from './topics/TopicDetail';
import LogIn from './users/LogIn';
import SignUp from './users/SignUp';
import Error404 from './Error404';
import FavoriteList from './favorite/FavoriteList';
import MyAccount from './users/MyAccount';
import AuthRoute from './auth/AuthRoute';

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      ,
      <Route path="/topics/:id" element={<TopicDetail />} />
      ,
      <Route
        path="/favorites/"
        element={(
          <AuthRoute>
            <FavoriteList />
          </AuthRoute>
              )}
      />
      ,
      <Route path="/log-in" element={<LogIn />} />
      ,
      <Route path="/sign-up" element={<SignUp />} />
      ,
      <Route
        path="/my-account"
        element={(
          <AuthRoute>
            <MyAccount />
          </AuthRoute>
              )}
      />
      ,
      <Route path="/*" element={<Error404 />} />
      ,
    </Routes>
  );
}

function AppUI() {
  return (
    <Container className="App" fluid="true">
      <Header />
      <Row className="App-container">
        <Col lg={8}>
          <Row className="App-Page">
            <AppRoutes />
          </Row>
        </Col>
      </Row>
    </Container>
  );
}

function App() {
  return (
    <RedirectionProvider>
      <LoginModalProvider>
        <AuthProvider>
          <TopicProvider>
            <AppUI />
          </TopicProvider>
        </AuthProvider>
      </LoginModalProvider>
    </RedirectionProvider>
  );
}

export default App;
