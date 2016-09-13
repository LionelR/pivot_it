import click
import copy


def clean(line, sep):
    """
    Clean a line
    :param line: The line as a string
    :param sep: The CSV separator
    :return: A list with cleaned data
    """
    return line.decode('utf8').strip().split(sep)


@click.command('pivot_it')
@click.argument('fin', type=click.File('rb'))
@click.argument('fout', type=click.File('wb'))
@click.option('-c', '--column', help="Column number or name after which to make the pivot. Default to 1", default='1')
@click.option('-s', '--separator', help="CSV separator. Default to comma", default=',')
@click.option('-k', '--ckey', help="New key column name, containing the old columns names. Default to 'key", default='key')
@click.option('-v', '--cval', help="New value column name, containing the pivoted values. Default to 'value'", default='value')
def run(fin, fout, column, separator, ckey, cval):
    """
    Pivot some data contained inside a CSV file after a specified column number and write the result to another file.
    The original CSV file must have a header on the first line.
    """

    lines = fin.readlines()
    header = clean(lines[0], separator)

    try:
        col = int(column)
    except:
        col = header.index(column) + 1

    keys = header[col:]
    new_header = copy.deepcopy(header[0:col])
    new_header.extend([ckey, cval])

    fout.write(bytes(separator.join(new_header) + '\n', 'UTF-8'))

    with click.progressbar(lines[1:], label='Processing') as bar:
        for nline, line in enumerate(bar):
            c_lines = clean(line, separator)
            refs = c_lines[0:col]
            values = c_lines[col:]
            for i, value in enumerate(values):
                l = copy.deepcopy(refs)
                l.extend([keys[i], value])
                fout.write(bytes(separator.join(l) + '\n', 'UTF-8'))

