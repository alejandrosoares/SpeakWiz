import COLORS from './constants';

function getRandomColors(numbers) {
  const lenAvailableColors = COLORS.length;
  const colors = [];
  // eslint-disable-next-line no-plusplus
  for (let i = 0; i < numbers; i++) {
    const color = COLORS[Math.floor(Math.random() * lenAvailableColors)];
    colors.push(color);
  }
  return colors;
}

export default getRandomColors;
