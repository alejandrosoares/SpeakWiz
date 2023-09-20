import React from 'react';
import '../assets/css/index.css';
import Col from 'react-bootstrap/Col';
import Welcome from './Welcome';
import TopicList from './topics/TopicList';

function Home() {
  return (
    <>
      <Col lg={12}>
        <Welcome />
      </Col>
      <Col lg={12}>
        <TopicList />
      </Col>
    </>
  );
}

export default Home;
