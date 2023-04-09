from faker import Faker

fake = Faker()

with open("insert_accommodations.sql", "w") as file:
    for i in range(1000):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_accommodation\"(id, name, no_stars, location, " + \
                       "price_per_night, type_id, check_in_time, check_out_time)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            id = i * 1000 + j + 1
            name = fake.company().replace('\'', '')
            no_star = fake.random.randint(1, 5)
            location = fake.country().replace('\'', '')
            price_per_night = fake.random.randint(10, 50) * 100
            type_id = fake.random.randint(1, 20)
            check_in_time = fake.time()
            check_out_time = fake.time()

            sql_command += "({}, \'{}\', {}, \'{}\', {}, {}, \'{}\', \'{}\'),\n"\
                .format(id, name, no_star, location, price_per_night, type_id, check_out_time, check_out_time)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
