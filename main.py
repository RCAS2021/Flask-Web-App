from website import create_app

app = create_app()

# Executes only if running this file, not if importing
if __name__ == "__main__":
    # Run runs the flask application, start the web-server.
    # Debug = True reruns the web-server on every change. Turn off in production
    app.run(debug=True)
