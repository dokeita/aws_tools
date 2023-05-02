import boto3
import click
# import pprint

glue = boto3.client("glue")

@click.command()
@click.option('--db_name', '-d', required=True, help='database name')
@click.option('-table_name', '-t', default='', help='table name')
def main(db_name, table_name):
    # python create-gluetable-erd.py -d datasource -t dokeita_glue_datasource

    #TODO table_nameが指定されていなければtable一覧を取得する

    table_names = []
    if table_name:
        table_names.append(table_name)
    else:
        table_names = get_tables(db_name)

    table_erds = []
    for table_name in table_names:
        table_erds = table_erds + get_table_erd(db_name, table_name)


    output(db_name, table_erds)


def get_table_erd(db_name, table_name):
    print('-----')

    table = glue.get_table(DatabaseName=db_name, Name=table_name)

    name = table.get('Table').get('Name')
    columns = table.get('Table').get('StorageDescriptor').get('Columns')

    print(f'erDiagram')
    print(f'    {name} {{')
    for item in columns:
        print(f'        {item.get("Type")} {item.get("Name")}')
    print(f'    }}')

    lines = []
    lines.append(f'```mermaid\n')
    lines.append(f'erDiagram\n')
    lines.append(f'    {name} {{\n')
    for item in columns:
        lines.append(f'        {item.get("Type")} {item.get("Name")}\n')
    lines.append(f'    }}\n')
    lines.append(f'```\n')

    return lines

def output(db_name, lines):
    print(lines)
    with open(f'{db_name}.md', 'w', encoding="utf-8", newline='') as f:
        f.writelines(lines)


def get_tables(db_name):
    tables = []
    response = glue.get_tables(DatabaseName=db_name)
    if response:
        for table in response.get('TableList'):
            tables.append(table.get('Name'))

    while 'NextToken' in response:
        response = glue.get_tables(DatabaseNam=db_name, NextToken=response.get('NextToken'))
        if response:
            for table in response.get('TableList'):
                tables.append(table.get('Name'))

    return tables

if __name__ == '__main__':
    main()