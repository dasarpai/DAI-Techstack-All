const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Callback endpoint
app.post("/callback", (req, res) => {
  const { access_token } = req.body;

  if (access_token) {
    console.log("Access token received:", access_token);
    res.send("Authorization successful! Access token received.");
  } else {
    res.status(400).send("No access token received.");
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
