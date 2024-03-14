const formatDate = (strDate) => {
  const date = new Date(strDate);
  const day = date.getDate().toString().padStart(2, '0');
  const month = date.getMonth().toString().padStart(2, '0');
  const year = date.getFullYear();
  return `${day}.${month}.${year}`;
};

export default formatDate;
