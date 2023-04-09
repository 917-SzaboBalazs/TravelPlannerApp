from faker import Faker

fake = Faker()

for file_index in range(1, 6):

    file_name = "insert_trip_transportations_" + str(file_index) + ".sql"
    start_index = (file_index - 1) * 2_000_000

    with open(file_name, "w") as file:
        for i in range(2000):
            sql_command = ""

            # Add command row
            sql_command += "INSERT INTO public.\"Trip_trip_transportations\"(id, trip_id, transportation_id)\n"
            sql_command += "VALUES\n"

            # Add values
            for j in range(1000):
                id = i * 1000 + j + 1 + start_index
                trip_id = (id - 1) // 10 + 1
                transportation_id = fake.unique.random_int(1, 1_000_000)

                sql_command += "({}, {}, {}),\n"\
                    .format(id, trip_id, transportation_id)

            fake.unique.clear()

            sql_command = sql_command[:-2]
            sql_command += "\n;\n"

            print(sql_command, file=file)
