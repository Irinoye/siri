// Import necessary modules
import express from 'express';
import serveStatic from 'serve-static';
import { join } from 'path';
import { fileURLToPath } from 'url';

// Set up __dirname in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = join(__filename, '..');

// Create Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the "public" folder
app.use(serveStatic(join(__dirname, 'public')));

// Route for serving index.html
app.get('/', (_req, res) => {
    res.sendFile(join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
