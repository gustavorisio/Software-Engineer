const { responde } = require('express');
const express = require('express');

const app = express();

app.get("/", (request,response) => {

    return response.send("Inicio");
    
});

app.listen(3000);