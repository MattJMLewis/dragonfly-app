def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create</title>
</head>
<body>
    <form method="post", action="http://localhost:8080/articles">
        Name:<br>
        <input type="text" name="name"><br>
        Text:<br>
        <input type="text" name="text">

        <input type="submit">
    </form>

</body>
</html>    '''
    return template