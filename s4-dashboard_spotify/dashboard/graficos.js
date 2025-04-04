window.onload = function () {
    var accessKey = 'spotify_access';
    const queryString = window.location.search;
    //const urlParams = new URLSearchParams(queryString);
    //const access_token = urlParams.get('access_token')
    const access_token = localStorage.getItem(accessKey);
    // Pega o User Display Name da API
    fetch('https://api.spotify.com/v1/me', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token,
        }
    }).then(async (response) => {
        const user_data = await response.json()
        document.getElementById('nome').innerHTML = user_data.display_name
    });

    // Define um array de cores para aplicar nos gráficos
    CanvasJS.addColorSet("podio", [
        "#f7a725", //ouro
        "#e8e8e8", //prata
        "#d66e45", //bronze
        "#2E8B57", //tons de verde
        "#3CB371",
        "#90EE90",
        "#2E8B57",
        "#3CB371",
        "#90EE90",
        "#2E8B57",
    ]);

    CanvasJS.addColorSet("tonsDeVerde", [
        "#2F4F4F",
        "#008080",
        "#2E8B57",
        "#3CB371",
        "#90EE90"
    ]);

    // Pega o Top Artists do usuário para definir 
    // os gráficos de gênero e top 3 artistas
    fetch('https://api.spotify.com/v1/me/top/artists', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token,
        }
    }).then(async (response) => {
        response.json().then((data) => {

            let genero = data.items[0].genres[0]
            document.getElementById('estilo').innerHTML = genero

            let artistasData = []
            let generosData = []

            if (!data) {
                return
            }

            // Lógica de consumo dos fetchs
            // Para generos
            let count1 = 40
            data.items.forEach((artist) => {
                count1 -= 4
                generosDataPoint = {
                    y: count1,
                    label: artist.genres[0]
                }
                if (count1 > 0) {
                    generosData.push(generosDataPoint)
                }
            })

            // Para artistas
            let count2 = 40
            data.items.forEach((artist) => {
                count2 -= 10
                artistaDataPoint = {
                    y: count2,
                    label: artist.name
                }
                if (count2 > 0) {
                    artistasData.push(artistaDataPoint)
                }
            })

            // Definição do gráfico de gêneros
            var chartGeneros = new CanvasJS.Chart("generos", {
                animationEnabled: true,
                theme: "dark2", // "light1", "light2", "dark1", "dark2"
                backgroundColor: "",
                colorSet: "tonsDeVerde",
                // width: 500,
                title: {
                    text: "Gêneros mais escutados",
                    fontFamily: "roboto",
                    fontColor: "#1DB954",
                    // fontSize: "",
                    fontWeight: "bold",
                    horizontalAlign: "left",
                },
                toolTip: {
                    enabled: false
                },
                data: [{
                    type: "doughnut",
                    showInLegend: false,
                    indexLabel: "{ label }",
                    indexLabelFontSize: 16,
                    indexLabelFontColor: "white",
                    indexLabelPlacement: "outside",
                    fillOpacity: .85,
                    dataPoints: generosData
                }]
            });

            // Definição do gráfico de artistas
            var chartArtistas = new CanvasJS.Chart("artistas", {
                animationEnabled: true,
                theme: "dark2",
                backgroundColor: "",
                colorSet: "podio",
                title: {
                    text: "Top 3 artistas mais ouvidos",
                    fontFamily: "roboto",
                    fontColor: "#1DB954",
                    // fontSize: "",
                    fontWeight: "bold",
                    horizontalAlign: "left",
                },
                toolTip: {
                    enabled: false
                },
                axisX: {
                    title: "",
                    labelFontColor: " ",
                    gridThickness: 0,
                    tickThickness: 0,
                },
                axisY: {
                    title: "",
                    labelFontColor: " ",
                    gridThickness: 0,
                    tickThickness: 0,
                },
                data: [{
                    type: "column",
                    showInLegend: false,
                    indexLabel: "{ label }",
                    indexLabelFontSize: 18,
                    indexLabelFontColor: "white",
                    indexLabelPlacement: "outside",
                    fillOpacity: .85,
                    dataPoints: artistasData,
                }]
            });

            chartArtistas.render();
            chartGeneros.render();

        }).catch((err) => {
            console.log(err);
        })
    });

    // Pega o Top Tracks do usuário para definir 
    // o gráfico top 10 músicas
    fetch('https://api.spotify.com/v1/me/top/tracks', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token,
        }
    })
        .then(async (response) => {

            response.json().then((data) => {

                let aDataPoints = []

                if (!data) {
                    return
                }

                let count = 40
                data.items.forEach((track) => {
                    count -= 4
                    oDataPoint = {
                        y: count,
                        label: track.name
                    }

                    if (count > 0) {
                        aDataPoints.push(oDataPoint)
                    }
                })

                var chartMusicas = new CanvasJS.Chart("musicas", {
                    animationEnabled: true,
                    theme: "dark2", // "light1", "light2", "dark1", "dark2"
                    backgroundColor: "",
                    colorSet: "podio",
                    title: {
                        text: "Top 10 músicas mais ouvidas",
                        fontFamily: "roboto",
                        fontColor: "#1DB954",
                        // fontSize: "",
                        fontWeight: "bold",
                        horizontalAlign: "left",
                    },
                    toolTip: {
                        enabled: false
                    },
                    axisX: {
                        title: "",
                        labelFontColor: " ",
                        gridThickness: 0,
                        tickThickness: 0,
                        margin: -48,
                    },
                    axisY: {
                        title: "",
                        labelFontColor: " ",
                        gridThickness: 0,
                        tickThickness: 0,
                    },
                    data: [{
                        type: "column",
                        showInLegend: false,
                        indexLabel: "{ label }",
                        indexLabelFontSize: 14,
                        indexLabelFontColor: "white",
                        indexLabelPlacement: "outside",
                        fillOpacity: .85,
                        dataPoints: aDataPoints
                    }]
                });
                chartMusicas.render();

            }).catch((err) => {
                console.log(err);
            })

        });
}