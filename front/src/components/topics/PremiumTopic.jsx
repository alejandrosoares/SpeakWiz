import React, { useContext } from 'react';
import '../../assets/css/topic/Topic.css';
import { Col } from 'react-bootstrap';
import Card from '../cards/Card';
import TagList from '../tags/TagList';
import { RedirectionContext } from '../../context/RedirectionContext';
import { LoginModalContext } from '../../context/LoginModalContext';

function PremiumTopic({ topic }) {
  const loginModalContext = useContext(LoginModalContext);
  const redirectionContext = useContext(RedirectionContext);

  const onClick = () => {
    redirectionContext.setRedirectTo(`/topics/${topic.id}`);
    redirectionContext.setResource(topic);
    loginModalContext.setShow(true);
  };

  return (
    <Col
      onClick={onClick}
      lg={5}
      className="Topic"
      style={{ backgroundColor: topic.style.backgroundColor }}
    >
      <div>
        <Card
          className="TopicCard"
          title={topic.title}
          description={topic.description}
          numberQuestions={topic.numberQuestions}
        />
        <TagList topic={topic} />
      </div>
    </Col>
  );
}

export default PremiumTopic;
