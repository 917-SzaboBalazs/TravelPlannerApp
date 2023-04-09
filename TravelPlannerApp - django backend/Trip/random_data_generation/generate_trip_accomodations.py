from faker import Faker

fake = Faker()

with open("insert_trip_accommodations.sql", "w") as file:
    for i in range(10000):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_trip_accommodations\"(id, trip_id, accommodation_id)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            id = i * 1000 + j + 1
            trip_id = (id - 1) // 10 + 1
            accommodation_id = fake.unique.random_int(1, 1_000_000)

            sql_command += "({}, {}, {}),\n"\
                .format(id, trip_id, accommodation_id)

        fake.unique.clear()

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
