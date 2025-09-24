

async function puxando_api() {
    const response = await fetch("http://localhost:8000/api/v1/bandas");
    const data = await response.json();

    return data;
}

// Mostrar as informações no Front-end
async function mostrar_bandas() {
    const bandas = await puxando_api();
    const container = document.getElementById("bandas_container");

    bandas.forEach(bandas => {
        const bandaDiv = document.createElement('div');
        bandaDiv.classList.add('banda');
        bandaDiv.innerHTML = `
            <h2>${banda.nome}</h2>
            <p>${banda.qtd_integrantes}</p>
            <p>${banda.tipo_musical}</p>
        `;

        container.appendChild(bandaDiv);
    });
}


/*
async function puxar_api() {
    await axios.get("http://localhost:8000/api/v1/bandas").then((response) => {
        const bandas = response.data;
        const container = document.getElementById("bandas_container");
        bandas.forEach(element => {
            const bandaDiv = document.getElementById('div');
            bandaDiv.classList.add('banda');
            bandaDiv.innerHTML = `
            <h2>${banda.nome}</h2>
            <p>${banda.qtd_integrantes}</p>
            <p>${banda.tipo_musical}</p>
        `
        container.append(bandaDiv);
        });
    })
}

puxar_api()
*/