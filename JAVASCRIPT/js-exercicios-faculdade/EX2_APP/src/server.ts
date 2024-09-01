import express from "express";

const app = express();

app.use(express.json());

console.log("Start Server:3000");
app.listen(3000);
