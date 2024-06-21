#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
