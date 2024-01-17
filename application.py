import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage

app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

storage_context = StorageContext.from_defaults(persist_dir="site-reliability-engineer-handbook")
index = load_index_from_storage(storage_context)
query_enginge = index.as_query_engine()
print(query_enginge.query('Who is site reliability engineer?'))

@app.message("")
def message_all(message, say):
    print(message['text'])
    
    text = message['text']
    response = query_enginge.query(text)
    
    message = str(response)
    sources = json.dumps(response.get_formatted_sources(length=100))
    
    print(message)
    print(sources)
    say(message + '\n\n' + sources)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()