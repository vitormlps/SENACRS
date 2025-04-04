function download() {
  let div =
    document.getElementById('all');

  html2canvas(div).then(
    function (canvas) {
      var a = document.createElement("a");
      a.href = canvas.toDataURL()
      a.download = 'Meu resultado'
      a.click();

    })
}

function realizarPesquisa() {
  window.open('https://forms.gle/3fD8GF7RBFcX3v637', '_blank');
}