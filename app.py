from covid19viz.toolkit import register


if __name__ == "__main__":
    app_instance = register.RegisterDashApplication()
    app = app_instance.app
    app.run_server(debug=False)
