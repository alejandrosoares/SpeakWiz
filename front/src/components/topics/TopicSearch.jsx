import React, { useContext } from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import '../../assets/css/topic/TopicSearch.css';
import { Row, Col } from 'react-bootstrap';
import { TopicContext } from '../../context/TopicContext';

function TopicSearch() {
  const topicContext = useContext(TopicContext);

  const onChangeSearchInput = (event) => {
    const title = event.target.value;
    topicContext.setSearchValue(title);
  };

  return (
    <Row className="TopicSearch">
      <Col xs={12} md={4}>
        <input
          type="text"
          name=""
          id=""
          placeholder="What do you want to talk about?"
          onChange={onChangeSearchInput}
        />
        <div className="TopicSearchBtn">
          <i className="bi bi-search" />
        </div>
      </Col>
    </Row>
  );
}

export default TopicSearch;
