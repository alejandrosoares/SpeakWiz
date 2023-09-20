const formatDate = (strDate) => {
  function getDay(date) {
    const day = date.getDate();
    return day > 9 ? day : `0${day}`;
  }
  const date = new Date(strDate);
  const day = getDay(date);
  const month = date.getMonth();
  const year = date.getFullYear();
  return `${day}.${month}.${year}`;
};

export default formatDate;
