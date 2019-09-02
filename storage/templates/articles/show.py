def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>''' + str(kwargs['article'].name) + '''</title>
</head>
<body>
    <h1>''' + str(kwargs['article'].name) + '''</h1>
    <h5>''' + str(kwargs['article'].text) + '''</h5>
</body>
</html>    '''
    return template