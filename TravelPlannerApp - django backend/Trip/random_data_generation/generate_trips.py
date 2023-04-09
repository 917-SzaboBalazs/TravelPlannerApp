import datetime

from faker import Faker

fake = Faker()

with open("insert_trips.sql", "w") as file:
    for i in range(1000):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_trip\"(id, name, destination, budget, " + \
                       "start_date, end_date, notes)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            id = i * 1000 + j + 1
            name = fake.sentence(nb_words=4, variable_nb_words=True)[:-1].replace('\'', '')
            destination = fake.country().replace('\'', '')
            budget = fake.random.randint(5, 30) * 1000
            start_date = fake.date_between()
            end_date = fake.date_between(start_date=start_date + datetime.timedelta(days=3),
                                         end_date=start_date + datetime.timedelta(days=30))

            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            notes = fake.paragraph(nb_sentences=4, variable_nb_sentences=True).replace('\'', '')

            sql_command += "({}, \'{}\', \'{}\', {}, \'{}\', \'{}\', \'{}\'),\n"\
                .format(id, name, destination, budget, start_date_str, end_date_str, notes)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
