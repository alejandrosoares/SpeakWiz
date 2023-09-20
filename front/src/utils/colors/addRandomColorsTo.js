import getRandomColors from './getRandomColors';

const addRandomColorsTo = (items) => {
  const colors = getRandomColors(items.length);
  const itemsWithColor = items.map((item, index) => {
    const newItem = { ...item };
    newItem.style = { backgroundColor: colors[index] };
    return newItem;
  });
  return itemsWithColor;
};

export default addRandomColorsTo;
