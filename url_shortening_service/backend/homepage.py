homepage = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #555;
            text-align: center;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #e9ecef;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        #short-url-output {
            font-weight: bold;
            color: #007bff;
        }
        .url-list-container {
            margin-top: 40px;
        }
        .url-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .url-item:last-child {
            border-bottom: none;
        }
        .url-item-info {
            display: flex;
            flex-direction: column;
        }
        .short-code {
            font-weight: bold;
            color: #007bff;
            font-size: 1.1em;
        }
        .long-url {
            color: #666;
            word-break: break-all;
        }
        .visits {
            font-size: 0.9em;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>URL Shortener</h1>
        <form id="url-form">
            <input type="text" id="long-url" name="long-url" placeholder="Enter a long URL here" required>
            <button type="submit">Shorten</button>
        </form>
        <div id="result" class="result" style="display:none;">
            <p>Shortened URL:</p>
            <a id="short-url-output" href="#"></a>
        </div>
        <p id="message"></p>
        
        <div class="url-list-container">
            <h2>All Shortened URLs</h2>
            <div id="url-list">
                <!-- URLs will be dynamically added here -->
            </div>
        </div>
    </div>

    <script>
        const shortenerForm = document.getElementById('url-form');
        const longUrlInput = document.getElementById('long-url');
        const messageEl = document.getElementById('message');
        const resultEl = document.getElementById('result');
        const shortUrlOutputEl = document.getElementById('short-url-output');
        const urlListEl = document.getElementById('url-list');

        async function fetchAndDisplayUrls() {
            try {
                const response = await fetch('/api/urls');
                const urls = await response.json();
                
                urlListEl.innerHTML = '';
                if (urls.length === 0) {
                    urlListEl.innerHTML = '<p style="text-align: center; color: #888;">No URLs shortened yet.</p>';
                } else {
                    urls.forEach(url => {
                        const urlItem = document.createElement('div');
                        urlItem.className = 'url-item';
                        urlItem.innerHTML = `
                            <div class="url-item-info">
                                <a class="short-code" href="/${url.short_url}" target="_blank">/${url.short_url}</a>
                                <span class="long-url">${url.long_url}</span>
                            </div>
                            <span class="visits">Visits: ${url.visits}</span>
                        `;
                        urlListEl.appendChild(urlItem);
                    });
                }
            } catch (error) {
                console.error("Failed to fetch URLs:", error);
                urlListEl.innerHTML = '<p style="text-align: center; color: red;">Failed to load URLs.</p>';
            }
        }

        shortenerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const longUrl = longUrlInput.value;
            
            messageEl.textContent = '';
            resultEl.style.display = 'none';

            try {
                const response = await fetch('/shorten', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ long_url: longUrl })
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.detail || 'Something went wrong');
                }

                shortUrlOutputEl.textContent = `/${data.short_url}`;
                shortUrlOutputEl.href = `/${data.short_url}`;
                resultEl.style.display = 'flex';
                longUrlInput.value = '';
                
                // Refresh the list after a new URL is shortened
                fetchAndDisplayUrls();

            } catch (error) {
                messageEl.textContent = error.message;
            }
        });
        
        // Initial fetch of all URLs on page load
        fetchAndDisplayUrls();
    </script>
</body>
</html>
"""
