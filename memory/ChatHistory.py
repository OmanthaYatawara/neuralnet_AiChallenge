from langchain_community.chat_message_histories import SQLChatMessageHistory
from sqlalchemy import create_engine
from .InitilizeDatabase import engine,message_store

def get_session_history(session_id):
    # Create a connection to the database
    with engine.connect() as conn:
        # Perform a query to check if the session ID exists
        result = conn.execute(
            message_store.select().where(message_store.c.session_id == session_id)
        ).fetchone()

    # Check if the result is None (no session ID found) or contains data (session ID exists)
    if result is None:
        history=SQLChatMessageHistory(session_id=session_id, connection=engine)
        history.__init__(session_id=session_id, connection=engine)
        return history
    else:
        history=SQLChatMessageHistory(session_id=session_id, connection=engine)
        return history

def add_chat_history(session_id,messages):
    history=SQLChatMessageHistory(session_id=session_id, connection=engine)
    history.clear()
    history.add_messages(messages)

def clear_chat_history(session_id):
    history=SQLChatMessageHistory(session_id=session_id, connection=engine)
    history.clear()