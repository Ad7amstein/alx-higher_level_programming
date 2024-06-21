#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (const ele of list) {
    if (searchElement === ele) {
      num++;
    }
  }
  return num;
};
