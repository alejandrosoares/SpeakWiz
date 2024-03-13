import React, { useContext } from 'react';
import '../../assets/css/topic/Topic.css';
import { Link } from 'react-router-dom';
import { Col } from 'react-bootstrap';
import Card from '../cards/Card';
import TagList from '../tags/TagList';
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
        <Card
          className="TopicCard"
          title={topic.title}
          description={topic.description}
          numberQuestions={topic.numberQuestions}
        />
        <TagList topic={topic} />
      </Link>
    </Col>
  );
}

export default LinkTopic;
