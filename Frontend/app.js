//express app that serves html file
const express = require("express");
const app = express();
const port = 3000;
const path = require("path");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/", async (req, res) => {
  try {
    const response = await fetch("http://localhost:5000/api");
    const result = await response.json();
    res.render("index", { data: result.data, error: null });
  } catch (error) {
    console.error("Error fetching data:", error);
    res.render("index", { data: null, error: error.message });
  }
});

app.use(express.static(path.join(__dirname, "public")));

app.listen(3000, () => {
  console.log(`Frontend app listening at http://localhost:${port}`);
});
