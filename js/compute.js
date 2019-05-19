// Window Range
var rmin = -1.5;
var rmax = 1.5;
var cmin = -1;
var cmax = 1;

window.onload = function() {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext('2d');

  canvas.width  = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;

  drawMandlebrot();

  window.addEventListener("wheel", function(event) {
    var drawingWidth = rmax-rmin;
    var drawingHeight = cmax-cmin;

    scroll_locX = event.pageX/canvas.width * drawingWidth + rmin;
    scroll_locY = event.pageY/canvas.height * drawingHeight + cmin;

    // Translate
    rmin -= scroll_locX;
    rmax -= scroll_locX;
    cmin -= scroll_locY;
    cmax -= scroll_locY;

    // Zoom
    rmin *= (1000-event.wheelDelta)/1000;
    rmax *= (1000-event.wheelDelta)/1000;
    cmin *= (1000-event.wheelDelta)/1000;
    cmax *= (1000-event.wheelDelta)/1000;

    // Translate Back
    rmin += scroll_locX;
    rmax += scroll_locX;
    cmin += scroll_locY;
    cmax += scroll_locY;

    drawMandlebrot();

    event.preventDefault();
  });

  window.addEventListener("resize", function(event) {
    var drawingWidth = rmax-rmin;
    var drawingHeight = cmax-cmin;
    var widthRatio = canvas.offsetWidth/canvas.width;
    var heightRatio = canvas.offsetHeight/canvas.height;

    rmax = rmin + drawingWidth*widthRatio;
    cmax = cmin + drawingHeight*heightRatio;

    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    drawMandlebrot();

    event.preventDefault();
  });
}

function drawMandlebrot() {
  console.log(rmin, rmax, cmin, cmax);

  // Drawing Section
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");

  var width = canvas.width;
  var height = canvas.height;

  var imageData = ctx.createImageData(width, height);
  var offset = 0;

  for (var j = 0; j<height; j++) {
    c_imag = ((cmax-cmin)/(height-1) * j) + cmin;
    for (var i = 0; i<width; i++) {
      c_real = ((rmax-rmin)/(width-1) * i) + rmin;

      var counter = insideJulia(c_real, c_imag);

      if (counter >= 100) {
        imageData.data[offset++] = 0;
        imageData.data[offset++] = 0;
        imageData.data[offset++] = 0;
        imageData.data[offset++] = 255;
      } else {
        imageData.data[offset++] = 255;
        imageData.data[offset++] = 255;
        imageData.data[offset++] = 255;
        imageData.data[offset++] = 255;
      }
    }
  }

  ctx.putImageData(imageData, 0, 0, 0, 0, width, height);
  insideJulia(1, 1);

}

function insideJulia(c_real, c_imag) {
  var counter = 0;
  var z_real = 0
  var z_imag = 0
  while (counter < 100 ) {
    z_real_copy = z_real;
    z_imag_copy = z_imag;

    z_real = z_real_copy*z_real_copy - z_imag_copy*z_imag_copy + c_real;
    z_imag = 2*z_real_copy*z_imag_copy + c_imag;

    if (z_real*z_real+z_imag*z_imag < 10) {
      counter++;
    } else {
      break;
    }
  }

  return counter;
}
