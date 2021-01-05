function binarySearch(element, array) {
  let counter = true;
  let half = Math.ceil(array.length / 2);
  let start = 0;
  let end = array.length;
  if (element == array[length]) {
    console.log("ELEMENT FOUND -> ", array[half]);
  } else if (element > array[length]) {
    start = half;
  } else if (element < array[length]) {
    start = 0;
    end = half;
  }
}
