import React, { useContext } from 'react';
import '../../assets/css/topic/Topic.css';
import { Link } from 'react-router-dom';
import { Col } from 'react-bootstrap';
import Card from '../cards/Card';
import PremiumTag from '../tags/PremiumTag';
import { TopicContext } from '../../context/TopicContext';

function LinkTopic({ topic }) {
  const topicContext = useContext(TopicContext);

  const onClick = () => {
    topicContext.setSearchValue('');
  };

  return (
    <Col
      lg={5}
      className="Topic"
      style={{ backgroundColor: topic.style.backgroundColor }}
      onClick={onClick}
    >
      <Link to={`/topics/${topic.id}`} state={topic}>
        {topic.premium && <PremiumTag />}
        <Card
          className="TopicCard"
          title={topic.title}
          description={topic.description}
          numberQuestions={topic.numberQuestions}
        />
      </Link>
    </Col>
  );
}

export default LinkTopic;
