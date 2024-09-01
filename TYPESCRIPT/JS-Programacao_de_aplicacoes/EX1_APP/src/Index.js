const express = require('express');

const app = express();

app.get("/", (request, response) => {
    return response.send("API no ar");
});

console.log("Start Server:3000");
app.listen(3000);
