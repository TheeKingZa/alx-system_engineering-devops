#!/usr/bin/python3
"""
Monitoring Configurations
"""
import datadog
from datadog import api
# Set up Datadog credentials
options = {
    'api_key': 'd637ef54d729ec19d8fb2849ea166d39',
    'app_key': '1b4d4a0e57235b17cdad2a5ee6e8a40850989c68'
}
datadog.initialize(**options)
# Collect and send metrics
metric_name = 'custom.metric.read_requests'
value = 42  # Metric value
api.Metric.send(metric=metric_name, points=value)
