import streamlit as st

column_name = ['date','topic','who']
column_full_name = ['DATING DATE','TOPIC','WHO WOULD JOIN']
column_value = column_name

#You can place something after the url to assign value, might be helpful when you had some function to redirect to here.
#ex: mail urlXXX/?date=2022-01-01&topic=party&who=Dan

def some_function(value):
    st.write("This line is run inside some expandable function...")
    #inside some function here, you can connect to SQL to write data in and/or get some data back.
    return value

try:
    query_params = st.experimental_get_query_params()
    for i in range(0,len(column_name)):
        column_value[i] = st.text_input(column_full_name[i], str(query_params[column_value[i]][0]))
except:
    for i in range(0,len(column_name)):
        column_value[i] = st.text_input(column_full_name[i], 'Please enter value here')
if st.button('Enter'):
    return_list = some_function(column_value)
    st.write(f"Your dating time is {return_list[0]}, topic is {return_list[1]} and {return_list[2]} would particapate with you.")