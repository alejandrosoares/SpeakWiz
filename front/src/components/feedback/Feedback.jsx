import React, { useEffect, useRef, useState } from 'react';
import '../../assets/css/Feedback.css';
import { Row, Col, Button } from 'react-bootstrap';
import { FeedbackType } from '../../utils/feedback';
import usePreferences from '../../hooks/usePreferences';

function Feedback({ resourceType, resource }) {
  const { isLoaded, getForCurrent, updateCurrent } = usePreferences(resourceType, resource.id);
  const [like, setLike] = useState(false);
  const [dislike, setDislike] = useState(false);
  const feedbackRef = useRef({ like, dislike });

  useEffect(() => {
    if (isLoaded) {
      const preferenceResource = getForCurrent();
      if (preferenceResource) {
        if (preferenceResource.value === FeedbackType.Like) {
          setLike(true);
        } else if (preferenceResource.value === FeedbackType.Dislike) {
          setDislike(true);
        }
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isLoaded]);

  useEffect(() => {
    feedbackRef.current.like = like;
    if (like && dislike) setDislike(false);
    if (isLoaded) {
      if (like) updateCurrent(FeedbackType.Like);
      if (!like && !dislike) updateCurrent(FeedbackType.Removed);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [like]);

  useEffect(() => {
    feedbackRef.current.dislike = dislike;
    if (dislike && like) setLike(false);
    if (isLoaded) {
      if (dislike) updateCurrent(FeedbackType.Dislike);
      if (!dislike && !like) updateCurrent(FeedbackType.Removed);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dislike]);

  return (
    <Row className="Feedback">
      <Col xs={12}>
        <span className="Feedback-Title">Did you like it?</span>
        <div>
          <Button className="Feedback-Btn" onClick={() => setLike(!like)}>
            {like
              ? <i className="bi bi-hand-thumbs-up-fill" />
              : <i className="bi bi-hand-thumbs-up" />}
          </Button>
          <Button className="Feedback-Btn" onClick={() => setDislike(!dislike)}>
            {dislike
              ? <i className="bi bi-hand-thumbs-down-fill" />
              : <i className="bi bi-hand-thumbs-down" />}
          </Button>
        </div>
      </Col>
    </Row>
  );
}

export default Feedback;
