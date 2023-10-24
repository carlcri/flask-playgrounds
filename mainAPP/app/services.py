import pprint, psycopg2, click
from psycopg2.extras import RealDictCursor

class EmployeeService:

    @staticmethod
    def query_employee_by_id(connection_string: str, id: int) -> dict:

        NEON_URI = connection_string

        try:
            conn = psycopg2.connect(NEON_URI)

        except:
            print("I am unable to connect to the database") 

        else:

            sql =f'''SELECT id,name,lastname, birthdate FROM employees 
                     WHERE id = {id}'''
            
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            print("Connected!\n")

            cursor.execute(sql)
            record = cursor.fetchall()

#            pprint.pprint(record)
            print(f'numero de registros: {len(record)}')

            if len(record) != 0:
                record = dict(record[0])
            else:
                record = {}

            conn.close()
            cursor.close()

            return record
        
        
    @staticmethod    
    def insert_employee(connection_string: str, name, lastname, birthdate):

        NEON_URI = connection_string

        try:
            conn = psycopg2.connect(NEON_URI)

        except:
            print("I am unable to connect to the database") 

        else:

            if len(birthdate) != 0:
                sql = f'''INSERT INTO employees(name, lastname, birthdate)
                    VALUES ('{name}', '{lastname}', '{birthdate}') returning id;'''
            else: 
                sql = f'''INSERT INTO employees(name, lastname)
                    VALUES ('{name}', '{lastname}') returning id;'''
            
            cursor = conn.cursor()

            print("Connected from insert employee!\n")

            cursor.execute(sql)
            returned_id = cursor.fetchone()[0]
            print(f'returned id={returned_id}')
            conn.commit()

            conn.close()
            cursor.close()

            return returned_id        

