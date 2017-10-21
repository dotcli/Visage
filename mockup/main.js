// click to turn off / on

// display indices!

var jewel1 = [];
// TODO
var jewel2 = [];
var jewel3 = [];
var jewels = [
  [],
  [],
  []
];

var jewelRadius = 40;
var jewelAngle = Math.PI / 3;

var triLength = 400;

function arrangePixels(pixel, iJewel, iPixel) {
  var pixelCenters = [
    [100, 100],
    [100 + triLength, 100],
    [100 + (triLength / 2), 100 + triLength * Math.sin(Math.PI / 3)],
  ];
  if (iPixel === 0) {
    pixel.setAttribute('cx', pixelCenters[iJewel][0]);
    pixel.setAttribute('cy', pixelCenters[iJewel][1]);
    return;
  }
  var angle = jewelAngle * (iPixel - 1 + 0.5);
  var cx = pixelCenters[iJewel][0] + Math.cos(angle) * jewelRadius;
  var cy = pixelCenters[iJewel][1] + Math.sin(angle) * jewelRadius;
  pixel.setAttribute('cx', cx);
  pixel.setAttribute('cy', cy);
}

var allPixels = document.querySelectorAll('circle');

for (var i = 0; i < allPixels.length; i++) {
  var p = allPixels[i];
  var iJewel = Math.floor(i / 7);
  var iPixel = i % 7;

  p.dataset.iJewel = iJewel;
  p.dataset.iPixel = iPixel;
  arrangePixels(p, iJewel, iPixel);
  p.addEventListener('click', clickSwitchFill);
  jewels[iJewel].push(p);
}

function clickSwitchFill(e) {
  var fill = e.target.getAttribute('fill');
  if (fill === 'black') e.target.setAttribute('fill', 'white');
  else if (fill === 'white') e.target.setAttribute('fill', 'black');
}

function fill() {

}