import React, { useState, useEffect, useContext } from 'react';
import '../../assets/css/topic/Topic.css';
import { Row, Col } from 'react-bootstrap';
import { useLocation, useParams } from 'react-router-dom';
import { RedirectionContext } from '../../context/RedirectionContext';
import { AuthContext } from '../../context/AuthContext';
import TopicSlider from './TopicSlider';
import topicApi from '../../apis/topicApi';
import Feedback from '../feedback/Feedback';
import { ResourceType } from '../../utils/feedback';
import Favorite from '../favorite/Favorite';

function TopicDetail() {
  const location = useLocation();
  const redirectionContext = useContext(RedirectionContext);
  const authContext = useContext(AuthContext);
  const { id: topicId } = useParams();
  const [stateQuestions, setQuestions] = useState([]);
  const [topic, setTopic] = useState(location.state || redirectionContext.resource);

  useEffect(() => {
    async function loadingQuestions() {
      try {
        const res = await topicApi.getById(topicId);
        const topicDetail = res.data;
        const questions = topicDetail.questions.map((question, id) => ({ question, id }));
        console.log('questions:', questions);
        setTopic(topicDetail);
        setQuestions(questions);
      } catch (error) {
        console.log('Error fetching topic details: ', error);
      }
    }
    loadingQuestions();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [topicId]);

  return (
    <>
      <Row className="TopicDetail">
        {
          authContext.user && topic
          && <Favorite resourceType={ResourceType.Topic} resource={topic} />
        }
        <Col xs={12}>
          <h1 className="TopicDetail-Title">{topic?.title}</h1>
        </Col>
        <Col xs={12}>
          <h2 className="TopicDetail-Description text-muted">{topic?.description}</h2>
        </Col>
        <Col xs={12}>
          <TopicSlider slides={stateQuestions} />
        </Col>
      </Row>
      {authContext.user && topic && <Feedback resourceType={ResourceType.Topic} resource={topic} />}

    </>
  );
}

export default TopicDetail;
