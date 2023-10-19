$(document).ready(function () {

  function addData(data) {
    $('table tbody').prepend(
      '<tr>' +
      '<td>' + data.date + '</td>' +
      '<td>' + data.alarma + '</td>' +
      '<td>' + data.value + '</td>' +
      '<td><a href="#" class="button"> Ver detalles </a></td>' +
      '</tr>'
    )
  }

  //connect to the socket server.
  //   var socket = io.connect("http://" + document.domain + ":" + location.port);
  var socket = io.connect();

  //receive details from server
  socket.on("updateSensorData", function (msg) {
    console.log("Received sensorData :: " + msg.date + " :: " + msg.value);
    addData(msg);
  });
});
