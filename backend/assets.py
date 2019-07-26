START_HTML = """
<html>

<head>
  <link rel="stylesheet" href="css/reveal.css">
  <link rel="stylesheet" href="css/theme/white.css">
</head>

<body>
  <div class="reveal">
    <div class="slides">
"""


def slide_html(text, img_url):
    return f"""
            <section data-background-image="{img_url}>"
                <h1>{text}</h1>
            </section>
            """


END_HTML = """
            </div>
        </div>
        <script src="js/reveal.js"></script>
        <script>
            Reveal.initialize();
        </script>
        </body>

        </html>
"""


test_deck = {
    "slides": [
        {
            "title": "Hello!",
            "img_url": "https://images.unsplash.com/photo-1562184760-a11b3cf7c169?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
        },
        {
            "title": "This is my deck!",
            "img_url": "https://images.unsplash.com/photo-1562184724-0b0833e5ba27?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=3766&q=80",
        },
        {
            "title": "And we're done!",
            "img_url": "https://images.unsplash.com/photo-1562184647-979b4a9f0b23?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=3900&q=80",
        },
    ]
}

