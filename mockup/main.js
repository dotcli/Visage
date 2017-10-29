// transform into vue!
var JEWEL_COUNT = 3;
var PIXELS_EACH_JEWEL = 7;
var PIXEL_COUNT = JEWEL_COUNT * PIXELS_EACH_JEWEL;
var STARTER_COLOR = 'white';

new Vue({
  el: '#app',
  data: {
    jewelRadius: 40,
    jewelAngle: Math.PI / 3,
    triLength: 400,
    pixels: [], // initialize in created hook
  },
  computed: {
    pixelCenters: function() {
      return [
        [100, 100],
        [100 + this.triLength, 100],
        [100 + (this.triLength / 2), 100 + this.triLength * Math.sin(Math.PI / 3)],
      ];
    },
    pythonCode: function() {
      var pixelColors = this.pixels.map(function(p) {
        var color = tinycolor(p.fill);
        if (color.isValid() === false) throw new Error('pixel fill is not valid color', p.fill);
        return [color._r, color._g, color._b];
      });
      return JSON.stringify(pixelColors);
    }
  },
  created: function() {
    for (var i = 0; i < PIXEL_COUNT; i++) {
      var p = {
        fill: STARTER_COLOR,
        x: 0,
        y: 0,
      };

      var iJewel = Math.floor(i / PIXELS_EACH_JEWEL);
      var iPixel = i % 7;
      this.arrangePixels(p, iJewel, iPixel);
      this.pixels[i] = p;
    }
  },
  methods: {
    arrangePixels: function (pixel, iJewel, iPixel) {
      if (iPixel === 0) {
        pixel.x = this.pixelCenters[iJewel][0];
        pixel.y = this.pixelCenters[iJewel][1];
        return;
      }
      var angle = this.jewelAngle * (iPixel - 1 + 0.5);
      pixel.x = this.pixelCenters[iJewel][0] + Math.cos(angle) * this.jewelRadius;
      pixel.y = this.pixelCenters[iJewel][1] + Math.sin(angle) * this.jewelRadius;
    },
    setPixelColor: function(e) {
      // set pixel color and force render update
      var targetIndex = Number(e.target.dataset.index);
      var targetPixel = this.pixels[targetIndex];
      if (targetPixel.fill === 'black') targetPixel.fill = 'white';
      else if (targetPixel.fill === 'white') targetPixel.fill = 'black';
      // force reactivity
      this.$set(this.pixels, targetIndex, targetPixel);
    }
  },
});


/* 
TODO make color palette creator
- create color based on CSS value input?
- plus and minus to manage
- click to choose that color
- click pixels to color them

Nice to have:
- color palette stays on the page as fixed element, 
but shrinkable / expandable


*/