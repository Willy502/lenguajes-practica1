import webbrowser
import os

class Helper:

    def get_file_readed(self, file):
        lists = {}
        for line in file:
            data_options = {}
            list_name = "".join(line.split("=")[0].split())
            to_trim_list = line.split("=")[1].upper()
            
            if "ORDENAR" in to_trim_list:
                data_options["ORDENAR"] = True

                if "BUSCAR" not in to_trim_list:
                    data_options["BUSCAR"] = False
                    data_options["DATA"] = "".join(to_trim_list.split("ORDENAR")[0].split())

                else:
                    data_lists = to_trim_list.split("ORDENAR")
                    if "BUSCAR" not in data_lists[0]:
                        data_list = "".join(data_lists[0].split())
                        data_options["BUSCAR"] = "".join(data_lists[1].split("BUSCAR")[1].split())
                    else:
                        data_list = "".join(data_lists[0].split("BUSCAR")[0].split())
                        data_options["BUSCAR"] = "".join(data_lists[0].split("BUSCAR")[1].split())
                    data_options["DATA"] = data_list
                    
            else:
                data_options["ORDENAR"] = False
                data_options["BUSCAR"] = False
                if "BUSCAR" in to_trim_list:
                    data_list = "".join(to_trim_list.split("BUSCAR")[0].split())
                    data_options["DATA"] = data_list
                    data_options["BUSCAR"] = "".join(to_trim_list.split("BUSCAR")[1].split())

            if data_options["BUSCAR"] != False:
                if data_options["BUSCAR"][len(data_options["BUSCAR"]) - 1] == ",":
                    data_options["BUSCAR"] = data_options["BUSCAR"][:-1]

            if data_options["DATA"][len(data_options["DATA"]) - 1] == ",":
                data_options["DATA"] = data_options["DATA"][:-1]

            lists[list_name] = data_options

        print(lists)
        return lists

    def generate_html(self, data):
        generated = False
        lines = ''
        for line in data.split("\n"):
            lines += '<li class="list-group-item">' + line + '</li>\n'

        html = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

            <title>Desplegar todos</title>
        </head>
        <body>

            <div class="container">
                <div class="row">
                    <br>
                    <h1>Desplegar todas las opciones</h1>
                    <hr>
                    <ul class="list-group">'''
        html += lines
        html += '''</ul>
                </div>
            </div>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

        </body>
        </html>
        '''
        file = open('practica1.html', 'w')
        file.write(html)
        file.close()
        filename = 'file://' + os.path.realpath(file.name)
        webbrowser.open_new_tab(filename)
        generated = True
        return generated