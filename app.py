from covid19viz.toolkit import register


app_instance = register.RegisterDashApplication()
app = app_instance.app
app.run_server(debug=False)
