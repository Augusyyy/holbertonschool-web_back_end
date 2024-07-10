// 推荐在循环对象属性的时候，使用for...in,在遍历数组的时候的时候使用for...of。
//
// for...in循环出的是key，for...of循环出的是value
//
// 注意，for...of是ES6新引入的特性。修复了ES5引入的for...in的不足
//
// for...of不能循环普通的对象，需要通过和Object.keys()搭配使用
export default function appendToEachArrayValue(array, appendString) {
  const array2 = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    array2[idx] = appendString + value;
  }

  return array2;
}
