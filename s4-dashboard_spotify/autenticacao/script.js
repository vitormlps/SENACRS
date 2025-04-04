var stateKey = 'spotify_auth_state';

/**
 * Obtains parameters from the hash of the URL
 * @return Object
 */
function getHashParams() {
  var hashParams = {};
  var e, r = /([^&;=]+)=?([^&;]*)/g,
    q = window.location.hash.substring(1);
  while (e = r.exec(q)) {
    hashParams[e[1]] = decodeURIComponent(e[2]);
  }
  return hashParams;
}

function generateRandomString(length) {
  var text = '';
  var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  for (var i = 0; i < length; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
};

function loggar(urlRedirect) {

  var client_id = 'fcb76e2b2088499183a2caaa6f341b46'; // Your client id
  // var redirect_uri = 'http://localhost:8001/autenticacao/index.html'; // Your redirect uri
  var redirect_uri = 'https://vitormlps.github.io/dashboardspotify/autenticacao/index.html'; // Your redirect uri
  console.log("redirect to:" + redirect_uri);
  var state = btoa(urlRedirect);

  localStorage.setItem(stateKey, state);
  var scope = 'user-read-private user-read-email user-top-read';

  var url = 'https://accounts.spotify.com/authorize';
  url += '?response_type=token';
  url += '&client_id=' + encodeURIComponent(client_id);
  url += '&scope=' + encodeURIComponent(scope);
  url += '&redirect_uri=' + encodeURIComponent(redirect_uri);
  url += '&state=' + encodeURIComponent(state);

  window.location = url;
}

function deslogar() {

  const url = 'https://www.spotify.com/logout/'
  const spotifyLogoutWindow = window.open(url, 'Spotify Logout', 'width=700,height=500,top=40,left=40')
  setTimeout(() => {
    spotifyLogoutWindow.close();
    //window.location = 'http://localhost:8001/';
    window.location = 'https://vitormlps.github.io/dashboardspotify/';
  }, 2000)
}