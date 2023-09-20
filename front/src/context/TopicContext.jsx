import React, { createContext, useState, useEffect } from 'react';
import addRandomColorsTo from '../utils/colors/addRandomColorsTo';
import topicApi from '../apis/topicApi';

export const TopicContext = createContext();

export function TopicProvider({ children }) {
  const [topics, setTopics] = useState([]);
  const [filteredTopics, setFilteredTopics] = useState([]);
  const [searchValue, setSearchValue] = useState(null);

  useEffect(() => {
    loadTopics();
  }, []);

  const loadTopics = async () => {
    const res = await topicApi.getAll();
    const retrievedTopics = res.data;
    const topicsWithColors = addRandomColorsTo(retrievedTopics);
    setTopics(topicsWithColors);
  };

  const filterByTitle = (topicsToFilter, title) => topicsToFilter.filter((topic) => {
    const topicTitle = topic.title.toLowerCase();
    const titleToSearch = title.toLowerCase();
    return topicTitle.includes(titleToSearch);
  });

  useEffect(() => {
    if (searchValue) setFilteredTopics(filterByTitle(topics, searchValue));
  }, [topics, searchValue]);

  return (
    <TopicContext.Provider value={{
      topics,
      setTopics,
      filteredTopics,
      setFilteredTopics,
      searchValue,
      setSearchValue,
    }}
    >
      {children}
    </TopicContext.Provider>
  );
}
