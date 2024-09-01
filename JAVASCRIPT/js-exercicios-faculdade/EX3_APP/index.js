const express = require('express');

const EX2_APP = express();

app.get("/", (request, response) => {
    return response.send("API no ar");
});

console.log("Start Server:3000");
app.listen(3000);
