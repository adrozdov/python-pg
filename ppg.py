import psycopg2
from psycopg2 import Error

def main():
    print('connecting to postgres')

try:
    conn = psycopg2.connect(database="braveaipcn_dev",
                            user="postgres",
                            password="password",
                            host="192.168.64.2",
                            port="8432")
    cur = conn.cursor()

    print("Server information")
    print(conn.get_dsn_parameters(), "\n")

    print("load list")
    nhs_number_ar = []
    nhs_number_list = ''
    data_file = open('nhs_numbers.txt', 'r')
    for line in data_file:
        nhs_number_ar.append(line.strip())
        nhs_number_list = nhs_number_list + line + ", "
    data_file.close()

    # print('data: ')
    # print(nhs_number_list)

    # query = "SELECT * FROM ehr LIMIT 10;"

    # query = """
    # SELECT column_name, data_type, is_nullable
    # FROM information_schema.columns
    # WHERE table_name = 'ehr';
    # """

    query = "SELECT * FROM ehr WHERE nhs_number IN %s"

    cur.execute(query, (nhs_number_list,))
    res = cur.fetchall()

    print(res)

except (Exception, Error) as error:
    print("Error connecting to database: ", error)
finally:
    if (conn):
        cur.close()
        conn.close()
        print("Database connection closed")

if __name__ == '__main__':
    main()