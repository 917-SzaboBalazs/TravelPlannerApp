from faker import Faker

fake = Faker()

with open("insert_activities.sql", "w") as file:
    for i in range(1000):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_activity\"(id, name, description, price, no_persons, has_instructor)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            id = i * 1000 + j + 1
            name = fake.job().replace('\'', '')
            description = fake.paragraph(nb_sentences=2, variable_nb_sentences=True).replace('\'', '')
            price = fake.random.randint(10, 100)
            no_persons = fake.random.randint(1, 10)
            has_instructor = fake.boolean(chance_of_getting_true=30)

            sql_command += "({}, \'{}\', \'{}\', {}, {}, {}),\n"\
                .format(id, name, description, price, no_persons, has_instructor)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
