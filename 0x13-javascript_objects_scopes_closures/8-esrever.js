#!/usr/bin/node

exports.esrever = function (list) {
  const newList = []; let y = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[y] = list[i];
    y++;
  }
  return newList;
};
