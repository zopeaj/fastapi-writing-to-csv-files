import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

import csv
from fastapi.responses import Response, StreamingResponse
from django.template import loader

from typing import List


class CsvService:
    def __init__():
        pass

    def writeCsv(self, response: Response, data: List[str]) -> Response:
        writer = csv.writer(response)
        writer.writerow(data)
        return response

    def write(self, value):
        return value

    def stream_csv_view(data: int) -> None:
        rows = (["Row {}".format(idx), str(idx)] for idx in range(data))
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        return writer

    def some_view(response: Response):
        csv_data =  (('First row', 'Foo', 'Bar', 'Baz'), ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),)

        t = loader.get_template('my_template_name.txt')
        c = {'data': csv_data}
        response.write(t.render(c))
        return response
