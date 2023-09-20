import React, { useContext, useEffect, useState } from 'react';
import '../../assets/css/topic/Topic.css';
import { Row } from 'react-bootstrap';
import { TopicContext } from '../../context/TopicContext';
import TopicSearch from './TopicSearch';
import LoginModal from '../modals/LoginModal';
import LinkTopic from './LinkTopic';
import PremiumTopic from './PremiumTopic';
import { AuthContext } from '../../context/AuthContext';
import { LoginModalContext } from '../../context/LoginModalContext';
import SectionLoader from '../loaders/SectionLoader';

function TopicList() {
  const topicContext = useContext(TopicContext);
  const authContext = useContext(AuthContext);
  const loginModalContext = useContext(LoginModalContext);
  const [loading, setLoading] = useState(true);

  const getTopicList = () => ((topicContext.searchValue?.length > 0)
    ? topicContext.filteredTopics
    : topicContext.topics);

  useEffect(() => {
    if (topicContext.topics.length) setLoading(false);
  }, [topicContext.topics]);

  return (
    <>
      <TopicSearch />

      {loading && <SectionLoader color="black" />}

      <Row className="TopicList">
        {getTopicList()?.map((topic) => (
          !authContext.user && topic.premium
            ? <PremiumTopic topic={topic} key={topic.id} />
            : <LinkTopic topic={topic} key={topic.id} />
        ))}
      </Row>

      { loginModalContext.show && <LoginModal /> }
    </>
  );
}

export default TopicList;
