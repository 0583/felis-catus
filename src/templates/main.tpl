<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>felis catus - the #1 worst short link redirector</title>

<body>
    <h1>{{ title }}</h1>
    <h2>{{ main_intro }}</h2>
    <h2>{{ table_title }}</h2>


<table>
    <thead>
    <th>unique id</th>
    <th>short link</th>
    <th>full link</th>
    </thead>
    <tbody>
      <meta charset="UTF-8">
    {% for item in table %}
        <tr>
            <td>{{ item[0] }}</td>
            <td><a href={{ item[3] }}>{{ item[1] }}</a></td>
            <td><a href={{ item[2] }}>{{ item[2] }}</a></td>
        </tr>
      {% endfor %}
      </tbody>
    </table>
    <h5>Copyright (c) {{ year }} @0583 Licensed under GPL-v3-or-later.</h5>
</body>
</head>

</html>