import express from "express";
import fetch from "node-fetch";

const app = express();
const PORT = 4000;

// Endpoint to simulate authentication flow
app.get("/authenticate", (req, res) => {
  // Simulate redirecting the user to an external API for authentication
  const redirectUrl = `http://localhost:3000/callback`;

  // Simulate an "access token" being sent back to the callback
  const accessToken = "mock_access_token_12345";

  // Make a POST request to the server's callback endpoint
  fetch(redirectUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ access_token: accessToken }),
  })
    .then((response) => response.text())
    .then((data) => {
      res.send(`
        <h1>Authentication Successful!</h1>
        <p>Response from callback server:</p>
        <pre>${data}</pre>
      `);
    })
    .catch((error) => {
      console.error("Error sending to callback:", error);
      res.status(500).send("Something went wrong.");
    });
});

// Start the client
app.listen(PORT, () => {
  console.log(`Client is running on http://localhost:${PORT}`);
});
