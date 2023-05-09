from faker import Faker

fake = Faker()

with open("insert_user_profiles.sql", "w") as file:
    for i in range(10):
        sql_command = ""

        # Add command row
        sql_command += "INSERT INTO public.\"Trip_userprofile\"(id, bio, location, gender, " + \
                       "phone_number, user_id)\n"
        sql_command += "VALUES\n"

        # Add values
        for j in range(1000):
            profile = fake.profile()

            id = i * 1000 + j + 1
            bio = 'I am a(n) ' + profile['job'].replace('\'', '')
            location = profile['address'].replace('\'', '').split('\n')[0]
            gender = profile['sex']
            phone_number = '07'

            for _ in range(8):
                digit = fake.pyint(0, 9)
                phone_number += str(digit)

            user_id = id

            sql_command += "({}, \'{}\', \'{}\', \'{}\', \'{}\', {}),\n"\
                .format(id, bio, location, gender, phone_number, user_id)

        sql_command = sql_command[:-2]
        sql_command += "\n;\n"

        print(sql_command, file=file)
