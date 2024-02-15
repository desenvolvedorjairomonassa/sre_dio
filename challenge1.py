# Define a list of tuples containing the names of metrics and the corresponding input values
metrics = [
    ('CPU', int(input())),
    ('RAM memory', int(input())),
    ('response time', int(input()))
]

# TODO: Define a function to monitor the metrics and generate alerts, if necessary
def monitor_and_alert(metrics):
    alerts = []

    # TODO: Iterate over each metric in the provided metrics list and check if any alerts were generated
    for metric_name, metric_value in metrics:
      if ((metric_name == 'CPU') and (metric_value>=80)):
        alert = f'Alert: High CPU usage detected ({metric_value}%)'
        alerts.append(alert)
      if ((metric_name == 'RAM memory') and (metric_value>=70)):
        alert = f'Alert: High RAM memory usage detected ({metric_value}%)'
        alerts.append(alert)
      if ((metric_name == 'response time') and (metric_value>250)):
        alert = f'Alert: Application response time above the limit ({metric_value}ms)'
        alerts.append(alert)
    if alerts == []:
      alerts.append('No anomalies detected')
    return '\n'.join(alerts)

print(monitor_and_alert(metrics))
