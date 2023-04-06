from faker import Faker
from faker_vehicle import VehicleProvider


fake = Faker()
fake.add_provider(VehicleProvider)

with open("insert_transportations.sql", "w") as file:
    for i in range(1000):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_transportation\"(id, name, price, speed, comfort_level, " + \
                       "type_id)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            id = i * 1000 + j + 1
            name = fake.vehicle_make().replace('\'', '')
            price = fake.random.randint(10, 50) * 10
            speed = fake.random.choice(["SLOW", "MEDIUM", "FAST"])
            comfort_level = fake.random.randint(1, 5)
            type_id = fake.random.randint(1, 20)

            sql_command += "({}, \'{}\', {}, \'{}\', {}, {}),\n"\
                .format(id, name, price, speed, comfort_level, type_id)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
