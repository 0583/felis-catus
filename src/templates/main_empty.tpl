<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>felis catus - the #1 worst short link redirector</title>

<body>
    <h1>{{ title }}</h1>
    <h2>{{ main_intro }}</h2>

    <h3>Submit new shorten link</h3>
    <form action="/add" method="post">
    <div>
        <label for="full_link">What's your full link?</label>
        <input name="full_link" id="full_link" value="https://www.github.com">
    </div>
    <div>
        <button>Submit</button>
    </div>
    </form>
    
    <h2>{{ table_title }}</h2>
    [ service unavailable ]

    <h4>current cpu pressure: {{ cpu_pressure }}, memory pressure: {{ memory_pressure }}</h4>
    <h5>Copyright (c) {{ year }} @0583 Licensed under GPL-v3-or-later.</h5>
</body>
</head>

</html>