from covid19viz.toolkit import register

app = register.RegisterDashApplication()
app.prepare_app()

if __name__ == "__main__":
    app._app.run_server(debug=False)
