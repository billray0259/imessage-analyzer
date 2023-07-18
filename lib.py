import pandas as pd
import sqlite3
import os
import numpy as np


INTERESTING_COLUMNS = ['message.guid', 'message.text', 'message.date', 'handle.id', 'message.is_from_me', 'chat.guid']


def find_database_file(start_dir='/', file_name='chat.db', hints=None, error=True):
    if file_name in os.listdir(start_dir) and os.path.isfile(os.path.join(start_dir, file_name)):
        return os.path.join(start_dir, file_name)
    
    hints = ['Users', '*', 'Library', 'Messages'] if hints is None else hints
    hint = hints[0]
    if hint == '*':
        for d in os.listdir(start_dir):
            d_path = os.path.join(start_dir, d)
            if os.path.isdir(d_path):
                found = find_database_file(d_path, file_name, hints[1:], error=False)
                if found is not None:
                    return found
        if error:
            raise FileNotFoundError(f'Could not find database file {file_name} in {start_dir}')
        else:
            return None
    
    hint_path = os.path.join(start_dir, hint)

    if not os.path.isdir(hint_path):
        if error:
            raise FileNotFoundError(f'Could not find database file {file_name} in {start_dir}')
        else:
            return None

    return find_database_file(hint_path, file_name, hints[1:])



def fetch_data(columns=None, db=None):
    if db is None:
        db = find_database_file()
    
    if columns is None:
        columns = INTERESTING_COLUMNS

    if type(db) is str:
        db_connection = sqlite3.connect(db)
        db_cursor = db_connection.cursor()
    elif type(db) is sqlite3.Connection:
        db_cursor = db.cursor()
    elif type(db) is sqlite3.Cursor:
        db_cursor = db

    if isinstance(columns, str):
        columns = [columns]

    # Join the columns into a comma-separated string
    columns_str = ', '.join(columns)

    SQL_CMD = f"""
    SELECT 
        {columns_str}
    FROM 
        message
    LEFT JOIN 
        chat_message_join ON message.ROWID = chat_message_join.message_id
    LEFT JOIN 
        chat ON chat_message_join.chat_id = chat.ROWID
    LEFT JOIN 
        handle ON message.handle_id = handle.ROWID
    LEFT JOIN 
        message_attachment_join ON message.ROWID = message_attachment_join.message_id
    LEFT JOIN 
        attachment ON message_attachment_join.attachment_id = attachment.ROWID;
    """
    # fetch all the messages
    db_cursor.execute(SQL_CMD)
    messages = db_cursor.fetchall()
    column_names = columns

    df = pd.DataFrame(messages)
    df.columns = column_names
    return df


def clean_data(data):
    messages = data.copy()
    if 'message.text' in data.columns:
        messages = messages.dropna(subset=['message.text'])
        messages['is_reaction'] = messages['message.text'].str.startswith(('Loved “', 'Emphasized “', 'Laughed at “', 'Disliked “', 'Questioned “', 'Liked “'))
    
    if 'message.date' in data.columns:
        messages.loc[:, 'message.date'] = pd.to_datetime(messages['message.date'] / 1000000000 + 978307200, unit='s')
        messages = messages.sort_values(by='message.date')
    
    if 'message.is_from_me' in data.columns:
        messages.loc[:, 'message.is_from_me'] = messages['message.is_from_me'].astype(bool)

    messages.set_index(np.arange(len(messages)), inplace=True)

    return messages



    
