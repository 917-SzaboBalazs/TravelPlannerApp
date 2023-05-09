from faker import Faker

fake = Faker()

with open("insert_users.sql", "w") as file:
    for i in range(10):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"auth_user\"(id, password, username, is_superuser, " + \
                       "first_name, last_name, email, is_staff, is_active, date_joined)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            profile = fake.simple_profile()

            id = i * 1000 + j + 1
            password = 'pass1234'
            username = profile['username'] + "_" + str(id)
            is_superuser = False
            first_name = profile['name'].split()[0]
            last_name = profile['name'].split()[1]
            email = profile['mail'].split('@')[0] + '_' + str(id) + '@' + profile['mail'].split('@')[1]
            is_staff = False
            is_active = True
            date_joined = '2023-12-15'

            sql_command += "({}, \'{}\', \'{}\', {}, \'{}\', \'{}\', \'{}\', {}, {}, \'{}\'),\n"\
                .format(id, password, username, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
