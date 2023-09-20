const buildGetParams = (params) => {
  const urlParams = new URLSearchParams(params);
  return `?${urlParams.toString()}`;
};

export default buildGetParams;
