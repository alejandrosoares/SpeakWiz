import React, { useState, useEffect, useContext } from 'react';
import '../../assets/css/topic/Topic.css';
import { Row, Col } from 'react-bootstrap';
import { useLocation, useParams } from 'react-router-dom';
import { RedirectionContext } from '../../context/RedirectionContext';
import { AuthContext } from '../../context/AuthContext';
import TopicSlider from './TopicSlider';
import addRandomColorsTo from '../../utils/colors/addRandomColorsTo';
import cardApi from '../../apis/cardApi';
import topicApi from '../../apis/topicApi';
import Feedback from '../feedback/Feedback';
import { ResourceType } from '../../utils/feedback';
import Favorite from '../favorite/Favorite';

function TopicDetail() {
  const location = useLocation();
  const redirectionContext = useContext(RedirectionContext);
  const authContext = useContext(AuthContext);
  const { id: topicId } = useParams();
  const [stateCards, setCards] = useState([]);
  const [topic, setTopic] = useState(location.state || redirectionContext.resource);

  useEffect(() => {
    async function loadingCards() {
      if (!topic) {
        const res = await topicApi.getById(topicId);
        setTopic(res.data);
      } else {
        loadCards();
      }
    }
    loadingCards();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [topic]);

  const loadCards = async () => {
    const authIsNeeded = topic.premium;
    const res = await cardApi.getAll(topic.id, authIsNeeded);
    const cards = res.data;
    const cardsWithColor = addRandomColorsTo(cards);
    setCards(cardsWithColor);
  };

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
          <TopicSlider slides={stateCards} />
        </Col>
      </Row>
      {authContext.user && topic && <Feedback resourceType={ResourceType.Topic} resource={topic} />}

    </>
  );
}

export default TopicDetail;
