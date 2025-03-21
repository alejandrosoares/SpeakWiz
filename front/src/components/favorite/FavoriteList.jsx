import React, { useEffect, useState } from 'react';
import '../../assets/css/topic/Topic.css';
import { Row } from 'react-bootstrap';
import LinkTopic from '../topics/LinkTopic';
import SectionLoader from '../loaders/SectionLoader';
import favoritesApi from '../../apis/favoritesApi';
import addRandomColorsTo from '../../utils/colors/addRandomColorsTo';
import SectionTitle from '../titles/SectionTitle';
import FavoriteEmptyList from './FavoriteEmptyList';

function FavoriteList() {
  const [favoriteList, setFavoriteList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadFavorites();
  }, []);

  const loadFavorites = async () => {
    const res = await favoritesApi.getAll();
    if (!res.error) {
      const resources = res.data;
      const resourcesWithColors = addRandomColorsTo(resources);
      setFavoriteList(resourcesWithColors);
      setLoading(false);
    }
  };

  return (
    <>
      <SectionTitle title="My Favorites" />

      {loading && <SectionLoader color="black" />}

      {!loading && favoriteList.length === 0 && <FavoriteEmptyList />}

      <Row className="TopicList">
        {favoriteList?.map((topic) => <LinkTopic topic={topic} key={topic.id} />)}
      </Row>

    </>
  );
}

export default FavoriteList;
