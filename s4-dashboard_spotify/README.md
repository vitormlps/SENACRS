# dashboardspotify

Data visualization dashboard for Spotify users to visualize their musical taste and style.

# about

Academic project using https://developer.spotify.com/

Developed by [Gabriel da Costa](https://github.com/GabrielCosta-Abap), [Gabriélen Cunha](https://github.com/Gabrielenfcunha), [Guilherme Menezes](https://github.com/Gui-Menezes), [João Luiz Scherer](https://github.com/jlsfilho2), [Lisandro Cazuza](https://github.com/RLisandro), [Márcio R.W. de Souza](https://github.com/rwsmarcio), [Paola Fantinel](https://github.com/fantinels), [Saul Vargas](https://github.com/SAULvaRGAS88) and [Vitor Lopes](https://github.com/vitormlps).

SENAC/RS - 2022/2

## Installation

These examples run on Node.js. On [its website](http://www.nodejs.org/download/) you can find instructions on how to install it. You can also follow [this gist](https://gist.github.com/isaacs/579814) for a quick and easy way to install Node.js and npm.

Once installed, clone the repository and install its dependencies running:

    $ npm install

### Using your own credentials

You will need to register your app and get your own credentials from the Spotify for Developers Dashboard.

To do so, go to [your Spotify for Developers Dashboard](https://beta.developer.spotify.com/dashboard) and create your application. For the examples, we registered these Redirect URIs:

-   http://localhost:8001 (needed for the implicit grant flow)
-   http://localhost:8001/callback

Once you have created your app, replace the `client_id`, `redirect_uri` and `client_secret` in the examples with the ones you get from My Applications.

### Running

    $ node app
