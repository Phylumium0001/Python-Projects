homepage = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shorten Your Link</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        input[type="text"] {
            padding: 0.75rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1rem;
            width: 300px;
        }
        button {
            padding: 0.75rem;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        #result {
            margin-top: 1rem;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>URL Shortener</h1>
        <form action="http://localhost/shorten" id="shortenForm" method="post">
            <input type="text" name="long_url" id="longUrlInput" placeholder="Enter a long URL" required>
            <button type="submit">Shorten</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        document.getElementById('shortenForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const resultDiv = document.getElementById('result');
            const longUrl = document.getElementById('longUrlInput').value
            console.log(longUrl)
            try{
                const response = await fetch("/shorten",{
                    method:'POST',
                    headers:{
                        'Content-Type' : 'application/json'
                    },
                    body: JSON.stringify({long_url:longUrl})
                })

                const data = await response.json();

                console.log(data)
                if (response.ok){
                    resultDiv.innerHTML = `<p>Your short URL is <a href='${data.short_url.replace("shlk.com/","")}' target='_blank'>${data.short_url}</a></p>`
                }else{
                    resultDiv.innerHTML = `<p style="color:red">Error: ${data.detail}</p>`
                }

            }catch(error){
            resultDiv.innerHTML= `<p style="color :red;">Failed to connect to the server</p>`
            }


        });
    </script>
</body>
</html>"""
