import webview

if __name__ == '__main__':
    url = 'http://localhost:8501'  # Replace with the URL of your locally hosted Streamlit app
    webview.create_window("My Streamlit Desktop App", url, width=800, height=600)
    webview.start()
