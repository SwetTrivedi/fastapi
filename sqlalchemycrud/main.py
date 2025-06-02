from tables import create_tables
from services import *

create_tables()
# Create the Data 

# create_user("swet","swet@gmail.com")
# create_user("ashish","ashish@gmail.com")

# Create the post the data 
# create_post(1,"HelloWorld","This is Swet first post ")
# create_post(2,"HelloWorld","This is ashish first post ")

#Get the single data 
# print(get_user_by_id(1))
# print(get_all_users())
# print(get_posts_by_user(2))


# update the data 

# update_user_email(1,"swettrivedi@gmail.com")

#delete_data

# delete_post(2)

# order by
# print(get_user_ordered_by_name())
# print(get_post_latest_first())

# Group by 
# print(get_post_count_per_user())

# join 
# print(get_posts_with_author())

# raw sql queries 
# print(raw_sql_insert())
print(raw_sql_example())