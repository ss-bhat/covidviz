from covid19viz.toolkit import register


app_instance = register.RegisterDashApplication()
app = app_instance.app
app.run_server(host="0.0.0.0", debug=False)
