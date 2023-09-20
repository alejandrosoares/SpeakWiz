const formatResponseByStatusCode = (expected, received, data) => {
  const isOk = received === expected;
  return {
    error: !isOk,
    data,
  };
};

export default formatResponseByStatusCode;
